# 🚀 PythonAnywhere Deployment Guide - Nexora Investments

**Last Updated**: January 25, 2026  
**Status**: ✅ Ready for Deployment  
**Version**: 2.1.0  

---

## 📋 Pre-Deployment Checklist

- [x] All code committed to main branch
- [x] All changes pushed to origin/main
- [x] No new dependencies added
- [x] Database compatible (SQLite)
- [x] Environment tested locally
- [x] Documentation updated

---

## 🔗 Git Repository

**Repository**: https://github.com/aidniglobal/nexora-investments  
**Branch**: main  
**Latest Commit**: feat: Expand investment programs to 46 countries...  

---

## 📥 Step-by-Step Deployment

### Step 1: Access PythonAnywhere Console

1. Log in to your PythonAnywhere account
2. Go to **Web** tab
3. Click on your web app (e.g., `yourusername.pythonanywhere.com`)

### Step 2: Clone/Update Repository

Open a **Bash console** in PythonAnywhere:

```bash
# Navigate to home directory
cd ~

# If this is first time, clone the repo
git clone https://github.com/aidniglobal/nexora-investments.git

# If already cloned, pull latest changes
cd nexora-investments
git pull origin main
```

### Step 3: Install Dependencies

```bash
# Install requirements
pip install -r requirements.txt --user

# Or if using light version (fewer dependencies)
pip install -r requirements-light.txt --user
```

### Step 4: Update WSGI Configuration

1. Go to **Web** tab in PythonAnywhere
2. Click on your web app
3. Under **Code** section, update the WSGI file:

**Path**: `/home/yourusername/nexora-investments/app.py`

**WSGI Content**:
```python
import sys

path = '/home/yourusername/nexora-investments'
if path not in sys.path:
    sys.path.append(path)

from app import app as application
```

### Step 5: Configure Web App Settings

1. **Python version**: Python 3.9 or 3.10
2. **Virtualenv**: (Optional, but recommended)
3. **Source code**: `/home/yourusername/nexora-investments`

### Step 6: Database Setup (If First Time)

In **Bash console**:

```bash
cd ~/nexora-investments

# The app uses SQLite which creates DB automatically
# No manual setup needed - app.py handles db.create_all()

# Optional: Initialize with test data
python -c "from app import app, db; app.app_context().push(); db.create_all()"
```

### Step 7: Reload Web App

1. Go to **Web** tab
2. Click **Reload** button at the top
3. Wait for green checkmark ✅

### Step 8: Configure Static Files

1. Go to **Web** tab
2. Under **Static files**, add:
   - **URL**: `/static/`
   - **Directory**: `/home/yourusername/nexora-investments/static`

3. Add another entry for uploads:
   - **URL**: `/uploads/`
   - **Directory**: `/home/yourusername/nexora-investments/uploads`

---

## 🔐 Environment Variables

Create or update `.env` file in `/home/yourusername/nexora-investments/`:

```env
# Flask Configuration
FLASK_ENV=production
FLASK_DEBUG=False

# Email Configuration (Optional)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_app_password

# CareerJet Affiliate (Already in code)
CAREERJET_AFFILIATE_ID=22926d61e8d645ae480bb1297fa3022f

# Secret Key
SECRET_KEY=your-secret-key-here
```

**Note**: Update with your actual values if needed.

---

## 📝 Important File Locations

```
/home/yourusername/nexora-investments/
├── app.py                    # Main Flask app
├── config.py                 # Configuration
├── investment_data.py        # 46 countries, 75 programs
├── models.py                 # Database models
├── requirements.txt          # Dependencies
├── requirements-light.txt    # Minimal dependencies
│
├── templates/                # HTML templates
│   ├── base.html
│   ├── job_search.html       # Job search with modal
│   ├── index.html
│   └── ...
│
├── static/                   # CSS, JS, images
│   ├── css/styles.css
│   ├── js/script.js
│   └── images/
│
├── uploads/                  # User uploads
│   ├── profile_pics/
│   ├── verified_documents/
│   └── photos/
│
└── nexora.db                 # SQLite database (auto-created)
```

