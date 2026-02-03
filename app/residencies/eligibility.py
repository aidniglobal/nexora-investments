"""
Eligibility checker service for residency programs
Validates applicant criteria against program requirements
"""
from typing import List, Tuple, Dict, Any
from datetime import datetime
import uuid
from app.residencies.models import ResidencyProgram
from app.residencies.schemas import (
    EligibilityCheckRequest, 
    EligibilityCheckResponse, 
    EligibilityMatchDetail,
    ResidencyProgramSchema
)
from models import db


class EligibilityChecker:
    """
    Service for checking applicant eligibility against residency programs
    Matches criteria: investment_budget, net_worth, family_size
    """
    
    def __init__(self):
        self.currency_rates = {
            'USD': 1.0,
            'EUR': 0.92,
            'GBP': 0.79,
            'CAD': 1.36,
            'AUD': 1.52,
            'SGD': 1.34,
            'AED': 3.67,
            'CHF': 0.88,
        }
    
    def check_eligibility(self, request: EligibilityCheckRequest) -> EligibilityCheckResponse:
        """
        Check eligibility against available programs
        Returns top 5 matching programs
        """
        request_id = f"req_{uuid.uuid4().hex[:8]}"
        
        # Get all programs or filter by country preference
        query = ResidencyProgram.query
        if request.country_preference:
            query = query.filter_by(country=request.country_preference)
        
        programs = query.all()
        
        # Calculate match details for each program
        matches: List[Tuple[ResidencyProgram, float, EligibilityMatchDetail]] = []
        
        for program in programs:
            score, detail = self._calculate_match_score(program, request)
            if score > 0:  # Only include programs with at least some match
                matches.append((program, score, detail))
        
        # Sort by score descending and take top 5
        matches.sort(key=lambda x: x[1], reverse=True)
        top_matches = matches[:5]
        
        # Convert to response schema
        matching_programs = [
            ResidencyProgramSchema(**program.to_dict()) 
            for program, _, _ in top_matches
        ]
        
        # Calculate overall eligibility score
        overall_score = sum(score for _, score, _ in top_matches) / len(top_matches) if top_matches else 0
        
        # Build message
        if not top_matches:
            message = "No matching programs found based on your criteria. Consider adjusting your budget or preferences."
        elif len(top_matches) == 1:
            message = f"Found 1 matching program based on your investment budget of ${request.investment_budget:,.0f}"
        else:
            message = f"Found {len(top_matches)} matching programs based on your criteria"
        
        return EligibilityCheckResponse(
            request_id=request_id,
            status="success",
            timestamp=datetime.utcnow().isoformat() + "Z",
            matching_programs=matching_programs,
            eligibility_score=round(overall_score, 2),
            message=message
        )
    
    def _calculate_match_score(
        self, 
        program: ResidencyProgram, 
        request: EligibilityCheckRequest
    ) -> Tuple[float, EligibilityMatchDetail]:
        """
        Calculate match score for a program
        Returns (score, detail_object)
        """
        score = 0.0
        matching_factors = []
        potential_issues = []
        
        # 1. Investment Amount Check (40% of score)
        investment_fit = self._check_investment_fit(program, request, matching_factors, potential_issues)
        if investment_fit:
            score += 40
        
        # 2. Family Size Check (30% of score)
        family_fit = self._check_family_fit(program, request, matching_factors, potential_issues)
        if family_fit:
            score += 30
        
        # 3. Net Worth Check (20% of score)
        net_worth_fit = self._check_net_worth_fit(program, request, matching_factors, potential_issues)
        if net_worth_fit:
            score += 20
        
        # 4. Program Type Preference (10% of score)
        if request.program_type_preference and program.program_type:
            if request.program_type_preference.value == program.program_type:
                score += 10
                matching_factors.append(f"Matches your preferred program type ({request.program_type_preference.value})")
        
        detail = EligibilityMatchDetail(
            program_id=program.id,
            program_name=program.program_name,
            country=program.country,
            match_score=round(score, 1),
            investment_fit=investment_fit,
            family_fit=family_fit,
            net_worth_fit=net_worth_fit,
            matching_factors=matching_factors,
            potential_issues=potential_issues
        )
        
        return score, detail
    
    def _check_investment_fit(
        self, 
        program: ResidencyProgram, 
        request: EligibilityCheckRequest,
        matching_factors: List[str],
        potential_issues: List[str]
    ) -> bool:
        """Check if investment budget meets program requirements"""
        if not program.investment_min_amount:
            return True  # No requirement
        
        # Convert request budget to program currency if needed
        converted_budget = self._convert_currency(
            request.investment_budget,
            'USD',
            program.investment_currency
        )
        
        if converted_budget >= program.investment_min_amount:
            matching_factors.append(
                f"Investment budget (${request.investment_budget:,.0f}) meets minimum requirement"
            )
            return True
        else:
            shortfall = program.investment_min_amount - converted_budget
            potential_issues.append(
                f"Investment shortfall of {program.investment_currency}{shortfall:,.0f} "
                f"(required: {program.investment_currency}{program.investment_min_amount:,.0f})"
            )
            return False
    
    def _check_family_fit(
        self, 
        program: ResidencyProgram, 
        request: EligibilityCheckRequest,
        matching_factors: List[str],
        potential_issues: List[str]
    ) -> bool:
        """Check if family size is within program limits"""
        if not program.family_size_limit:
            return True  # No limit
        
        if request.family_size <= program.family_size_limit:
            matching_factors.append(
                f"Family size ({request.family_size}) within limit ({program.family_size_limit})"
            )
            return True
        else:
            potential_issues.append(
                f"Family size ({request.family_size}) exceeds program limit ({program.family_size_limit})"
            )
            return False
    
    def _check_net_worth_fit(
        self, 
        program: ResidencyProgram, 
        request: EligibilityCheckRequest,
        matching_factors: List[str],
        potential_issues: List[str]
    ) -> bool:
        """Check if net worth meets program requirements"""
        if not program.net_worth_required:
            return True  # No requirement
        
        if request.net_worth >= program.net_worth_required:
            matching_factors.append(
                f"Net worth (${request.net_worth:,.0f}) meets requirement"
            )
            return True
        else:
            shortfall = program.net_worth_required - request.net_worth
            potential_issues.append(
                f"Net worth shortfall of ${shortfall:,.0f} "
                f"(required: ${program.net_worth_required:,.0f})"
            )
            return False
    
    def _convert_currency(self, amount: float, from_currency: str, to_currency: str) -> float:
        """Convert amount between currencies"""
        if from_currency == to_currency:
            return amount
        
        from_rate = self.currency_rates.get(from_currency, 1.0)
        to_rate = self.currency_rates.get(to_currency, 1.0)
        
        # Convert to USD first, then to target currency
        in_usd = amount / from_rate
        converted = in_usd * to_rate
        
        return round(converted, 2)
    
    def get_currency_rate(self, from_currency: str, to_currency: str) -> float:
        """Get exchange rate between two currencies"""
        if from_currency == to_currency:
            return 1.0
        
        from_rate = self.currency_rates.get(from_currency, 1.0)
        to_rate = self.currency_rates.get(to_currency, 1.0)
        
        return round(to_rate / from_rate, 4)


# Singleton instance
eligibility_checker = EligibilityChecker()
