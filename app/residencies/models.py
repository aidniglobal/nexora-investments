"""
SQLAlchemy models for residency/visa programs
"""
from typing import Optional, List, Dict, Any
from datetime import datetime, timezone
from models import db


class ResidencyProgram(db.Model):
    """
    Represents a residency/visa program offered by a country.
    Loaded from investment_data.json or manually created.
    """
    __tablename__ = 'residency_program'

    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(100), nullable=False, index=True)
    program_name = db.Column(db.String(200), nullable=False, unique=True, index=True)
    description = db.Column(db.Text, nullable=True)
    
    # Investment Requirements
    investment_required = db.Column(db.String(100), nullable=True)
    investment_currency = db.Column(db.String(10), default='USD', nullable=False)
    investment_min_amount = db.Column(db.Float, nullable=True)  # Min in base currency
    investment_max_amount = db.Column(db.Float, nullable=True)  # Max in base currency
    
    # Processing Info
    processing_time = db.Column(db.String(100), nullable=True)
    processing_time_months = db.Column(db.Integer, nullable=True)  # Standardized in months
    
    # Requirements
    documents_required = db.Column(db.JSON, nullable=True)  # List of required documents
    family_size_limit = db.Column(db.Integer, nullable=True)  # Max family members allowed
    age_requirement = db.Column(db.String(100), nullable=True)  # e.g., "18+", "No restriction"
    net_worth_required = db.Column(db.Float, nullable=True)  # Net worth in USD equivalent
    
    # Program Details
    benefits = db.Column(db.Text, nullable=True)
    interview_required = db.Column(db.Boolean, default=False)
    embassy_locations = db.Column(db.JSON, nullable=True)  # List of embassy locations
    program_type = db.Column(db.String(50), nullable=True)  # e.g., "investor", "employment", "startup"
    
    # Metadata
    country_flag_code = db.Column(db.String(2), nullable=True)  # ISO 3166-1 alpha-2 code for flag
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), 
                          onupdate=lambda: datetime.now(timezone.utc))
    
    def __repr__(self):
        return f'<ResidencyProgram {self.program_name} - {self.country}>'
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert model to dictionary for API responses"""
        return {
            'id': self.id,
            'country': self.country,
            'program_name': self.program_name,
            'description': self.description,
            'investment_required': self.investment_required,
            'investment_currency': self.investment_currency,
            'investment_min_amount': self.investment_min_amount,
            'investment_max_amount': self.investment_max_amount,
            'processing_time': self.processing_time,
            'processing_time_months': self.processing_time_months,
            'documents_required': self.documents_required,
            'family_size_limit': self.family_size_limit,
            'age_requirement': self.age_requirement,
            'net_worth_required': self.net_worth_required,
            'benefits': self.benefits,
            'interview_required': self.interview_required,
            'embassy_locations': self.embassy_locations,
            'program_type': self.program_type,
            'country_flag_code': self.country_flag_code,
        }


class ResidencyApplication(db.Model):
    """
    Represents a user's application to a residency program
    """
    __tablename__ = 'residency_application'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    program_id = db.Column(db.Integer, db.ForeignKey('residency_program.id'), nullable=False)
    
    # Applicant Info
    full_name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    
    # Application Details
    investment_amount = db.Column(db.Float, nullable=True)
    investment_currency = db.Column(db.String(10), default='USD')
    family_size = db.Column(db.Integer, default=1)
    net_worth = db.Column(db.Float, nullable=True)
    
    # Status
    status = db.Column(db.String(50), default='pending')  # pending, approved, rejected, in_review
    notes = db.Column(db.Text, nullable=True)
    
    # Timestamps
    submitted_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc),
                          onupdate=lambda: datetime.now(timezone.utc))
    
    # Relationships
    user = db.relationship('User', backref=db.backref('residency_applications', lazy=True))
    program = db.relationship('ResidencyProgram', backref=db.backref('applications', lazy=True))
    
    def __repr__(self):
        return f'<ResidencyApplication {self.full_name} - {self.program.program_name}>'
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'user_id': self.user_id,
            'program_id': self.program_id,
            'program_name': self.program.program_name if self.program else None,
            'country': self.program.country if self.program else None,
            'full_name': self.full_name,
            'email': self.email,
            'investment_amount': self.investment_amount,
            'family_size': self.family_size,
            'net_worth': self.net_worth,
            'status': self.status,
            'submitted_at': self.submitted_at.isoformat() if self.submitted_at else None,
        }