---

## 🧪 Testing After Deployment

### Test 1: Home Page
```
https://yourusername.pythonanywhere.com/
```
Expected: Home page loads successfully

### Test 2: Job Search
```
https://yourusername.pythonanywhere.com/job-search
```
Expected: Search form loads, can search jobs

### Test 3: Investment Programs
```
https://yourusername.pythonanywhere.com/
```
Expected: Navigation shows investment programs

### Test 4: Modal Job Details
1. Go to job-search
2. Search for any job
3. Click "View Details"
4. Expected: Modal popup with job details (stays on page)

### Test 5: Registration/Login
1. Try to register
2. Try to login
3. Expected: Authentication works

---

## ⚙️ Troubleshooting

### Issue: 500 Internal Server Error

**Solution**:
1. Check PythonAnywhere error log
2. Verify WSGI file path is correct
3. Check database permissions
4. Reload web app

### Issue: Static Files Not Loading

**Solution**:
1. Verify static files configuration
2. Check directory paths are absolute
3. Run `python collect_static.py` if using Django (not needed here)

### Issue: Database Not Found

**Solution**:
```bash
cd ~/nexora-investments
python -c "from app import app, db; app.app_context().push(); db.create_all()"
```

### Issue: Module Not Found

**Solution**:
```bash
pip install -r requirements.txt --user
# OR
pip install -r requirements-light.txt --user
```

### Issue: Can't Access /uploads Folder

**Solution**:
1. Make sure static files are configured
2. Check uploads folder exists
3. Verify folder permissions (755)

---

## 📚 Key Files Updated in This Release

### investment_data.py
- **Before**: 23 countries, ~26 programs
- **After**: 46 countries, 75 programs
- **Size**: ~2000+ lines of data

### app.py
- **CareerJet Integration**: Affiliate ID updated
- **Job Search Routes**: Enhanced with sample data
- **Lines**: 1369 total

### templates/job_search.html
- **Modal View**: New JavaScript function
- **User Experience**: Enhanced with modal popup
- **Lines**: 251 total

### README.md & QUICKSTART.md
- **Updated**: Feature descriptions
- **New**: Job search guide
- **Coverage**: 46 countries mentioned

---

## 🔄 Continuous Updates

To pull latest changes in future:

```bash
cd ~/nexora-investments
git pull origin main
pip install -r requirements.txt --user
# Then reload web app in PythonAnywhere
```

---

## 🎉 Success Indicators

After deployment, you should see:

✅ Home page loads  
✅ Job search works  
✅ Modal opens for job details  
✅ Investment programs display  
✅ User authentication works  
✅ Database saves data  
✅ Static files load (CSS, JS)  

---

## 📞 Support & Resources

### Documentation Files
- [README.md](README.md) - Feature overview
- [QUICKSTART.md](QUICKSTART.md) - Quick start
- [UPDATES_JANUARY_2026.md](UPDATES_JANUARY_2026.md) - What's new
- [CAREERJET_AFFILIATE_UPDATE.md](CAREERJET_AFFILIATE_UPDATE.md) - Affiliate config

### PythonAnywhere Help
- **Web console**: For debugging
- **Error log**: Check for issues
- **Reload button**: To apply changes

---

## ✨ New Features in This Version

1. **46 Countries** - Global investment programs
2. **75 Programs** - Diverse options with varied investments
3. **CareerJet Affiliate** - Global job search with tracking
4. **Modal UI** - Better user experience, stays on app
5. **Enhanced Documentation** - Complete guides for deployment

---

**Deployment Status**: ✅ Ready  
**Estimated Setup Time**: 15-20 minutes  
**Database**: SQLite (auto-created)  
**Python Version**: 3.9+  
**No New Dependencies**: ✅ Uses existing packages  

**Go to**: https://yourusername.pythonanywhere.com to access your live app! 🎉

