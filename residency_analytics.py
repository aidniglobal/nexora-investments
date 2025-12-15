"""
Nexora Residency Analytics Module
Enhanced comparison and analysis based on passports.io and residencies.io patterns
"""

from residency_data import residency_programs

def get_program_analytics(country=None, program_name=None):
    """Get detailed analytics for residency programs"""
    analytics = {
        "total_programs": 0,
        "total_countries": 0,
        "average_investment": 0,
        "programs_with_citizenship": 0,
        "popular_programs": [],
        "best_value_programs": [],
        "fastest_processing": [],
        "programs_by_type": {},
        "investment_range": {
            "under_50k": [],
            "50k_to_250k": [],
            "250k_to_500k": [],
            "above_500k": []
        }
    }
    
    programs_data = []
    
    for country_name, programs in residency_programs.items():
        if country and country_name.lower() != country.lower():
            continue
            
        for prog_name, prog_data in programs.items():
            if program_name and prog_name.lower() != program_name.lower():
                continue
            
            analytics["total_programs"] += 1
            
            # Program type analysis
            prog_type = prog_data.get('residency_type', 'Other')
            if prog_type not in analytics["programs_by_type"]:
                analytics["programs_by_type"][prog_type] = []
            analytics["programs_by_type"][prog_type].append({
                "country": country_name,
                "program": prog_name,
                "data": prog_data
            })
            
            # Citizenship path analysis
            if prog_data.get('path_to_citizenship') and prog_data.get('path_to_citizenship').lower() != 'no citizenship path':
                analytics["programs_with_citizenship"] += 1
            
            # Popular programs
            if prog_data.get('popular'):
                analytics["popular_programs"].append({
                    "country": country_name,
                    "program": prog_name,
                    "visa_free": prog_data.get('visa_free_countries', 0)
                })
            
            # Investment categorization
            if 'investment_types' in prog_data:
                for inv_type, inv_data in prog_data['investment_types'].items():
                    min_str = inv_data['minimum'].replace('€', '').replace('£', '').replace('CAD $', '').replace('AUD $', '').replace('AED', '').replace('SGD $', '').replace('/year', '').replace(',', '').strip()
                    try:
                        min_amount = float(min_str)
                        programs_data.append(min_amount)
                        
                        # Categorize by investment range
                        if min_amount < 50000:
                            analytics["investment_range"]["under_50k"].append({
                                "country": country_name,
                                "program": prog_name,
                                "amount": f"€{min_amount:,.0f}",
                                "type": inv_type
                            })
                        elif min_amount < 250000:
                            analytics["investment_range"]["50k_to_250k"].append({
                                "country": country_name,
                                "program": prog_name,
                                "amount": f"€{min_amount:,.0f}",
                                "type": inv_type
                            })
                        elif min_amount < 500000:
                            analytics["investment_range"]["250k_to_500k"].append({
                                "country": country_name,
                                "program": prog_name,
                                "amount": f"€{min_amount:,.0f}",
                                "type": inv_type
                            })
                        else:
                            analytics["investment_range"]["above_500k"].append({
                                "country": country_name,
                                "program": prog_name,
                                "amount": f"€{min_amount:,.0f}",
                                "type": inv_type
                            })
                    except:
                        pass
    
    analytics["total_countries"] = len([c for c in residency_programs.keys()])
    
    if programs_data:
        analytics["average_investment"] = f"€{sum(programs_data)/len(programs_data):,.0f}"
    
    return analytics


def compare_programs(program_list):
    """
    Compare multiple residency programs
    program_list: list of tuples [(country, program_name), ...]
    """
    comparison = {
        "programs": [],
        "investment_comparison": [],
        "processing_time_comparison": [],
        "requirements_comparison": [],
        "benefits_comparison": [],
        "cost_comparison": [],
        "family_eligibility": [],
        "citizenship_paths": [],
        "best_for": {
            "lowest_investment": None,
            "fastest_processing": None,
            "most_benefits": None,
            "best_visa_free_access": None
        }
    }
    
    min_investment = float('inf')
    min_processing = float('inf')
    max_benefits = 0
    max_visa_free = 0
    
    for country, program_name in program_list:
        if country not in residency_programs:
            continue
        
        if program_name not in residency_programs[country]:
            continue
        
        prog_data = residency_programs[country][program_name]
        
        comparison["programs"].append({
            "country": country,
            "name": program_name,
            "type": prog_data.get('residency_type'),
            "description": prog_data.get('description'),
            "visa_free": prog_data.get('visa_free_countries', 0),
            "citizenship_path": prog_data.get('path_to_citizenship', 'No citizenship path')
        })
        
        # Investment comparison
        if 'investment_types' in prog_data:
            for inv_type, inv_data in prog_data['investment_types'].items():
                comparison["investment_comparison"].append({
                    "country": country,
                    "program": program_name,
                    "type": inv_type,
                    "minimum": inv_data.get('minimum'),
                    "roi_potential": inv_data.get('roi_potential')
                })
        
        # Processing time
        processing = prog_data.get('processing_time', 'Not specified')
        comparison["processing_time_comparison"].append({
            "country": country,
            "program": program_name,
            "processing_time": processing,
            "permit_duration": prog_data.get('initial_permit_duration')
        })
        
        # Requirements
        if 'requirements' in prog_data:
            comparison["requirements_comparison"].append({
                "country": country,
                "program": program_name,
                "count": len(prog_data.get('requirements', [])),
                "requirements": prog_data.get('requirements', [])
            })
        
        # Benefits
        if 'benefits' in prog_data:
            benefits = prog_data.get('benefits', [])
            comparison["benefits_comparison"].append({
                "country": country,
                "program": program_name,
                "count": len(benefits),
                "benefits": benefits
            })
            
            if len(benefits) > max_benefits:
                max_benefits = len(benefits)
                comparison["best_for"]["most_benefits"] = f"{country} - {program_name}"
        
        # Visa-free access
        visa_free = prog_data.get('visa_free_countries', 0)
        if visa_free > max_visa_free:
            max_visa_free = visa_free
            comparison["best_for"]["best_visa_free_access"] = f"{country} - {program_name} ({visa_free} countries)"
        
        # Family eligibility
        comparison["family_eligibility"].append({
            "country": country,
            "program": program_name,
            "eligible": prog_data.get('family_members_eligible', False)
        })
        
        # Citizenship paths
        comparison["citizenship_paths"].append({
            "country": country,
            "program": program_name,
            "path": prog_data.get('path_to_citizenship', 'No citizenship path')
        })
        
        # Cost comparison
        if 'cost' in prog_data:
            comparison["cost_comparison"].append({
                "country": country,
                "program": program_name,
                "costs": prog_data.get('cost', {})
            })
    
    return comparison


