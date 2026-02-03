"""
Pydantic schemas for residency programs and eligibility checking
"""
from typing import Optional, List
from pydantic import BaseModel, Field, validator
from enum import Enum


class ProgramTypeEnum(str, Enum):
    """Types of residency programs"""
    investor = "investor"
    employment = "employment"
    startup = "startup"
    student = "student"
    retired = "retired"
    family = "family"
    citizenship = "citizenship"


class EligibilityCheckRequest(BaseModel):
    """Input model for eligibility checking"""
    investment_budget: float = Field(..., gt=0, description="Available investment amount in USD")
    net_worth: float = Field(..., ge=0, description="Total net worth in USD")
    family_size: int = Field(default=1, ge=1, le=20, description="Number of family members")
    age: Optional[int] = Field(default=None, ge=18, le=120, description="Applicant age")
    country_preference: Optional[str] = Field(default=None, description="Preferred destination country")
    program_type_preference: Optional[ProgramTypeEnum] = Field(default=None, description="Preferred program type")
    
    @validator('investment_budget')
    def validate_investment(cls, v):
        if v <= 0:
            raise ValueError('Investment budget must be greater than 0')
        return v


class ResidencyProgramSchema(BaseModel):
    """Pydantic schema for ResidencyProgram model"""
    id: int
    country: str
    program_name: str
    description: Optional[str] = None
    investment_required: Optional[str] = None
    investment_currency: str = "USD"
    investment_min_amount: Optional[float] = None
    investment_max_amount: Optional[float] = None
    processing_time: Optional[str] = None
    processing_time_months: Optional[int] = None
    documents_required: Optional[List[str]] = None
    family_size_limit: Optional[int] = None
    age_requirement: Optional[str] = None
    net_worth_required: Optional[float] = None
    benefits: Optional[str] = None
    interview_required: bool = False
    embassy_locations: Optional[List[str]] = None
    program_type: Optional[str] = None
    country_flag_code: Optional[str] = None
    
    class ConfigDict:
        from_attributes = True


class EligibilityCheckResponse(BaseModel):
    """Response model for eligibility check"""
    request_id: str
    status: str = "success"
    timestamp: str
    matching_programs: List[ResidencyProgramSchema] = Field(..., max_items=10)
    eligibility_score: float = Field(..., ge=0, le=100, description="Overall match score 0-100")
    message: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "request_id": "req_12345",
                "status": "success",
                "timestamp": "2024-02-03T10:30:00Z",
                "matching_programs": [],
                "eligibility_score": 85.5,
                "message": "Found 5 matching programs based on your criteria"
            }
        }


class EligibilityMatchDetail(BaseModel):
    """Detailed eligibility match information"""
    program_id: int
    program_name: str
    country: str
    match_score: float = Field(..., ge=0, le=100)
    investment_fit: bool
    family_fit: bool
    net_worth_fit: bool
    matching_factors: List[str] = Field(default=[], description="Why this program matches")
    potential_issues: List[str] = Field(default=[], description="Potential disqualifications")


class CurrencyConversionRequest(BaseModel):
    """Input for currency conversion"""
    amount: float = Field(..., gt=0)
    from_currency: str = Field(default="USD")
    to_currency: str = Field(default="EUR")


class CurrencyConversionResponse(BaseModel):
    """Response for currency conversion"""
    original_amount: float
    from_currency: str
    to_currency: str
    converted_amount: float
    exchange_rate: float
    timestamp: str
