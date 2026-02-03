"""
Routes for residencies blueprint
API endpoints and views for residency programs
"""
from flask import jsonify, render_template, request, current_app
from functools import wraps
import json
from app.residencies import residencies
from app.residencies.models import ResidencyProgram, ResidencyApplication
from app.residencies.schemas import EligibilityCheckRequest, CurrencyConversionRequest
from app.residencies.eligibility import eligibility_checker
from models import db
from flask_login import current_user, login_required


def api_error(message: str, status_code: int = 400):
    """Helper to return consistent API error responses"""
    return jsonify({'status': 'error', 'message': message}), status_code


def api_success(data, status_code: int = 200):
    """Helper to return consistent API success responses"""
    return jsonify({'status': 'success', 'data': data}), status_code


# ============================================================================
# API ENDPOINTS
# ============================================================================

@residencies.route('/api/eligibility', methods=['POST'])
def check_eligibility():
    """
    Check eligibility for residency programs
    
    POST /residencies/api/eligibility
    Content-Type: application/json
    {
        "investment_budget": 500000,
        "net_worth": 2000000,
        "family_size": 4,
        "age": 35,
        "country_preference": "United Kingdom",
        "program_type_preference": "investor"
    }
    
    Returns: EligibilityCheckResponse with top 5 matching programs
    """
    try:
        data = request.get_json()
        if not data:
            return api_error("No JSON data provided", 400)
        
        # Validate request
        eligibility_request = EligibilityCheckRequest(**data)
        
        # Check eligibility
        response = eligibility_checker.check_eligibility(eligibility_request)
        
        return jsonify(response.model_dump()), 200
    
    except ValueError as e:
        return api_error(f"Validation error: {str(e)}", 400)
    except Exception as e:
        current_app.logger.error(f"Eligibility check error: {str(e)}")
        return api_error("Internal server error", 500)


@residencies.route('/api/programs', methods=['GET'])
def list_programs():
    """
    List all available residency programs with filters
    
    GET /residencies/api/programs?country=USA&program_type=investor&min_investment=50000
    """
    try:
        country = request.args.get('country')
        program_type = request.args.get('program_type')
        min_investment = request.args.get('min_investment', type=float)
        max_investment = request.args.get('max_investment', type=float)
        
        query = ResidencyProgram.query
        
        if country:
            query = query.filter_by(country=country)
        if program_type:
            query = query.filter_by(program_type=program_type)
        if min_investment:
            query = query.filter(ResidencyProgram.investment_min_amount >= min_investment)
        if max_investment:
            query = query.filter(ResidencyProgram.investment_max_amount <= max_investment)
        
        programs = query.all()
        return jsonify({
            'status': 'success',
            'count': len(programs),
            'data': [p.to_dict() for p in programs]
        }), 200
    
    except Exception as e:
        current_app.logger.error(f"List programs error: {str(e)}")
        return api_error("Internal server error", 500)


@residencies.route('/api/programs/<int:program_id>', methods=['GET'])
def get_program(program_id):
    """Get detailed information about a specific program"""
    try:
        program = ResidencyProgram.query.get(program_id)
        if not program:
            return api_error("Program not found", 404)
        
        return jsonify({
            'status': 'success',
            'data': program.to_dict()
        }), 200
    
    except Exception as e:
        current_app.logger.error(f"Get program error: {str(e)}")
        return api_error("Internal server error", 500)


@residencies.route('/api/programs/by-country/<country>', methods=['GET'])
def get_programs_by_country(country):
    """Get all programs for a specific country"""
    try:
        programs = ResidencyProgram.query.filter_by(country=country).all()
        
        return jsonify({
            'status': 'success',
            'country': country,
            'count': len(programs),
            'data': [p.to_dict() for p in programs]
        }), 200
    
    except Exception as e:
        current_app.logger.error(f"Get programs by country error: {str(e)}")
        return api_error("Internal server error", 500)


