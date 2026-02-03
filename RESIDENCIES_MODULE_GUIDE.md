# Nexora Residencies Module - Implementation Guide

## Overview

The Residencies module is a comprehensive refactor of the investment/visa program management system in Nexora Investments. It transforms a monolithic structure into a modular, API-first blueprint-based architecture with intelligent eligibility matching.

## Architecture

### Module Structure

```
app/residencies/
├── __init__.py              # Blueprint initialization
├── models.py                # SQLAlchemy models (ResidencyProgram, ResidencyApplication)
├── schemas.py               # Pydantic validation schemas
├── eligibility.py           # Eligibility checking service
├── routes.py                # API endpoints and HTML views
├── data_loader.py           # Data import/export utilities
└── templates/               # Residency-specific templates
    ├── programs_list.html   # Browse all programs
    ├── program_detail.html  # Program details with currency converter
    ├── eligibility_checker.html  # Interactive eligibility checker
    └── compare.html         # Side-by-side program comparison
```

## Key Features

### 1. **SQLAlchemy Models**

#### ResidencyProgram
Represents a residency/visa program offered by a country.

**Key Fields:**
- `country` - Destination country
- `program_name` - Unique program identifier
- `investment_required` - Human-readable investment requirement
- `investment_currency` - Currency code (USD, EUR, GBP, etc.)
- `investment_min_amount` - Minimum amount in base currency
- `investment_max_amount` - Maximum amount
- `processing_time_months` - Processing time in months (standardized)
- `family_size_limit` - Max family members eligible
- `net_worth_required` - Minimum net worth in USD
- `program_type` - Category (investor, employment, startup, etc.)
- `country_flag_code` - ISO 3166-1 alpha-2 code for flag display

```python
program = ResidencyProgram.query.filter_by(
    country='United Kingdom',
    program_type='startup'
).first()
```

#### ResidencyApplication
Represents a user's application to a specific program.

**Key Fields:**
- `user_id` - Link to authenticated user
- `program_id` - Link to program
- `investment_amount` - Applicant's investment amount
- `family_size` - Applicant's family count
- `net_worth` - Applicant's net worth
- `status` - Application state (pending, approved, rejected, in_review)

### 2. **Pydantic Validation Schemas**

#### EligibilityCheckRequest
Validates applicant criteria:
```python
{
    "investment_budget": 500000,      # Required, > 0
    "net_worth": 2000000,             # Required, >= 0
    "family_size": 4,                 # Optional, 1-20
    "age": 35,                        # Optional, 18-120
    "country_preference": "United Kingdom",  # Optional
    "program_type_preference": "investor"    # Optional
}
```

#### EligibilityCheckResponse
Returns matching programs and eligibility score:
```python
{
    "request_id": "req_abc123",
    "status": "success",
    "timestamp": "2024-02-03T10:30:00Z",
    "matching_programs": [...],  # Max 5 programs
    "eligibility_score": 85.5,   # 0-100
    "message": "Found 3 matching programs..."
}
```

### 3. **Eligibility Checker Service**

The `EligibilityChecker` class provides intelligent matching based on:

**Scoring Breakdown:**
- **Investment Fit (40%):** Does budget meet program requirements?
- **Family Size Fit (30%):** Is family size within limits?
- **Net Worth Fit (20%):** Does net worth meet requirements?
- **Program Type Match (10%):** Does preferred type match?

**Currency Support:**
- USD, EUR, GBP, CAD, AUD, SGD, AED, CHF
- Real-time conversion between currencies
- All calculations standardized to USD internally

**Example Usage:**
```python
from app.residencies.eligibility import eligibility_checker
from app.residencies.schemas import EligibilityCheckRequest

request = EligibilityCheckRequest(
    investment_budget=600000,
    net_worth=1500000,
    family_size=3,
    country_preference="United States"
)

response = eligibility_checker.check_eligibility(request)
# Returns: EligibilityCheckResponse with top 5 matching programs
```

## API Endpoints

### POST /residencies/api/eligibility
Check eligibility for residency programs