def get_program_ranking(criteria="visa_free"):
    """
    Rank programs based on different criteria
    criteria: 'visa_free', 'investment', 'processing_time', 'benefits'
    """
    ranked = []
    
    for country, programs in residency_programs.items():
        for prog_name, prog_data in programs.items():
            if criteria == "visa_free":
                score = prog_data.get('visa_free_countries', 0)
                ranked.append({
                    "country": country,
                    "program": prog_name,
                    "score": score,
                    "metric": f"{score} visa-free countries"
                })
            
            elif criteria == "investment" and 'investment_types' in prog_data:
                min_investment = float('inf')
                for inv_type, inv_data in prog_data['investment_types'].items():
                    min_str = inv_data['minimum'].replace('€', '').replace('£', '').replace('CAD $', '').replace('AUD $', '').replace('AED', '').replace('SGD $', '').replace('/year', '').replace(',', '').strip()
                    try:
                        amount = float(min_str)
                        if amount < min_investment:
                            min_investment = amount
                    except:
                        pass
                
                if min_investment != float('inf'):
                    ranked.append({
                        "country": country,
                        "program": prog_name,
                        "score": min_investment,
                        "metric": f"€{min_investment:,.0f} minimum",
                        "lower_is_better": True
                    })
            
            elif criteria == "benefits" and 'benefits' in prog_data:
                score = len(prog_data.get('benefits', []))
                ranked.append({
                    "country": country,
                    "program": prog_name,
                    "score": score,
                    "metric": f"{score} benefits"
                })
    
    # Sort by score
    if criteria in ["investment"]:
        ranked.sort(key=lambda x: x.get('score', float('inf')))
    else:
        ranked.sort(key=lambda x: x.get('score', 0), reverse=True)
    
    return ranked[:10]  # Top 10


def get_program_insights(country):
    """Get insights and statistics for a specific country"""
    if country not in residency_programs:
        return None
    
    programs = residency_programs[country]
    insights = {
        "country": country,
        "total_programs": len(programs),
        "program_types": [],
        "average_processing_time": "N/A",
        "programs_with_citizenship": 0,
        "family_friendly_count": 0,
        "popular_programs": [],
        "minimum_investments": [],
        "country_highlights": []
    }
    
    citizenship_count = 0
    family_count = 0
    program_types = {}
    
    for prog_name, prog_data in programs.items():
        # Count program types
        prog_type = prog_data.get('residency_type', 'Other')
        if prog_type not in program_types:
            program_types[prog_type] = 0
        program_types[prog_type] += 1
        
        # Count citizenship paths
        if prog_data.get('path_to_citizenship') and prog_data.get('path_to_citizenship').lower() != 'no citizenship path':
            citizenship_count += 1
        
        # Count family friendly
        if prog_data.get('family_members_eligible'):
            family_count += 1
        
        # Popular programs
        if prog_data.get('popular'):
            insights["popular_programs"].append(prog_name)
        
        # Get minimum investments
        if 'investment_types' in prog_data:
            for inv_type, inv_data in prog_data['investment_types'].items():
                insights["minimum_investments"].append({
                    "program": prog_name,
                    "type": inv_type,
                    "amount": inv_data.get('minimum')
                })
    
    insights["program_types"] = [{"type": k, "count": v} for k, v in program_types.items()]
    insights["programs_with_citizenship"] = citizenship_count
    insights["family_friendly_count"] = family_count
    insights["minimum_investments"].sort(key=lambda x: x.get('amount', '€0'))
    
    # Country highlights
    country_info = {}
    if programs:
        first_prog = list(programs.values())[0]
        if 'country_info' in first_prog:
            country_info = first_prog['country_info']
    
    if country_info:
        insights["country_highlights"] = [
            f"Capital: {country_info.get('capital', 'N/A')}",
            f"Region: {country_info.get('region', 'N/A')}",
            f"Languages: {country_info.get('language', 'N/A')}",
            f"EU Member: {'Yes' if country_info.get('eu_member') else 'No'}",
            f"Schengen Member: {'Yes' if country_info.get('schengen_member') else 'No'}",
            f"Cost of Living: {country_info.get('cost_of_living', 'N/A')}"
        ]
    
    return insights


if __name__ == "__main__":
    # Test analytics
    analytics = get_program_analytics()
    print(f"Total Programs: {analytics['total_programs']}")
    print(f"Total Countries: {analytics['total_countries']}")
    print(f"Programs with Citizenship: {analytics['programs_with_citizenship']}")
