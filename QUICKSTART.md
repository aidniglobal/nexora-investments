# 🚀 Quick Start Guide - Nexora Platform

## 5-Minute Setup

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Initialize Database
```bash
python init_residency_db.py
```

### Step 3: Run Application
```bash
python run.py
```

### Step 4: Open Browser
```
http://localhost:5000
```

---

## 🎯 Key Features to Explore

### 1. Browse Residency Programs
Visit `/residencies` to see all available programs from 10 countries

### 2. Check Eligibility
Go to `/residency-eligibility` and answer questions about:
- Investment budget
- Annual income
- Citizenship requirements
- Preferred countries

### 3. Calculate ROI
Use `/residency-calculator` to:
- Calculate investment returns
- Break down costs
- Estimate timelines

### 4. Compare Programs
Visit `/residency-comparison` to:
- Select multiple programs
- Compare features side-by-side
- View investment requirements

### 5. Find Consultants
Check `/consultants` to:
- Browse expert profiles
- See ratings and experience
- Book consultations

### 6. Read Blog
Visit `/residency-blog` for:
- Guides and tutorials
- Case studies
- Immigration tips

---

## 📊 Sample Data

### Available Countries
1. **Portugal** - Golden Visa (from €280,000)
2. **Malta** - Residency Program (from €12,000/year)
3. **Greece** - Golden Visa (from €250,000)
4. **Spain** - Golden Visa (from €500,000)
5. **Cyprus** - Permanent Residence (from €200,000)
6. **UK** - Tier 1 Investor (from £2,000,000)
7. **Canada** - Express Entry & Entrepreneur (from CAD $300,000)
8. **Australia** - Skilled Visa & Investor (from AUD $1,500,000)
9. **UAE** - Golden Visa (from AED 750,000)
10. **Singapore** - Tech.Pass (from SGD $30,000/month)

### Program Types
- Investment Residency
- Employment-based
- Skilled Migration
- Retirement/Passive Income
- Business/Entrepreneur

---

## 👤 User Features

### Register & Login
```
Route: /register
Create account and start tracking applications
```

### View Dashboard
```
Route: /dashboard
See all your documents and applications
```

### Save Programs
```
Save your favorite programs for later
View in "My Saved Programs" section
```

### Track Applications
```
Route: /my-residency-applications
Monitor application status and progress
```

---

## 🧮 Calculator Example

### ROI Calculation
```
Investment: $500,000
Expected Return: 5% annually
Period: 5 years

Result:
Final Value: $637,565
Total Profit: $137,565
```

### Cost Breakdown
```
Investment: $500,000
Application Fees: $5,000
Legal Fees: $3,000
Processing Fees: $1,000
─────────────────
Total Cost: $509,000
```

---

## 📱 Responsive Design

The platform works on:
- ✅ Desktop computers
- ✅ Tablets
- ✅ Mobile phones

Navigate using responsive menu on all devices.

---

## 🔐 User Accounts

### Create Account
1. Click "Register" button
2. Enter name, email, password
3. Accept terms and conditions
4. Verify email (if configured)

### Login
1. Go to `/login`
2. Enter email and password
3. Access your dashboard

### Manage Profile
1. Go to `/profile`
2. Update personal information
3. Change profile picture
4. Save changes

---

## 🎓 Eligibility Checker Walkthrough

### Step 1: Enter Budget
```
"How much can you invest?"
Example: $500,000
```

### Step 2: Enter Income
```
"What's your annual income?"
Example: $100,000
```

### Step 3: Select Criteria
```
☑ I want a path to citizenship
☐ Multi-generational family
☑ Fast processing preferred
```

### Step 4: Choose Countries
```
☑ Portugal
☑ Malta
☑ Spain
☐ Canada
☑ Australia
```

### Result: Top Matching Programs!
```
1. Portugal Golden Visa - 95% match
2. Malta Residency - 88% match
3. Spain Golden Visa - 85% match
...
```

---

## 💡 Pro Tips

### Find Best Programs
1. Use Eligibility Checker first
2. Compare top 3 matches
3. Read blog posts about programs
4. Book consultation with expert

### Calculate True Costs
1. Use ROI Calculator
2. Add processing fees
3. Include legal costs
4. Factor in travel time

### Make Smart Comparisons
1. Compare investment amounts
2. Check processing times
3. Verify citizenship pathways
4. Review visa-free benefits

### Connect with Experts
1. Browse consultant directory
2. Check ratings and reviews
3. Review specializations
4. Book consultation

---

## 🔧 Configuration

### Email Setup (Optional)
Edit `app.py`:
```python
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'your-email'
app.config['MAIL_PASSWORD'] = 'your-password'
```

### Database (Optional)
Edit `config.py` for production:
```python
# SQLite (default)
SQLALCHEMY_DATABASE_URI = 'sqlite:///nova.db'

# PostgreSQL
SQLALCHEMY_DATABASE_URI = 'postgresql://user:pass@localhost/nova'
```

---

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Use different port
python run.py --port 5001
```

### Database Error
```bash
# Reinitialize database
python init_residency_db.py
```

### Import Error
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Static Files Not Loading
```bash
# Clear browser cache and reload
Ctrl+Shift+R (or Cmd+Shift+R on Mac)
```

---

## 📞 Support

### Getting Help
- 📧 Email: support@aidiniglobal.com
- 🌐 Website: www.aidiniglobal.com
- 📱 Phone: +919879428291

### Common Questions

**Q: How do I add more programs?**
A: Edit `residency_data.py` and add new entries following the existing format.

**Q: Can I customize the design?**
A: Yes! Modify `static/css/styles.css` for styling and templates for layout.

**Q: How do I add consultants?**
A: Use the database directly or create an admin panel.

**Q: Is my data secure?**
A: Yes! Passwords are hashed and sensitive data is protected.

---

## 🎉 You're All Set!

Your Nova residency platform is ready to use. Start exploring and helping users find their ideal residency program!

**Happy exploring! 🌍**

---

**Version:** 2.0  
**Last Updated:** December 2025  
**Developed by:** Aidni Global LLP