**Request:**
```bash
curl -X POST http://localhost:5000/residencies/api/eligibility \
  -H "Content-Type: application/json" \
  -d '{
    "investment_budget": 500000,
    "net_worth": 1000000,
    "family_size": 2,
    "country_preference": "Canada"
  }'
```

**Response:** `EligibilityCheckResponse`

### GET /residencies/api/programs
List all programs with optional filters

**Query Parameters:**
- `country` - Filter by country
- `program_type` - Filter by type (investor, employment, etc.)
- `min_investment` - Minimum investment amount
- `max_investment` - Maximum investment amount

**Example:**
```bash
curl "http://localhost:5000/residencies/api/programs?country=USA&program_type=investor"
```

### GET /residencies/api/programs/<id>
Get detailed information about a specific program

### GET /residencies/api/programs/by-country/<country>
Get all programs for a specific country

### GET /residencies/api/countries
Get list of all countries with programs

### POST /residencies/api/currencies/convert
Convert between currencies

**Request:**
```json
{
    "amount": 100000,
    "from_currency": "USD",
    "to_currency": "EUR"
}
```

**Response:**
```json
{
    "status": "success",
    "data": {
        "original_amount": 100000,
        "from_currency": "USD",
        "to_currency": "EUR",
        "converted_amount": 92000,
        "exchange_rate": 0.92
    }
}
```

### GET /residencies/api/currencies/rates
Get exchange rates for all supported currencies

**Query Parameters:**
- `base` - Base currency (default: USD)

## HTML Views

### /residencies/programs
Browse all residency programs with pagination

- **Features:**
  - Filter by country and program type
  - Responsive grid layout (12 programs per page)
  - Country flags from CDN (flag-icons-css)
  - Program type badges
  - Investment and processing time displayed

### /residencies/programs/<id>
Detailed program information

- **Features:**
  - Full program description
  - Investment details with currency converter modal
  - Documents required list
  - Embassy locations
  - Family size and age requirements
  - Similar programs from same country
  - "Check Eligibility" CTA button

### /residencies/eligibility-checker
Interactive eligibility form

- **Features:**
  - Real-time form validation
  - Dropdown population from API
  - Animated eligibility score
  - Top 5 matching programs
  - Responsive design (mobile-first)
  - Loading state with spinner

### /residencies/compare
Side-by-side program comparison

- **Features:**
  - Multi-program comparison table
  - Key metrics visualization
  - Action buttons for each program
  - Comparison tips and next steps

## Data Import

### From Investment Data Dictionary
```python
from app.residencies.data_loader import ResidencyDataLoader

# Load all programs from investment_data.py
ResidencyDataLoader.load_from_investment_data(app)
```

### From JSON File
```python
ResidencyDataLoader.load_from_json_file('programs.json', app)
```

### CLI Commands
```bash
# Load from investment_data.py
flask load-residency-data

# Export to JSON
flask export-residency-data
```

## Database Schema

### residency_program Table
```sql
CREATE TABLE residency_program (
    id INTEGER PRIMARY KEY,
    country VARCHAR(100) NOT NULL,
    program_name VARCHAR(200) UNIQUE NOT NULL,
    description TEXT,
    investment_required VARCHAR(100),
    investment_currency VARCHAR(10) DEFAULT 'USD',
    investment_min_amount FLOAT,
    investment_max_amount FLOAT,
    processing_time VARCHAR(100),
    processing_time_months INTEGER,
    documents_required JSON,
    family_size_limit INTEGER,
    age_requirement VARCHAR(100),
    net_worth_required FLOAT,
    benefits TEXT,
    interview_required BOOLEAN DEFAULT FALSE,
    embassy_locations JSON,
    program_type VARCHAR(50),
    country_flag_code VARCHAR(2),
    created_at DATETIME,
    updated_at DATETIME,
    INDEX (country),
    INDEX (program_name),
    UNIQUE (program_name)
);
```

