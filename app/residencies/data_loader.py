"""
Data loader utility to populate ResidencyProgram models from investment_data.py
Also provides CLI commands for database seeding
"""
import json
import os
from typing import Dict, Any, List
from app import create_app
from models import db
from app.residencies.models import ResidencyProgram, ResidencyApplication
from investment_data import investment_programs


# Country to ISO 3166-1 alpha-2 code mapping for flags
COUNTRY_FLAG_CODES = {
    'United States': 'US',
    'United Kingdom': 'GB',
    'Canada': 'CA',
    'Australia': 'AU',
    'Singapore': 'SG',
    'United Arab Emirates': 'AE',
    'Switzerland': 'CH',
    'Portugal': 'PT',
    'Germany': 'DE',
    'France': 'FR',
    'Netherlands': 'NL',
    'Spain': 'ES',
    'Italy': 'IT',
    'Ireland': 'IE',
    'New Zealand': 'NZ',
    'Japan': 'JP',
    'South Korea': 'KR',
    'Hong Kong': 'HK',
    'Thailand': 'TH',
    'Philippines': 'PH',
    'Malaysia': 'MY',
    'Vietnam': 'VN',
    'Turkey': 'TR',
    'Greece': 'GR',
    'Malta': 'MT',
    'Cyprus': 'CY',
}

# Program type inference from program names
PROGRAM_TYPE_KEYWORDS = {
    'investor': ['investor', 'investment', 'visa', 'entrepreneur', 'startup', 'founder'],
    'employment': ['work', 'skilled', 'professional', 'employee', 'employment'],
    'student': ['student', 'study', 'graduate', 'education'],
    'retired': ['retirement', 'retired', 'pensioner', 'retiree', 'passive income'],
    'family': ['family', 'spouse', 'dependent', 'reunion'],
    'citizenship': ['citizenship', 'naturalization'],
}


