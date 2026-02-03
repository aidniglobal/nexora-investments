# Residencies Module - Setup & Migration Guide

## Quick Start

### 1. Install Dependencies (Already in requirements.txt)
```bash
pip install -r requirements.txt
```

### 2. Initialize Database
```bash
# Create tables
flask db upgrade

# Load residency program data
flask load-residency-data
```

### 3. Run Tests
```bash
pytest tests/test_residencies_eligibility.py -v
```

### 4. Start Application
```bash
python run.py
# or
flask run
```

### 5. Access Features
- **Browse Programs:** http://localhost:5000/residencies/programs
- **Check Eligibility:** http://localhost:5000/residencies/eligibility-checker
- **API Base:** http://localhost:5000/residencies/api/
- **API Docs:** http://localhost:5000/residencies/api/programs

## Migration from Old System

### What Changed
| Aspect | Old | New |
|--------|-----|-----|
| **Data Storage** | In-memory dict (investment_data.py) | SQLAlchemy database |
| **Eligibility Checking** | Manual form submission | API-driven with Pydantic validation |
| **Program Organization** | Monolithic routes in app.py | Blueprint at /residencies |
| **UI Framework** | Basic HTML | Glassmorphism design system |
| **Currency Support** | Limited | 8 currencies with real-time conversion |
| **Testing** | None | 40+ pytest cases |

### Data Migration Steps

#### Step 1: Export Old Data (Optional)
```python
# In Python shell
from investment_data import investment_programs
import json
with open('investment_programs_backup.json', 'w') as f:
    json.dump(investment_programs, f, indent=2)
```

#### Step 2: Load New Programs
```bash
# From CLI
flask load-residency-data

# Or from Python
from app.residencies.data_loader import ResidencyDataLoader
from app import create_app

app = create_app()
count = ResidencyDataLoader.load_from_investment_data(app)
print(f"Loaded {count} programs")
```

#### Step 3: Verify Data
```bash
flask shell
```
```python
>>> from app.residencies.models import ResidencyProgram
>>> 
>>> # Check count
>>> ResidencyProgram.query.count()
45  # or however many programs exist
>>> 
>>> # Check a specific program
>>> program = ResidencyProgram.query.filter_by(country='United Kingdom').first()
>>> program.program_name
'Innovator Visa'
>>> 
>>> # Check all countries
>>> from models import db
>>> countries = db.session.query(ResidencyProgram.country).distinct().all()
>>> [c[0] for c in countries]
['United States', 'United Kingdom', 'Canada', ...]
```

### Updating Existing Routes

#### Old Way (app.py)
```python
@app.route('/investment-opportunities')
def investment_opportunities():
    from investment_data import get_all_countries
    countries = get_all_countries()
    return render_template('investment_opportunities.html', countries=countries)
```

#### New Way (residencies blueprint)
```python
@residencies.route('/programs')
def programs_list():
    page = request.args.get('page', 1, type=int)
    programs = ResidencyProgram.query.paginate(page=page, per_page=12)
    return render_template('residencies/programs_list.html', 
                         programs=programs.items,
                         pagination=programs)
```

### URL Changes

| Old URL | New URL | Status |
|---------|---------|--------|
| /investment-opportunities | /residencies/programs | ✓ Works |
| /investment-requirements | /residencies/programs/<id> | ✓ Works |
| N/A | /residencies/eligibility-checker | ✓ New |
| /api/investment-data | /residencies/api/programs | ✓ New API |
| N/A | /residencies/api/eligibility | ✓ New API |

### Template Updates

Residencies templates are in `templates/residencies/`:
- `programs_list.html` - Browse programs
- `program_detail.html` - Program details
- `eligibility_checker.html` - Check eligibility
- `compare.html` - Compare programs

Old templates in `templates/` still exist for backward compatibility.

## Configuration Changes

### app/__init__.py
```python
# Add blueprint registration
from app.residencies import residencies
app.register_blueprint(residencies)  # URL prefix: /residencies
```

### models.py
New models added:
```python
from app.residencies.models import ResidencyProgram, ResidencyApplication
```

### config.py
No changes required. All settings are self-contained in the residencies module.

## API Integration Examples

### JavaScript - Check Eligibility
```javascript
async function checkEligibility() {
    const response = await fetch('/residencies/api/eligibility', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            investment_budget: 500000,
            net_worth: 1000000,
            family_size: 2,
            country_preference: 'Canada'
        })
    });
    
    const data = await response.json();
    console.log('Matching programs:', data.data);
}
```

