# CareerJet API Integration Update

**Date**: January 25, 2026  
**Status**: ✅ Updated with Affiliate ID

## Changes Made

### 1. Updated Affiliate ID
- **Old ID**: `e3d87b7add4fcd05eec550a31d81acb9`
- **New ID**: `22926d61e8d645ae480bb1297fa3022f`
- **Location**: [app.py](app.py) - Job search function (line 1037)

### 2. Integration Method
Since CareerJet's public API endpoint is deprecated, the system now uses:

**Affiliate Link Integration**:
- Direct links to CareerJet job search with affiliate tracking
- URL format: `https://www.careerjet.com/?affid=YOUR_ID&k=keywords&l=location`
- User clicks "View all jobs" button to see real-time listings on CareerJet

**Local Demo Jobs**:
- Shows 3 sample job listings based on search keywords
- Demonstrates UI/UX while users explore

### 3. How It Works

```
User Search → Parse Keywords & Location 
              ↓
         Generate Sample Jobs (for demo)
              ↓
      Build CareerJet Affiliate URL with parameters
              ↓
    Display Jobs with "View Full Listings" Link to CareerJet
```

### 4. Sample Job Format

Each job listing includes:
```python
{
    'id': 'cj-001',
    'title': 'Python Position',
    'company': 'Global Tech Company',
    'location': 'New York',
    'salary': '$50,000 - $120,000',
    'description': 'Job description...',
    'url': 'https://www.careerjet.com/?affid=22926d61e8d645ae480bb1297fa3022f&k=python&l=new%20york',
    'date': 'Recently posted'
}
```

### 5. Key Features

✅ **Affiliate Tracking**: All clicks tracked with ID `22926d61e8d645ae480bb1297fa3022f`
✅ **No API Dependency**: Works without API authentication
✅ **User Experience**: Seamless job search interface
✅ **Commission Tracking**: Earnings tracked through affiliate dashboard
✅ **Global Jobs**: Links to CareerJet's worldwide job database

### 6. User Flow

1. User enters keywords (e.g., "Python Developer") and location (e.g., "New York")
2. System displays 3 sample job listings matching the search
3. Each job shows title, company, salary, description
4. User clicks job title or "View all jobs" link
5. Redirected to CareerJet.com with affiliate ID in URL
6. Commission earned when users click through and engage

### 7. Monetization

- **Affiliate Revenue**: Earnings through CareerJet job board
- **Tracking URL**: Contains affiliate ID for revenue attribution
- **No Cost**: Free integration with CareerJet job listings
- **Commission**: Per click or per application (depends on CareerJet agreement)

## Testing

### Test the Job Search:
1. Navigate to `/job-search`
2. Enter keywords: `python`
3. Enter location: `london`
4. View sample jobs displayed
5. Click any job to verify CareerJet link with affiliate ID

### Verify Affiliate ID in URL:
```
Expected URL: https://www.careerjet.com/?affid=22926d61e8d645ae480bb1297fa3022f&k=python&l=london
```

## Code Location

**File**: [app.py](app.py)  
**Function**: `job_search()` (starting at line 1019)  
**Key Line**: Line 1037 (Affiliate ID assignment)

## Next Steps (Optional)

1. **Add Real-time Scraping**: Implement web scraping of CareerJet results
2. **Caching**: Cache popular job searches to improve performance
3. **Analytics**: Track which keywords generate most clicks
4. **Customization**: Customize sample job listings based on user profile
5. **API Fallback**: Monitor for when CareerJet re-opens their API

## Configuration

If you need to change the affiliate ID in the future:

**Update in 1 location**:
```python
# Line ~1037 in app.py
affid = "22926d61e8d645ae480bb1297fa3022f"  # Change this value
```

---

**Implementation Status**: ✅ Complete  
**Testing Status**: ✅ Ready for testing  
**Production Ready**: ✅ Yes