@residencies.route('/api/currencies/convert', methods=['POST'])
def convert_currency():
    """
    Convert amount between currencies
    
    POST /residencies/api/currencies/convert
    {
        "amount": 100000,
        "from_currency": "USD",
        "to_currency": "EUR"
    }
    """
    try:
        data = request.get_json()
        if not data:
            return api_error("No JSON data provided", 400)
        
        conv_request = CurrencyConversionRequest(**data)
        
        converted_amount = eligibility_checker._convert_currency(
            conv_request.amount,
            conv_request.from_currency,
            conv_request.to_currency
        )
        
        exchange_rate = eligibility_checker.get_currency_rate(
            conv_request.from_currency,
            conv_request.to_currency
        )
        
        return jsonify({
            'status': 'success',
            'data': {
                'original_amount': conv_request.amount,
                'from_currency': conv_request.from_currency,
                'to_currency': conv_request.to_currency,
                'converted_amount': converted_amount,
                'exchange_rate': exchange_rate,
                'timestamp': json.dumps(__import__('datetime').datetime.utcnow(), default=str)
            }
        }), 200
    
    except ValueError as e:
        return api_error(f"Validation error: {str(e)}", 400)
    except Exception as e:
        current_app.logger.error(f"Currency conversion error: {str(e)}")
        return api_error("Internal server error", 500)


@residencies.route('/api/currencies/rates', methods=['GET'])
def get_currency_rates():
    """Get all available currency conversion rates"""
    try:
        base_currency = request.args.get('base', 'USD')
        
        rates = {}
        for currency in eligibility_checker.currency_rates.keys():
            if currency != base_currency:
                rates[currency] = eligibility_checker.get_currency_rate(base_currency, currency)
        
        return jsonify({
            'status': 'success',
            'base': base_currency,
            'rates': rates,
            'timestamp': __import__('datetime').datetime.utcnow().isoformat() + 'Z'
        }), 200
    
    except Exception as e:
        current_app.logger.error(f"Get rates error: {str(e)}")
        return api_error("Internal server error", 500)


@residencies.route('/api/countries', methods=['GET'])
def get_countries():
    """Get list of all countries with programs"""
    try:
        countries = db.session.query(ResidencyProgram.country).distinct().all()
        country_list = sorted([c[0] for c in countries])
        
        return jsonify({
            'status': 'success',
            'count': len(country_list),
            'data': country_list
        }), 200
    
    except Exception as e:
        current_app.logger.error(f"Get countries error: {str(e)}")
        return api_error("Internal server error", 500)


# ============================================================================
# HTML VIEWS
# ============================================================================

@residencies.route('/programs')
def programs_list():
    """Display all residency programs"""
    try:
        page = request.args.get('page', 1, type=int)
        country_filter = request.args.get('country')
        program_type_filter = request.args.get('type')
        
        query = ResidencyProgram.query
        
        if country_filter:
            query = query.filter_by(country=country_filter)
        if program_type_filter:
            query = query.filter_by(program_type=program_type_filter)
        
        # Paginate: 12 per page
        paginated = query.paginate(page=page, per_page=12)
        
        countries = db.session.query(ResidencyProgram.country).distinct().all()
        country_list = sorted([c[0] for c in countries])
        
        return render_template('residencies/programs_list.html',
                             programs=paginated.items,
                             pagination=paginated,
                             countries=country_list,
                             selected_country=country_filter,
                             selected_type=program_type_filter)
    
    except Exception as e:
        current_app.logger.error(f"Programs list error: {str(e)}")
        return render_template('error.html', message="Failed to load programs"), 500


@residencies.route('/programs/<int:program_id>')
def program_detail(program_id):
    """Display detailed view of a specific program"""
    try:
        program = ResidencyProgram.query.get(program_id)
        if not program:
            return render_template('error.html', message="Program not found"), 404
        
        # Get similar programs from same country
        similar = ResidencyProgram.query.filter(
            ResidencyProgram.country == program.country,
            ResidencyProgram.id != program.id
        ).limit(3).all()
        
        return render_template('residencies/program_detail.html',
                             program=program,
                             similar_programs=similar)
    
    except Exception as e:
        current_app.logger.error(f"Program detail error: {str(e)}")
        return render_template('error.html', message="Failed to load program"), 500


@residencies.route('/eligibility-checker')
def eligibility_checker_view():
    """Display interactive eligibility checker"""
    return render_template('residencies/eligibility_checker.html')


@residencies.route('/compare')
def compare_programs():
    """Compare multiple programs side-by-side"""
    try:
        program_ids = request.args.getlist('programs', type=int)
        
        if not program_ids:
            return render_template('residencies/compare.html', programs=[])
        
        programs = ResidencyProgram.query.filter(
            ResidencyProgram.id.in_(program_ids)
        ).all()
        
        return render_template('residencies/compare.html', programs=programs)
    
    except Exception as e:
        current_app.logger.error(f"Compare programs error: {str(e)}")
        return render_template('error.html', message="Failed to compare programs"), 500