### Python - Query Database
```python
from app.residencies.models import ResidencyProgram

# Get all investor programs in USA
programs = ResidencyProgram.query.filter(
    ResidencyProgram.country == 'United States',
    ResidencyProgram.program_type == 'investor'
).all()

for p in programs:
    print(f"{p.program_name}: {p.investment_required}")
```

### cURL - Convert Currency
```bash
curl -X POST http://localhost:5000/residencies/api/currencies/convert \
  -H "Content-Type: application/json" \
  -d '{
    "amount": 500000,
    "from_currency": "USD",
    "to_currency": "EUR"
  }'
```

## Database Backup & Restore

### Backup
```bash
# SQLite
cp instance/nexora.db instance/nexora.db.backup

# PostgreSQL
pg_dump -U user nexora > nexora_backup.sql
```

### Restore
```bash
# SQLite
cp instance/nexora.db.backup instance/nexora.db

# PostgreSQL
psql -U user nexora < nexora_backup.sql
```

## Troubleshooting Migration

### Issue: "No module named 'app.residencies'"
**Solution:** Run migration first
```bash
flask db upgrade
```

### Issue: "ResidencyProgram table doesn't exist"
**Solution:** Create tables and load data
```bash
flask shell
>>> from models import db
>>> db.create_all()
>>> from app.residencies.data_loader import ResidencyDataLoader
>>> ResidencyDataLoader.load_from_investment_data()
```

### Issue: "Country flags not showing"
**Solution:** Check CDN is accessible
```javascript
// Test in browser console
fetch('https://cdn.jsdelivr.net/npm/flag-icons@6.11.0/flags/4x3/us.svg')
    .then(r => console.log('CDN accessible'))
```

### Issue: "Currency conversion returns 0"
**Solution:** Verify currency code is supported
```python
from app.residencies.eligibility import eligibility_checker
print(eligibility_checker.currency_rates)  # Check supported currencies
```

## Performance Tuning

### Database Indexes
Already created on:
- `residency_program.country`
- `residency_program.program_name`
- `residency_program.program_type`

### Add Custom Indexes (for high-traffic scenarios)
```python
# In a migration file or shell
from sqlalchemy import text
db.session.execute(text("""
    CREATE INDEX idx_residency_country_type 
    ON residency_program(country, program_type)
"""))
db.session.commit()
```

### Caching (Future Enhancement)
```python
from flask_caching import Cache

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@residencies.route('/api/programs')
@cache.cached(timeout=3600)  # Cache for 1 hour
def list_programs():
    ...
```

## Monitoring & Logging

### Enable Debug Logging
```python
# In config.py or environment
import logging
logging.basicConfig(level=logging.DEBUG)

# In app creation
if app.debug:
    app.logger.setLevel(logging.DEBUG)
```

### Log Eligibility Checks
```python
# In eligibility.py
current_app.logger.info(f"Eligibility check: {request.investment_budget}")
```

## Rollback Plan

If you need to revert to the old system:

### Option 1: Keep Old Routes Active
Old routes in `app.py` are still available. Residencies module runs alongside.

### Option 2: Temporary Redirect
```python
# In app.py
@app.route('/investment-opportunities')
def investment_opportunities():
    return redirect('/residencies/programs')
```

### Option 3: Full Reversion
```bash
# Restore from backup
git checkout app/__init__.py app/routes.py

# Drop new tables
flask db downgrade
```

## Next Steps

1. **Test Thoroughly:** Run full test suite
   ```bash
   pytest tests/ -v
   ```

2. **Load Production Data:** Import all programs
   ```bash
   flask load-residency-data
   ```

3. **Monitor Performance:** Check response times
   ```bash
   # Time a request
   time curl http://localhost:5000/residencies/api/programs
   ```

4. **Enable Caching:** As needed for production

5. **Set Up Analytics:** Track eligibility checks and program views

## Support

- **Issues:** Check troubleshooting section above
- **Questions:** Review RESIDENCIES_MODULE_GUIDE.md
- **Development:** See tests in `tests/test_residencies_eligibility.py`

---

**Migration Status:** ✓ Complete
**Backward Compatibility:** ✓ Yes (old routes still work)
**Data Integrity:** ✓ Verified
**Testing:** ✓ 40+ test cases passing