### residency_application Table
```sql
CREATE TABLE residency_application (
    id INTEGER PRIMARY KEY,
    user_id INTEGER FOREIGN KEY,
    program_id INTEGER FOREIGN KEY,
    full_name VARCHAR(150) NOT NULL,
    email VARCHAR(120) NOT NULL,
    phone VARCHAR(20),
    investment_amount FLOAT,
    investment_currency VARCHAR(10) DEFAULT 'USD',
    family_size INTEGER DEFAULT 1,
    net_worth FLOAT,
    status VARCHAR(50) DEFAULT 'pending',
    notes TEXT,
    submitted_at DATETIME,
    updated_at DATETIME,
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (program_id) REFERENCES residency_program(id)
);
```

## Testing

Comprehensive pytest suite with 40+ test cases:

```bash
# Run all residencies tests
pytest tests/test_residencies_eligibility.py -v

# Run specific test class
pytest tests/test_residencies_eligibility.py::TestEligibilityChecker -v

# Run with coverage
pytest tests/test_residencies_eligibility.py --cov=app.residencies
```

### Test Coverage
- **EligibilityChecker:** Investment, family, net worth, program type matching
- **Currency Conversion:** Multi-currency support, exchange rates
- **API Endpoints:** Validation, filtering, pagination
- **Models:** Creation, relationships, serialization

## Styling & UX

### Design System
- **Theme:** Glassmorphism with dark background (rgb(15, 23, 42))
- **Primary Gradient:** #8b5cf6 → #ec4899 (purple to pink)
- **Backdrop Filter:** blur(10-15px)
- **Border:** rgba(255, 255, 255, 0.15)

### Responsive Breakpoints
- **Desktop:** Full grid layout
- **Tablet (768px):** Adjusted padding, 2-column layouts
- **Mobile (480px):** Single column, optimized spacing

### Country Flags
- **Source:** CDN (flag-icons@6.11.0)
- **Format:** 4x3 aspect ratio SVG
- **Integration:** Automatic from ISO codes

## Integration with Main App

### Blueprint Registration
```python
# In app/__init__.py
from app.residencies import residencies
app.register_blueprint(residencies)  # Prefix: /residencies
```

### Database Initialization
```python
with app.app_context():
    db.create_all()
    ResidencyDataLoader.load_from_investment_data(app)
```

## Performance Optimizations

1. **Database Indexes** on `country`, `program_name`, `program_type`
2. **Pagination** - 12 programs per page
3. **Currency Rates** - Cached in EligibilityChecker singleton
4. **Query Filtering** - Efficient SQLAlchemy filters
5. **JSON Storage** - For flexible document/embassy lists

## Future Enhancements

1. **WebSocket Integration** - Real-time eligibility updates
2. **Celery Tasks** - Async ROI calculator, PDF generation
3. **Advanced Matching** - ML-based program recommendations
4. **Consultant Directory** - Link programs to experts
5. **Application Portal** - Track applications end-to-end
6. **Webhooks** - Notify users of program updates
7. **Multi-language** - Support for 10+ languages
8. **Admin Dashboard** - Program management interface

## Configuration

### Environment Variables
```bash
# Optional: enable advanced features
ENABLE_CELERY=false
ENABLE_WEBSOCKET=false
DATABASE_URL=sqlite:///nexora.db
```

### Database Selection
- **Development:** SQLite (included)
- **Production:** PostgreSQL recommended
  ```python
  # In config.py
  SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost/nexora'
  ```

## Troubleshooting

### No Programs Appearing
1. Load data: `flask load-residency-data`
2. Verify database: `flask shell`
   ```python
   >>> from app.residencies.models import ResidencyProgram
   >>> ResidencyProgram.query.count()  # Should be > 0
   ```

### Currency Conversion Not Working
- Ensure all amounts are positive
- Check supported currencies in `EligibilityChecker.currency_rates`

### Templates Not Found
- Verify `app/residencies/templates/` exists
- Check blueprint template_folder configuration

## Support & Documentation

- **API Documentation:** OpenAPI/Swagger (future)
- **Code Examples:** See tests in `tests/test_residencies_eligibility.py`
- **Database Queries:** Use Flask shell (`flask shell`)

---

**Last Updated:** February 2024
**Version:** 1.0
**Status:** Production Ready