class ResidencyDataLoader:
    """Load residency program data from investment_data.py into database"""
    
    @staticmethod
    def infer_program_type(program_name: str, program_info: Dict) -> str:
        """Infer program type from program name and details"""
        name_lower = program_name.lower()
        
        for program_type, keywords in PROGRAM_TYPE_KEYWORDS.items():
            if any(keyword in name_lower for keyword in keywords):
                return program_type
        
        # Default based on content
        if 'investment' in str(program_info).lower():
            return 'investor'
        
        return 'other'
    
    @staticmethod
    def parse_investment_amount(investment_str: str) -> tuple:
        """
        Parse investment string like '$500,000 - $1,000,000' or '€50,000 minimum'
        Returns: (min_amount, max_amount, currency)
        """
        import re
        
        if not investment_str or investment_str == 'N/A':
            return None, None, 'USD'
        
        # Extract currency
        currency = 'USD'
        if '€' in investment_str:
            currency = 'EUR'
        elif '£' in investment_str:
            currency = 'GBP'
        elif 'CAD' in investment_str:
            currency = 'CAD'
        elif 'AUD' in investment_str:
            currency = 'AUD'
        elif 'SGD' in investment_str:
            currency = 'SGD'
        elif 'AED' in investment_str:
            currency = 'AED'
        elif 'CHF' in investment_str:
            currency = 'CHF'
        
        # Extract numbers
        numbers = re.findall(r'[\d,]+', investment_str)
        
        if len(numbers) >= 2:
            min_amount = float(numbers[0].replace(',', ''))
            max_amount = float(numbers[1].replace(',', ''))
            return min_amount, max_amount, currency
        elif len(numbers) == 1:
            amount = float(numbers[0].replace(',', ''))
            return amount, None, currency
        
        return None, None, currency
    
    @staticmethod
    def parse_processing_time(time_str: str) -> int:
        """
        Parse processing time string like '18-36 months' or '8 weeks'
        Returns: months (approximate)
        """
        import re
        
        if not time_str:
            return None
        
        # Extract numbers
        numbers = re.findall(r'\d+', time_str)
        
        if 'month' in time_str.lower():
            if len(numbers) >= 2:
                # Average of range
                return int((int(numbers[0]) + int(numbers[1])) / 2)
            elif len(numbers) == 1:
                return int(numbers[0])
        
        elif 'week' in time_str.lower():
            if len(numbers) >= 2:
                weeks = (int(numbers[0]) + int(numbers[1])) / 2
            else:
                weeks = int(numbers[0]) if numbers else 4
            
            return int(weeks / 4.3)  # Convert weeks to months
        
        elif 'year' in time_str.lower():
            if len(numbers) >= 1:
                return int(numbers[0]) * 12
        
        return None
    
    @classmethod
    def load_from_investment_data(cls, app=None):
        """
        Load all programs from investment_data.py into database
        """
        if app is None:
            app = create_app()
        
        with app.app_context():
            # Clear existing programs
            ResidencyProgram.query.delete()
            db.session.commit()
            
            programs_created = 0
            
            for country, programs_dict in investment_programs.items():
                for program_name, program_info in programs_dict.items():
                    try:
                        # Parse investment amount
                        min_amount, max_amount, currency = cls.parse_investment_amount(
                            program_info.get('Investment Required', 'N/A')
                        )
                        
                        # Parse processing time
                        processing_months = cls.parse_processing_time(
                            program_info.get('Processing Time')
                        )
                        
                        # Get flag code
                        flag_code = COUNTRY_FLAG_CODES.get(country)
                        
                        # Infer program type
                        program_type = cls.infer_program_type(program_name, program_info)
                        
                        # Extract documents (if available)
                        documents = program_info.get('Documents', [])
                        
                        # Create program
                        program = ResidencyProgram(
                            country=country,
                            program_name=program_name,
                            description=None,
                            investment_required=program_info.get('Investment Required'),
                            investment_currency=currency,
                            investment_min_amount=min_amount,
                            investment_max_amount=max_amount,
                            processing_time=program_info.get('Processing Time'),
                            processing_time_months=processing_months,
                            family_size_limit=None,  # Not in original data
                            net_worth_required=None,  # Can be enhanced
                            program_type=program_type,
                            interview_required=program_info.get('Interview Requirement', 'No').lower() == 'yes',
                            country_flag_code=flag_code,
                            documents_required=documents if documents else None,
                            benefits=program_info.get('Benefits'),
                            embassy_locations=program_info.get('Embassy Locations'),
                        )
                        
                        db.session.add(program)
                        programs_created += 1
                    
                    except Exception as e:
                        print(f"Error loading {country}/{program_name}: {str(e)}")
                        continue
            
            db.session.commit()
            return programs_created
    
    @classmethod
    def load_from_json_file(cls, json_file_path: str, app=None):
        """
        Load programs from a JSON file
        
        Expected format:
        {
            "Country": {
                "Program Name": {
                    "investment_required": "...",
                    "processing_time": "...",
                    ...
                }
            }
        }
        """
        if app is None:
            app = create_app()
        
        with app.app_context():
            try:
                with open(json_file_path, 'r') as f:
                    data = json.load(f)
                
                # Clear existing programs
                ResidencyProgram.query.delete()
                db.session.commit()
                
                programs_created = 0
                
                for country, programs_dict in data.items():
                    for program_name, program_info in programs_dict.items():
                        try:
                            # Get values with defaults
                            investment_str = program_info.get('investment_required', 'N/A')
                            min_amount, max_amount, currency = cls.parse_investment_amount(investment_str)
                            
                            processing_months = cls.parse_processing_time(
                                program_info.get('processing_time')
                            )
                            
                            flag_code = COUNTRY_FLAG_CODES.get(country)
                            program_type = program_info.get('program_type', 'other')
                            
                            program = ResidencyProgram(
                                country=country,
                                program_name=program_name,
                                description=program_info.get('description'),
                                investment_required=investment_str,
                                investment_currency=currency,
                                investment_min_amount=min_amount,
                                investment_max_amount=max_amount,
                                processing_time=program_info.get('processing_time'),
                                processing_time_months=processing_months,
                                family_size_limit=program_info.get('family_size_limit'),
                                net_worth_required=program_info.get('net_worth_required'),
                                program_type=program_type,
                                interview_required=program_info.get('interview_required', False),
                                country_flag_code=flag_code,
                                documents_required=program_info.get('documents_required'),
                                benefits=program_info.get('benefits'),
                                embassy_locations=program_info.get('embassy_locations'),
                            )
                            
                            db.session.add(program)
                            programs_created += 1
                        
                        except Exception as e:
                            print(f"Error loading {country}/{program_name}: {str(e)}")
                            continue
                
                db.session.commit()
                return programs_created
            
            except FileNotFoundError:
                print(f"JSON file not found: {json_file_path}")
                return 0
            except json.JSONDecodeError:
                print(f"Invalid JSON file: {json_file_path}")
                return 0
    
    @classmethod
    def export_to_json(cls, output_path: str, app=None):
        """Export all programs to JSON file"""
        if app is None:
            app = create_app()
        
        with app.app_context():
            programs = ResidencyProgram.query.all()
            
            data = {}
            for program in programs:
                if program.country not in data:
                    data[program.country] = {}
                
                data[program.country][program.program_name] = program.to_dict()
            
            with open(output_path, 'w') as f:
                json.dump(data, f, indent=2, default=str)
            
            return len(programs)


# CLI Commands for Flask
def register_data_loader_commands(app):
    """Register CLI commands for data loading"""
    
    @app.cli.command('load-residency-data')
    def load_residency_data():
        """Load residency program data from investment_data.py"""
        count = ResidencyDataLoader.load_from_investment_data(app)
        print(f"✓ Loaded {count} residency programs")
    
    @app.cli.command('export-residency-data')
    def export_residency_data():
        """Export all residency programs to JSON"""
        output = 'residency_programs_export.json'
        count = ResidencyDataLoader.export_to_json(output, app)
        print(f"✓ Exported {count} programs to {output}")
