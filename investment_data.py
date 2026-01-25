"""
Nexora Global Investment & Business Migration Programs Database
Comprehensive worldwide investment programs and business migration opportunities
"""

investment_programs = {
    "USA": {
        "EB-5 Immigrant Investor Program": {
            "Documents": [
                "Passport: Valid for at least 6 months",
                "Form I-485: Application to Register Permanent Residence",
                "Form I-526: Immigrant Petition by Alien Entrepreneur",
                "Proof of funds: Investment capital of $1 million (or $500k in TEA areas)",
                "Business plan: Detailed investment project plan",
                "Financial documents: Bank statements, tax returns, proof of source of funds",
                "Employment verification: Letters showing job creation plan"
            ],
            "Investment Required": "$500,000 - $1,000,000",
            "Processing Time": "18-36 months",
            "Embassy Locations": ["New York", "Los Angeles", "Chicago", "Houston", "Miami"],
            "Interview Requirement": "Yes, interview required",
            "Benefits": "Permanent residency, family inclusion, path to citizenship",
            "Notes": "Investment must create at least 10 jobs. Regional centers available for easier processing."
        },
        "E-2 Treaty Investor Visa": {
            "Documents": [
                "Passport: Valid travel document",
                "DS-156: Nonimmigrant Visa Application",
                "Photos: Recent passport-style photos",
                "Business registration: Company formation documents",
                "Investment proof: Bank statements, evidence of capital transfer",
                "Business plan: Detailed operational and financial plan",
                "Tax returns: Previous 2-3 years",
                "Employment letters: Verification of business operations"
            ],
            "Investment Required": "$50,000 - $100,000 (minimum)",
            "Processing Time": "2-4 weeks",
            "Embassy Locations": ["Nationwide",
 "Treaty-dependent countries"],
            "Interview Requirement": "Yes, interview required",
            "Benefits": "Valid up to 5 years, renewable, can bring family",
            "Notes": "Available for nationals of 60+ treaty countries. Can manage any size business."
        },
        "EB-1C Multinational Executive": {
            "Documents": [
                "Form I-140: Immigrant Petition for Alien Worker",
                "Passport and travel documents",
                "Evidence of executive/manager status",
                "Organizational chart and company documents",
                "Tax returns: 3-5 years for both companies",
                "Employment verification: Letters from both employers",
                "Business relationship documentation"
            ],
            "Investment Required": "Business ownership transfer",
            "Processing Time": "12-24 months",
            "Embassy Locations": ["Major US cities"],
            "Interview Requirement": "Usually yes",
            "Benefits": "Green card for executive/manager, family eligibility",
            "Notes": "For managers/executives transferring between companies."
        }
    },
    "United Kingdom": {
        "Innovator Visa": {
            "Documents": [
                "Passport: Valid for duration of stay",
                "Business plan: Detailed 3-5 year plan",
                "Endorsement: From accredited body",
                "Financial documents: Proof of £50,000 investment",
                "CV and qualifications",
                "English language certificate: CEFR level B2 or above",
                "Tuberculosis test: If required"
            ],
            "Investment Required": "£50,000 minimum",
            "Processing Time": "8 weeks",
            "Embassy Locations": ["London", "Birmingham", "Manchester", "Edinburgh"],
            "Interview Requirement": "May be required",
            "Benefits": "Route to settlement, business ownership in UK",
            "Notes": "For founders of innovative businesses. Can bring spouse and dependents."
        },
        "Startup Visa": {
            "Documents": [
                "Passport",
                "Business plan",
                "Endorsement from accredited body",
                "CV and qualifications",
                "English language evidence",
                "Financial documents",
                "Tuberculosis certificate"
            ],
            "Investment Required": "No specific investment required",
            "Processing Time": "8 weeks",
            "Embassy Locations": ["Nationwide"],
            "Interview Requirement": "May be required",
            "Benefits": "Starting point for business, family can join",
            "Notes": "For early-stage entrepreneurs with innovative ideas."
        },
        "Standard Visitor Visa": {
            "Documents": [
                "Valid passport",
                "Completed application form",
                "Passport-style photo",
                "Proof of funds: £945 + living costs",
                "Proof of ties to home country",
                "Return flight booking"
            ],
            "Investment Required": "N/A (Visa cost £115)",
            "Processing Time": "3 weeks - 3 months",
            "Embassy Locations": ["Worldwide"],
            "Interview Requirement": "Usually not required",
            "Benefits": "Short-term business/tourism",
            "Notes": "Valid for 6 months. No work permitted."
        }
    },
    "Germany": {
        "Self-Employment Visa": {
            "Documents": [
                "Passport",
                "Business plan: Detailed plan in German/English",
                "Evidence of qualifications: Credentials, resume",
                "Financial proof: Sufficient capital (€50,000-€100,000)",
                "Insurance documents: Health insurance",
                "Tax registration certificate",
                "Lease agreement for business location"
            ],
            "Investment Required": "€50,000 - €100,000",
            "Processing Time": "6-8 weeks",
            "Embassy Locations": ["Berlin", "Munich", "Hamburg", "Frankfurt", "Cologne"],
            "Interview Requirement": "Yes, usually required",
            "Benefits": "Path to permanent residency, family sponsorship",
            "Notes": "For entrepreneurs setting up business in Germany."
        },
        "EU Blue Card": {
            "Documents": [
                "Passport",
                "Employment contract",
                "Degree certificate: Relevant qualification",
                "Health insurance",
                "Proof of funds for living"
            ],
            "Investment Required": "N/A (Employment-based)",
            "Processing Time": "4-6 weeks",
            "Embassy Locations": ["Major cities"],
            "Interview Requirement": "Usually not required",
            "Benefits": "EU mobility, family reunification possible",
            "Notes": "For highly skilled workers earning €55,200+ annually."
        }
    },
    "Singapore": {
        "EntrePass": {
            "Documents": [
                "Passport",
                "Business registration documents",
                "Shareholders' agreement",
                "Company's financial statements",
                "Business plan: Detailed operations plan",
                "Personal financial documents",
                "Educational/professional credentials"
            ],
            "Investment Required": "SGD 500,000 (preferred) or business acumen",
            "Processing Time": "4-6 weeks",
            "Embassy Locations": ["Singapore"],
            "Interview Requirement": "May be required",
            "Benefits": "Self-employment, path to permanent residency",
            "Notes": "For foreign entrepreneurs starting business in Singapore."
        },
        "Tech.Pass": {
            "Documents": [
                "Passport",
                "Resume/CV",
                "Job offer letter",
                "Company incorporation certificate",
                "Educational qualifications"
            ],
            "Investment Required": "N/A (Employment-based)",
            "Processing Time": "2-3 weeks",
            "Embassy Locations": ["Singapore"],
            "Interview Requirement": "Usually not required",
            "Benefits": "Tech talent fast-track, family eligible",
            "Notes": "For tech professionals earning SGD 14,000+ monthly."
        }
    },
    "Canada": {
        "Start-up Visa": {
            "Documents": [
                "Passport",
                "Business plan",
                "Letter of support from designated organization",
                "Proof of funds: CAD 75,000+",
                "Educational credentials",
                "Language test: IELTS or TOEFL",
                "Medical exam results"
            ],
            "Investment Required": "CAD 75,000+",
            "Processing Time": "12-16 months",
            "Embassy Locations": ["Toronto", "Vancouver", "Calgary", "Montreal"],
            "Interview Requirement": "May be required",
            "Benefits": "Path to permanent residency, family eligibility",
            "Notes": "For innovative entrepreneurs with backing from Canadian investors."
        },
        "Self-Employed": {
            "Documents": [
                "Passport",
                "Proof of experience: 2 years in past 5 years",
                "Financial proof: CAD 20,000+",
                "Language test scores",
                "Education credentials",
                "Medical and police certificates"
            ],
            "Investment Required": "CAD 20,000+",
            "Processing Time": "12-24 months",
            "Embassy Locations": ["Nationwide"],
            "Interview Requirement": "Likely",
            "Benefits": "Permanent residency, family can join",
            "Notes": "For individuals who are self-employed in an eligible occupation."
        }
    },
    "Australia": {
        "Skilled Visa (189)": {
            "Documents": [
                "Passport",
                "Skills assessment: From accredited body",
                "English language test: IELTS",
                "Educational credentials",
                "Work experience documentation",
                "Medical and police certificates",
                "State sponsorship (if applicable)"
            ],
            "Investment Required": "N/A (Points-based)",
            "Processing Time": "8-16 weeks",
            "Embassy Locations": ["Sydney", "Melbourne", "Brisbane", "Perth"],
            "Interview Requirement": "Usually not required",
            "Benefits": "Permanent residency, skilled worker status",
            "Notes": "Points-based system. Requires 65 points minimum."
        },
        "Business Innovation Visa (188A)": {
            "Documents": [
                "Passport",
                "Business plan",
                "Financial records: 2-3 years",
                "Evidence of investment capital",
                "English language certificate",
                "Medical and police checks",
                "State nomination"
            ],
            "Investment Required": "AUD 200,000 - AUD 1,250,000",
            "Processing Time": "12-24 months",
            "Embassy Locations": ["Major cities"],
            "Interview Requirement": "Usually yes",
            "Benefits": "Provisional residency, path to permanent residency",
            "Notes": "For business owners/investors. Can lead to 888 subclass."
        }
    },
    "Portugal": {
        "Golden Visa (Investment)": {
            "Documents": [
                "Passport",
                "Investment proof: €280,000+ (or other eligible investment)",
                "Financial documents: Bank statements, tax returns",
                "Business plan",
                "Police certificate",
                "Medical certificate",
                "Proof of accommodation"
            ],
            "Investment Required": "€280,000 - €500,000+",
            "Processing Time": "60-90 days",
            "Embassy Locations": ["Lisbon", "Porto"],
            "Interview Requirement": "Usually not required",
            "Benefits": "Residency, path to citizenship after 5 years",
            "Notes": "Multiple investment options including real estate, business, and employment creation."
        },
        "Digital Nomad Visa": {
            "Documents": [
                "Passport",
                "Employment contract or business registration",
                "Proof of income: €2,700+ monthly",
                "Health insurance",
                "Proof of accommodation",
                "Criminal record check"
            ],
            "Investment Required": "N/A (Income requirement €2,700/month)",
            "Processing Time": "4-6 weeks",
            "Embassy Locations": ["Worldwide"],
            "Interview Requirement": "Usually not required",
            "Benefits": "1-year residency, renewable, work from Portugal",
            "Notes": "For remote workers and freelancers."
        }
    },
    "Dubai (UAE)": {
        "Investor Visa": {
            "Documents": [
                "Passport",
                "Proof of investment: AED 500,000+",
                "Real estate purchase agreement (if applicable)",
                "Financial statements",
                "Business documents",
                "Medical test: Results",
                "Emirates ID application"
            ],
            "Investment Required": "AED 500,000 - AED 1,000,000+",
            "Processing Time": "2-4 weeks",
            "Embassy Locations": ["Dubai", "Abu Dhabi", "Sharjah"],
            "Interview Requirement": "Rarely",
            "Benefits": "Long-term residency, fast-track, family eligible",
            "Notes": "3-year renewable visa. Can invest in real estate or business."
        },
        "Business License Visa": {
            "Documents": [
                "Passport",
                "Business plan",
                "Commercial registration",
                "Lease agreement",
                "Financial proof",
                "Medical examination",
                "Background check"
            ],
            "Investment Required": "AED 100,000+ (variable by sector)",
            "Processing Time": "1-2 weeks",
            "Embassy Locations": ["Major emirates"],
            "Interview Requirement": "Usually not required",
            "Benefits": "Business ownership, residency, family sponsorship",
            "Notes": "Flexible business setup options available."
        }
    },
    "Switzerland": {
        "Entrepreneur Visa": {
            "Documents": [
                "Passport",
                "Business plan: Detailed CHF",
                "Financial proof: CHF 50,000+",
                "Company registration: Copy",
                "Lease agreement: Proof of location",
                "Educational documents",
                "Insurance: Health insurance"
            ],
            "Investment Required": "CHF 50,000 - CHF 200,000",
            "Processing Time": "8-12 weeks",
            "Embassy Locations": ["Bern", "Zurich", "Geneva", "Basel"],
            "Interview Requirement": "Yes, usually required",
            "Benefits": "Business residency, family can join",
            "Notes": "Approved by cantonal government. Must contribute to employment."
        }
    },
    "Netherlands": {
        "Self-Employed Visa": {
            "Documents": [
                "Passport",
                "Business plan",
                "Financial proof: EUR 6,500 - EUR 100,000+",
                "Chamber of Commerce registration",
                "Tax registration",
                "Health insurance",
                "Accommodation proof"
            ],
            "Investment Required": "EUR 6,500 - EUR 100,000+",
            "Processing Time": "4-6 weeks",
            "Embassy Locations": ["Amsterdam", "Rotterdam", "The Hague"],
            "Interview Requirement": "Usually not required",
            "Benefits": "Business ownership, family eligibility, path to residency",
            "Notes": "One of the most business-friendly countries in EU."
        },
        "Knowledge Migrant Visa": {
            "Documents": [
                "Passport",
                "Employment contract",
                "Educational credentials",
                "Medical insurance",
                "Proof of accommodation"
            ],
            "Investment Required": "N/A (Employment-based)",
            "Processing Time": "2-3 weeks",
            "Embassy Locations": ["Nationwide"],
            "Interview Requirement": "Rarely required",
            "Benefits": "Work permit, family can join, fast processing",
            "Notes": "For skilled professionals earning EUR 3,500+ monthly."
        }
    },
    "Ireland": {
        "Startup Visa": {
            "Documents": [
                "Passport",
                "Business plan",
                "Entrepreneur visa approval letter",
                "Proof of funds: EUR 100,000+ or investment commitment",
                "Educational credentials",
                "Medical insurance"
            ],
            "Investment Required": "EUR 100,000+",
            "Processing Time": "4-8 weeks",
            "Embassy Locations": ["Dublin", "Cork"],
            "Interview Requirement": "May be required",
            "Benefits": "Business ownership, EU citizenship path, tax benefits",
            "Notes": "Ireland has favorable tax rates for startups."
        },
        "Critical Skills Employment Permit": {
            "Documents": [
                "Employment contract",
                "Passport",
                "Educational qualifications",
                "Medical insurance"
            ],
            "Investment Required": "N/A (Employment-based)",
            "Processing Time": "2-4 weeks",
            "Embassy Locations": ["Nationwide"],
            "Interview Requirement": "Usually not required",
            "Benefits": "Work permit, path to residency, family eligible",
            "Notes": "Fast-track for skilled workers in demand sectors."
        }
    },
    "Spain": {
        "Investor Visa": {
            "Documents": [
                "Passport",
                "Investment proof: EUR 500,000+",
                "Real estate purchase agreement (if applicable)",
                "Financial documents",
                "Background check",
                "Health insurance",
                "Proof of accommodation"
            ],
            "Investment Required": "EUR 500,000 - EUR 1,000,000+",
            "Processing Time": "60-90 days",
            "Embassy Locations": ["Madrid", "Barcelona", "Valencia", "Malaga"],
            "Interview Requirement": "Rarely required",
            "Benefits": "Residency, family eligible, renewable, travel EU",
            "Notes": "Can invest in real estate, business, or capital investment."
        },
        "Digital Nomad Visa": {
            "Documents": [
                "Passport",
                "Employment contract or business registration",
                "Proof of income: EUR 2,300+ monthly",
                "Health insurance",
                "Criminal record certificate"
            ],
            "Investment Required": "N/A (Income requirement)",
            "Processing Time": "4-6 weeks",
            "Embassy Locations": ["Worldwide"],
            "Interview Requirement": "Usually not required",
            "Benefits": "1-year residency, renewable, work from Spain",
            "Notes": "For remote workers and freelancers."
        }
    },
    "New Zealand": {
        "Business Visa": {
            "Documents": [
                "Passport",
                "Business plan",
                "Financial proof: NZD 200,000+ or investment",
                "English language test",
                "Health screening",
                "Character reference",
                "Medical examination"
            ],
            "Investment Required": "NZD 200,000+ or demonstrate business plan",
            "Processing Time": "8-16 weeks",
            "Embassy Locations": ["Auckland", "Wellington"],
            "Interview Requirement": "Usually yes",
            "Benefits": "Business ownership, path to residency, stunning location",
            "Notes": "Business visa is 3 years, renewable."
        },
        "Skilled Migrant Visa": {
            "Documents": [
                "Passport",
                "Skills assessment",
                "English language test",
                "Educational credentials",
                "Job offer (optional but helpful)",
                "Medical and police certificates"
            ],
            "Investment Required": "N/A (Points-based)",
            "Processing Time": "12-20 weeks",
            "Embassy Locations": ["Nationwide"],
            "Interview Requirement": "Rarely required",
            "Benefits": "Permanent residency, sponsorship available",
            "Notes": "Points-based system. Currently around 160 points required."
        }
    },
    "Thailand": {
        "Retirement Visa": {
            "Documents": [
                "Passport",
                "Proof of income: THB 65,000/month or bank balance THB 800,000+",
                "Medical certificate",
                "Criminal record check",
                "Proof of accommodation"
            ],
            "Investment Required": "THB 800,000 (or THB 65,000/month income)",
            "Processing Time": "3-5 days",
            "Embassy Locations": ["Bangkok", "Chiang Mai", "Phuket"],
            "Interview Requirement": "Usually not required",
            "Benefits": "Long-term residency, renewable annually, low cost of living",
            "Notes": "Most popular visa for retirees in Southeast Asia."
        },
        "Elite Visa": {
            "Documents": [
                "Passport",
                "Application form",
                "Financial proof",
                "Background information",
                "Medical certificate"
            ],
            "Investment Required": "THB 600,000 - THB 2,000,000+ (one-time)",
            "Processing Time": "2-4 weeks",
            "Embassy Locations": ["Thailand-wide"],
            "Interview Requirement": "Rarely required",
            "Benefits": "20-year residency, privileges, fast-track services",
            "Notes": "Premium membership program with many benefits."
        }
    },
    "Malaysia": {
        "Malaysia My Second Home (MM2H)": {
            "Documents": [
                "Passport",
                "Proof of funds: MYR 300,000+ (or MYR 150,000 for age 50+)",
                "Fixed deposit: MYR 300,000 (or MYR 150,000)",
                "Medical certificate",
                "Police clearance",
                "Proof of accommodation"
            ],
            "Investment Required": "MYR 150,000 - MYR 300,000",
            "Processing Time": "2-3 months",
            "Embassy Locations": ["Kuala Lumpur", "Penang"],
            "Interview Requirement": "May be required",
            "Benefits": "10-year renewable visa, very affordable living",
            "Notes": "Popular with retirees and digital nomads."
        }
    },
    "Mexico": {
        "Temporary Residency": {
            "Documents": [
                "Passport",
                "Proof of income: USD 2,700+/month or lump sum USD 42,000+",
                "Proof of accommodation",
                "Criminal background check",
                "Medical examination"
            ],
            "Investment Required": "USD 42,000+ (or USD 2,700/month income)",
            "Processing Time": "4-6 weeks",
            "Embassy Locations": ["Mexico City", "Monterrey", "Guadalajara"],
            "Interview Requirement": "Usually yes",
            "Benefits": "4-year renewable visa, low cost of living",
            "Notes": "One of the easiest temporary residency options."
        },
        "Investor Visa": {
            "Documents": [
                "Passport",
                "Investment proof: MXN 2,700,000+ or real estate",
                "Financial documents",
                "Background check",
                "Medical examination"
            ],
            "Investment Required": "MXN 2,700,000+ (USD ~180,000)",
            "Processing Time": "6-8 weeks",
            "Embassy Locations": ["Major cities"],
            "Interview Requirement": "Usually yes",
            "Benefits": "Permanent residency path, business ownership",
            "Notes": "Can invest in real estate or business."
        }
    },
    "Vietnam": {
        "Temporary Residence Card": {
            "Documents": [
                "Passport",
                "Visa approval letter",
                "Application form",
                "Medical examination",
                "Police clearance",
                "Accommodation letter"
            ],
            "Investment Required": "N/A (Visa cost ~USD 50)",
            "Processing Time": "1-2 weeks",
            "Embassy Locations": ["Hanoi", "Ho Chi Minh City"],
            "Interview Requirement": "Usually not required",
            "Benefits": "Long-term stay, affordable living",
            "Notes": "Multiple entry visa available."
        }
    },
    "Philippines": {
        "SRRV (Special Resident Retiree's Visa)": {
            "Documents": [
                "Passport",
                "Proof of age: 35+",
                "Fixed deposit: PHP 500,000+ (age 35-49) or PHP 300,000 (age 50+)",
                "Medical examination",
                "Police clearance"
            ],
            "Investment Required": "PHP 300,000 - PHP 500,000",
            "Processing Time": "1-2 weeks",
            "Embassy Locations": ["Manila", "Cebu"],
            "Interview Requirement": "Usually not required",
            "Benefits": "Lifetime residency, can buy property",
            "Notes": "Great for retirees in tropical paradise."
        }
    },
    "Chile": {
        "Investment Visa": {
            "Documents": [
                "Passport",
                "Investment proof: USD 200,000+",
                "Business plan",
                "Financial documents",
                "Background check",
                "Medical examination"
            ],
            "Investment Required": "USD 200,000+",
            "Processing Time": "60-90 days",
            "Embassy Locations": ["Santiago"],
            "Interview Requirement": "Usually yes",
            "Benefits": "1-year visa, renewable, stable country",
            "Notes": "One of the most developed economies in Latin America."
        },
        "Skilled Worker Visa": {
            "Documents": [
                "Employment contract",
                "Passport",
                "Educational credentials",
                "Medical examination"
            ],
            "Investment Required": "N/A (Employment-based)",
            "Processing Time": "4-6 weeks",
            "Embassy Locations": ["Nationwide"],
            "Interview Requirement": "Rarely required",
            "Benefits": "Work permit, family eligible",
            "Notes": "For professionals in demand sectors."
        }
    },
    "Greece": {
        "Residence Permit (Golden Visa)": {
            "Documents": [
                "Passport",
                "Investment proof: EUR 250,000+",
                "Real estate purchase agreement",
                "Financial documents",
                "Police clearance"
            ],
            "Investment Required": "EUR 250,000+",
            "Processing Time": "30-45 days",
            "Embassy Locations": ["Athens", "Thessaloniki"],
            "Interview Requirement": "Rarely required",
            "Benefits": "Residency, family eligible, EU travel, property ownership",
            "Notes": "Real estate investment required."
        }
    },
    "France": {
        "Investor Visa": {
            "Documents": [
                "Passport",
                "Investment proof: EUR 500,000+",
                "Business plan: Detailed 3-5 year plan",
                "Financial documents: Bank statements, tax returns",
                "Employment creation documentation",
                "Medical certificate",
                "Police clearance"
            ],
            "Investment Required": "EUR 500,000 - EUR 1,000,000+",
            "Processing Time": "60-90 days",
            "Embassy Locations": ["Paris", "Lyon", "Marseille", "Toulouse"],
            "Interview Requirement": "Usually yes",
            "Benefits": "Residency, family eligible, EU citizenship path after 5 years, access to EU market",
            "Notes": "Must create jobs in France. Gateway to EU business market."
        },
        "Startup Visa": {
            "Documents": [
                "Passport",
                "Business plan: Innovative project",
                "Endorsement: From accredited organization",
                "Proof of funds: EUR 30,000+",
                "CV and qualifications",
                "Medical examination"
            ],
            "Investment Required": "EUR 30,000+",
            "Processing Time": "4-8 weeks",
            "Embassy Locations": ["Major cities"],
            "Interview Requirement": "May be required",
            "Benefits": "Fast-track residency, tax benefits for startups, EU market access",
            "Notes": "France supports young entrepreneurs. Best for tech/innovation."
        }
    },
    "Italy": {
        "Investor Visa": {
            "Documents": [
                "Passport",
                "Investment proof: EUR 500,000+",
                "Real estate or business investment documentation",
                "Financial proof",
                "Background check",
                "Medical certificate"
            ],
            "Investment Required": "EUR 500,000 - EUR 2,000,000+",
            "Processing Time": "60-90 days",
            "Embassy Locations": ["Rome", "Milan", "Naples", "Florence"],
            "Interview Requirement": "Usually yes",
            "Benefits": "Residency, family eligible, EU travel, property ownership rights",
            "Notes": "Can invest in real estate, government bonds, or business. Cultural destination."
        },
        "Self-Employment Visa": {
            "Documents": [
                "Passport",
                "Business plan",
                "Financial proof: EUR 10,000+",
                "Educational credentials",
                "Medical examination",
                "Police clearance"
            ],
            "Investment Required": "EUR 10,000+",
            "Processing Time": "8-12 weeks",
            "Embassy Locations": ["Major cities"],
            "Interview Requirement": "Usually yes",
            "Benefits": "Business ownership, residency path, family eligibility",
            "Notes": "Supports artisans and creative professionals."
        }
    },
    "Belgium": {
        "Investor Visa": {
            "Documents": [
                "Passport",
                "Business plan",
                "Investment proof: EUR 100,000+",
                "Financial documents",
                "Background check",
                "Medical certificate"
            ],
            "Investment Required": "EUR 100,000+",
            "Processing Time": "6-8 weeks",
            "Embassy Locations": ["Brussels", "Antwerp", "Ghent"],
            "Interview Requirement": "May be required",
            "Benefits": "Residency, EU base, diamond trading hub access, family eligible",
            "Notes": "Gateway to EU. Good for business startups."
        },
        "Employee Card": {
            "Documents": [
                "Passport",
                "Employment contract",
                "Educational credentials",
                "Medical examination"
            ],
            "Investment Required": "N/A (Employment-based)",
            "Processing Time": "2-4 weeks",
            "Embassy Locations": ["Nationwide"],
            "Interview Requirement": "Usually not required",
            "Benefits": "Work permit, family eligible, EU mobility",
            "Notes": "Fast processing for skilled workers."
        }
    },
    "Japan": {
        "Investor Visa": {
            "Documents": [
                "Passport",
                "Business plan: Detailed operations plan",
                "Company registration documents",
                "Investment proof: JPY 5,000,000+",
                "Financial documents",
                "Background check"
            ],
            "Investment Required": "JPY 5,000,000+ (~USD 35,000)",
            "Processing Time": "4-8 weeks",
            "Embassy Locations": ["Tokyo", "Osaka", "Kyoto"],
            "Interview Requirement": "Usually yes",
            "Benefits": "3-year renewable visa, family eligible, path to permanent residency",
            "Notes": "Must show business viability. Gateway to Asia market."
        },
        "Skilled Professional Visa": {
            "Documents": [
                "Passport",
                "Employment contract",
                "Educational credentials",
                "Medical examination",
                "Police clearance"
            ],
            "Investment Required": "N/A (Employment-based)",
            "Processing Time": "2-4 weeks",
            "Embassy Locations": ["Nationwide"],
            "Interview Requirement": "Rarely required",
            "Benefits": "5-year visa, family eligible, fast-track to permanent residency",
            "Notes": "For specialists in demand sectors."
        }
    },
    "South Korea": {
        "Investor Visa (D-2-1)": {
            "Documents": [
                "Passport",
                "Business plan",
                "Investment proof: KRW 300,000,000+",
                "Company registration",
                "Financial documents",
                "Background check",
                "Medical examination"
            ],
            "Investment Required": "KRW 300,000,000+ (~USD 230,000)",
            "Processing Time": "4-6 weeks",
            "Embassy Locations": ["Seoul", "Busan", "Incheon"],
            "Interview Requirement": "Usually yes",
            "Benefits": "2-year renewable visa, family eligible, tech hub access",
            "Notes": "Great for tech startups. Strong business environment."
        },
        "Foreign Specialist Visa (E-1)": {
            "Documents": [
                "Passport",
                "Employment contract",
                "Educational credentials: Bachelor's degree or higher",
                "Work experience documentation",
                "Medical examination"
            ],
            "Investment Required": "N/A (Employment-based)",
            "Processing Time": "1-2 weeks",
            "Embassy Locations": ["Major cities"],
            "Interview Requirement": "Usually not required",
            "Benefits": "1-3 year visa, renewable, family eligible, tech industry benefits",
            "Notes": "Fast-track for tech professionals."
        }
    },
    "Hong Kong": {
        "Investment Visa (Capital Investment Entrant Scheme)": {
            "Documents": [
                "Passport",
                "Investment proof: HKD 10,000,000+",
                "Business plan",
                "Financial documents",
                "Background check",
                "Medical examination"
            ],
            "Investment Required": "HKD 10,000,000+ (~USD 1,280,000)",
            "Processing Time": "8-12 weeks",
            "Embassy Locations": ["Hong Kong"],
            "Interview Requirement": "Usually yes",
            "Benefits": "Residency, family eligible, tax benefits, Asian business hub",
            "Notes": "One of world's best business environments."
        },
        "General Employment Category": {
            "Documents": [
                "Passport",
                "Employment contract",
                "Educational credentials",
                "Medical examination",
                "Police clearance"
            ],
            "Investment Required": "N/A (Employment-based)",
            "Processing Time": "4-6 weeks",
            "Embassy Locations": ["Hong Kong"],
            "Interview Requirement": "May be required",
            "Benefits": "2-3 year visa, renewable, family eligible, exceptional tax rates",
            "Notes": "For professionals in specialized fields."
        }
    },
    "United Arab Emirates (Abu Dhabi)": {
        "Gold Visa": {
            "Documents": [
                "Passport",
                "Investment proof: AED 2,000,000+",
                "Real estate purchase agreement",
                "Financial documents",
                "Medical examination",
                "Background check",
                "Proof of accommodation"
            ],
            "Investment Required": "AED 2,000,000+ (~USD 545,000)",
            "Processing Time": "2-4 weeks",
            "Embassy Locations": ["Abu Dhabi", "Dubai"],
            "Interview Requirement": "Usually not required",
            "Benefits": "10-year visa, family eligible, real estate ownership, luxury lifestyle",
            "Notes": "Premium investment option. Golden residence program."
        },
        "Green Visa": {
            "Documents": [
                "Passport",
                "Self-employment certificate",
                "Business plan",
                "Proof of funds",
                "Medical examination"
            ],
            "Investment Required": "AED 500,000+ (variable by business type)",
            "Processing Time": "2-3 weeks",
            "Embassy Locations": ["Major emirates"],
            "Interview Requirement": "Usually not required",
            "Benefits": "3-year visa, self-employment, family eligible, renewable",
            "Notes": "New scheme for entrepreneurs and business owners."
        }
    },
    "Brazil": {
        "Temporary Visa (Investor)": {
            "Documents": [
                "Passport",
                "Investment proof: BRL 500,000+",
                "Business plan",
                "Financial documents",
                "Background check",
                "Medical examination"
            ],
            "Investment Required": "BRL 500,000+ (~USD 100,000)",
            "Processing Time": "4-8 weeks",
            "Embassy Locations": ["Brasília", "Rio de Janeiro", "São Paulo"],
            "Interview Requirement": "Usually yes",
            "Benefits": "2-year renewable visa, family eligible, largest economy in LATAM",
            "Notes": "Growing opportunities in tech, agriculture, energy sectors."
        },
        "Digital Visa": {
            "Documents": [
                "Passport",
                "Employment contract or business registration",
                "Proof of income: BRL 3,000+/month",
                "Medical examination"
            ],
            "Investment Required": "N/A (Income requirement)",
            "Processing Time": "2-3 weeks",
            "Embassy Locations": ["Nationwide"],
            "Interview Requirement": "Usually not required",
            "Benefits": "1-year visa, renewable, work from Brazil",
            "Notes": "For remote workers and digital entrepreneurs."
        }
    },
    "Canada (Alberta)": {
        "Self-Employed Farmer/Rancher": {
            "Documents": [
                "Passport",
                "Agricultural experience documentation",
                "Farm/ranch business plan",
                "Financial proof: CAD 50,000+",
                "Medical examination",
                "Police clearance"
            ],
            "Investment Required": "CAD 50,000+",
            "Processing Time": "16-20 months",
            "Embassy Locations": ["Toronto", "Vancouver", "Calgary"],
            "Interview Requirement": "Usually yes",
            "Benefits": "Permanent residency, family eligible, rural development opportunities",
            "Notes": "Canada needs agricultural professionals."
        }
    },
    "Norway": {
        "Business Investor Visa": {
            "Documents": [
                "Passport",
                "Business plan",
                "Investment proof: NOK 500,000+",
                "Financial documents",
                "Qualifications documentation",
                "Medical examination"
            ],
            "Investment Required": "NOK 500,000+ (~USD 47,000)",
            "Processing Time": "8-12 weeks",
            "Embassy Locations": ["Oslo", "Bergen"],
            "Interview Requirement": "Usually yes",
            "Benefits": "Residency, family eligible, access to Nordic market, quality of life",
            "Notes": "High living standards. Strong business ecosystem."
        }
    },
    "Sweden": {
        "Entrepreneur Residence Permit": {
            "Documents": [
                "Passport",
                "Business plan",
                "Investment proof: SEK 100,000+",
                "Financial documents",
                "Educational credentials",
                "Medical examination"
            ],
            "Investment Required": "SEK 100,000+ (~USD 9,500)",
            "Processing Time": "6-8 weeks",
            "Embassy Locations": ["Stockholm", "Gothenburg"],
            "Interview Requirement": "May be required",
            "Benefits": "2-year renewable residence, family eligible, EU access",
            "Notes": "Startup-friendly. Great for tech entrepreneurs."
        }
    },
    "Finland": {
        "Residence Permit (Entrepreneur)": {
            "Documents": [
                "Passport",
                "Business plan",
                "Investment proof: EUR 20,000+",
                "Financial documents",
                "Medical examination"
            ],
            "Investment Required": "EUR 20,000+",
            "Processing Time": "6-8 weeks",
            "Embassy Locations": ["Helsinki"],
            "Interview Requirement": "May be required",
            "Benefits": "Permanent residence possible, family eligible, innovation hub",
            "Notes": "Tech startup leader. Low costs compared to other Nordic countries."
        }
    },
    "Iceland": {
        "Residence Permit (Business Owner)": {
            "Documents": [
                "Passport",
                "Business plan",
                "Investment proof: ISK 10,000,000+",
                "Financial documents",
                "Medical examination",
                "Police clearance"
            ],
            "Investment Required": "ISK 10,000,000+ (~USD 75,000)",
            "Processing Time": "8-12 weeks",
            "Embassy Locations": ["Reykjavik"],
            "Interview Requirement": "Usually yes",
            "Benefits": "Renewable residence, family eligible, EEA market access",
            "Notes": "Unique opportunity in innovative Arctic economy."
        }
    },
    "Luxembourg": {
        "Business Investment Visa": {
            "Documents": [
                "Passport",
                "Business plan",
                "Investment proof: EUR 500,000+",
                "Financial documents",
                "Background check",
                "Medical examination"
            ],
            "Investment Required": "EUR 500,000+",
            "Processing Time": "8-12 weeks",
            "Embassy Locations": ["Luxembourg City"],
            "Interview Requirement": "Usually yes",
            "Benefits": "Residency, family eligible, financial hub, EU access",
            "Notes": "Major financial center. Low tax rates for companies."
        }
    },
    "Cyprus": {
        "Investor Visa": {
            "Documents": [
                "Passport",
                "Investment proof: EUR 300,000+",
                "Real estate or business investment documentation",
                "Financial documents",
                "Background check",
                "Medical certificate"
            ],
            "Investment Required": "EUR 300,000 - EUR 2,000,000+",
            "Processing Time": "60-90 days",
            "Embassy Locations": ["Nicosia", "Limassol"],
            "Interview Requirement": "May be required",
            "Benefits": "Residency, family eligible, EU citizenship after 3 years, Mediterranean lifestyle",
            "Notes": "Can invest in real estate or business. Affordable EU entry."
        }
    },
    "Malta": {
        "Investor Visa": {
            "Documents": [
                "Passport",
                "Investment proof: EUR 250,000+",
                "Property investment or business documentation",
                "Financial documents",
                "Background check",
                "Medical examination"
            ],
            "Investment Required": "EUR 250,000+",
            "Processing Time": "30-60 days",
            "Embassy Locations": ["Valletta"],
            "Interview Requirement": "May be required",
            "Benefits": "Residency, family eligible, EU access, low crime rate, English-speaking",
            "Notes": "Easiest EU residency. English is official language."
        },
        "Individual Investor Programme": {
            "Documents": [
                "Passport",
                "Investment proof: EUR 600,000+",
                "Business plan",
                "Financial documents",
                "Medical examination"
            ],
            "Investment Required": "EUR 600,000+",
            "Processing Time": "4-8 weeks",
            "Embassy Locations": ["Valletta"],
            "Interview Requirement": "May be required",
            "Benefits": "EU citizenship after 12 months, family eligible, passport privilege",
            "Notes": "Fast route to EU citizenship."
        }
    },
    "Turkey": {
        "Residence Permit (ikamet)": {
            "Documents": [
                "Passport",
                "Proof of accommodation",
                "Proof of funds: USD 300+/month",
                "Medical examination",
                "Police clearance"
            ],
            "Investment Required": "N/A (Minimum living cost)",
            "Processing Time": "1-2 weeks",
            "Embassy Locations": ["Ankara", "Istanbul"],
            "Interview Requirement": "Usually not required",
            "Benefits": "Long-term residency, renewable, affordable living, bridge to EU",
            "Notes": "One of cheapest developed countries to reside."
        },
        "Business Visa": {
            "Documents": [
                "Passport",
                "Business plan",
                "Investment proof: USD 250,000+",
                "Company registration",
                "Financial documents",
                "Background check"
            ],
            "Investment Required": "USD 250,000+",
            "Processing Time": "4-6 weeks",
            "Embassy Locations": ["Major cities"],
            "Interview Requirement": "Usually yes",
            "Benefits": "Residency, family eligible, gateway to Middle East and Europe",
            "Notes": "Strategic location. Growing business opportunities."
        }
    },
    "Indonesia": {
        "B211A Visa (Extended Stay)": {
            "Documents": [
                "Passport",
                "Business plan",
                "Investment proof: IDR 25,000,000+",
                "Company registration",
                "Financial documents",
                "Medical examination"
            ],
            "Investment Required": "IDR 25,000,000+ (~USD 1,600)",
            "Processing Time": "2-4 weeks",
            "Embassy Locations": ["Jakarta", "Bali", "Surabaya"],
            "Interview Requirement": "Usually not required",
            "Benefits": "Long-term residency, business ownership, family eligible",
            "Notes": "Cheapest major business residency option worldwide."
        }
    },
    "India": {
        "Overseas Citizen of India (OCI)": {
            "Documents": [
                "Passport",
                "Birth certificate or proof of parentage",
                "Marriage/divorce certificates if applicable",
                "Educational credentials",
                "Police clearance",
                "Medical examination"
            ],
            "Investment Required": "N/A (Fee-based)",
            "Processing Time": "4-6 weeks",
            "Embassy Locations": ["All Indian embassies"],
            "Interview Requirement": "Usually not required",
            "Benefits": "Lifelong multiple entry, family eligible, business opportunities",
            "Notes": "For diaspora and persons of Indian origin."
        },
        "Business Visa": {
            "Documents": [
                "Passport",
                "Business plan",
                "Proof of funds",
                "Company registration",
                "Reference letter from business partner",
                "Medical examination"
            ],
            "Investment Required": "Variable (business-dependent)",
            "Processing Time": "3-5 days",
            "Embassy Locations": ["Nationwide"],
            "Interview Requirement": "Usually not required",
            "Benefits": "Up to 1 year validity, family can visit, business expansion hub",
            "Notes": "Fast-track processing. Huge business opportunities."
        }
    },
    "Kenya": {
        "Investment Visa": {
            "Documents": [
                "Passport",
                "Business plan",
                "Investment proof: USD 50,000+",
                "Company registration",
                "Financial documents",
                "Background check",
                "Medical examination"
            ],
            "Investment Required": "USD 50,000+",
            "Processing Time": "2-3 weeks",
            "Embassy Locations": ["Nairobi", "Mombasa"],
            "Interview Requirement": "Usually yes",
            "Benefits": "Renewable residency, family eligible, African market hub access",
            "Notes": "Gateway to East Africa. Startup ecosystem growing."
        }
    },
    "South Africa": {
        "Business Visa": {
            "Documents": [
                "Passport",
                "Business plan",
                "Proof of funds: ZAR 500,000+",
                "Company registration",
                "Financial documents",
                "Background check",
                "Medical examination"
            ],
            "Investment Required": "ZAR 500,000+ (~USD 28,000)",
            "Processing Time": "4-6 weeks",
            "Embassy Locations": ["Johannesburg", "Cape Town", "Pretoria"],
            "Interview Requirement": "Usually yes",
            "Benefits": "Temporary or permanent residency option, family eligible",
            "Notes": "Most developed economy in Africa. Gateway to African markets."
        },
        "Intra-Company Transfer": {
            "Documents": [
                "Passport",
                "Employment contract",
                "Proof of qualification",
                "Medical examination"
            ],
            "Investment Required": "N/A (Employment-based)",
            "Processing Time": "4-8 weeks",
            "Embassy Locations": ["Major cities"],
            "Interview Requirement": "May be required",
            "Benefits": "Work permit, family eligible, good quality of life",
            "Notes": "For multinational company transfers."
        }
    },
    "Egypt": {
        "Investment Visa": {
            "Documents": [
                "Passport",
                "Business plan",
                "Investment proof: USD 100,000+",
                "Company registration",
                "Financial documents",
                "Background check"
            ],
            "Investment Required": "USD 100,000+",
            "Processing Time": "2-3 weeks",
            "Embassy Locations": ["Cairo", "Alexandria"],
            "Interview Requirement": "Usually yes",
            "Benefits": "Residency, family eligible, gateway to Middle East and Africa",
            "Notes": "Emerging market. Strategic location for business."
        }
    },
    "Pakistan": {
        "Investor Visa": {
            "Documents": [
                "Passport",
                "Business plan",
                "Investment proof: USD 200,000+",
                "Company registration",
                "Financial documents",
                "Background check"
            ],
            "Investment Required": "USD 200,000+",
            "Processing Time": "3-4 weeks",
            "Embassy Locations": ["Islamabad", "Karachi", "Lahore"],
            "Interview Requirement": "Usually yes",
            "Benefits": "Residency, family eligible, growing tech hub",
            "Notes": "Fast-growing economy. Tech talent abundant."
        }
    },
    "Philippines (Additional)": {
        "13A Visa (Spouse/Relative)": {
            "Documents": [
                "Passport",
                "Marriage certificate",
                "Spouse's birth certificate",
                "Bank statements",
                "Medical examination",
                "Police clearance"
            ],
            "Investment Required": "N/A (Relationship-based)",
            "Processing Time": "1-2 weeks",
            "Embassy Locations": ["Manila", "Cebu"],
            "Interview Requirement": "Usually not required",
            "Benefits": "Permanent resident status, multiple entry, family integration",
            "Notes": "For foreigners married to Filipino citizens."
        }
    },
    "Vietnam (Additional)": {
        "Business Visa": {
            "Documents": [
                "Passport",
                "Business plan",
                "Investment proof: USD 100,000+",
                "Company registration",
                "Financial documents",
                "Letter of invitation from Vietnamese company"
            ],
            "Investment Required": "USD 100,000+",
            "Processing Time": "1-2 weeks",
            "Embassy Locations": ["Hanoi", "Ho Chi Minh City"],
            "Interview Requirement": "Usually not required",
            "Benefits": "Long-term residency, business ownership, family eligible",
            "Notes": "One of Asia's fastest-growing economies."
        }
    },
    "Thailand (Additional)": {
        "Long Term Resident Visa (LTR)": {
            "Documents": [
                "Passport",
                "Background information",
                "Proof of income/funds",
                "Medical examination",
                "Insurance: Coverage THB 200,000+"
            ],
            "Investment Required": "Variable by category (USD 80,000+ - USD 1,000,000+)",
            "Processing Time": "2-4 weeks",
            "Embassy Locations": ["Bangkok", "Chiang Mai"],
            "Interview Requirement": "May be required",
            "Benefits": "10-year residency, unlimited family members eligible, tax benefits",
            "Notes": "New premium visa. Excellent value for lifestyle."
        }
    }
}

company_info = {
    "name": "Aidni Global LLP",
    "headquarters": "Mumbai, India",
    "phone": "+919825728291",
    "email": "info@aidniglobal.com",
    "website": "www.aidniglobal.com",
    "expertise": "Global Investment & Business Migration Solutions"
}

def get_investment_info(country, program_type):
    """Retrieve investment program information by country and type"""
    if country in investment_programs:
        if program_type in investment_programs[country]:
            return investment_programs[country][program_type]
    return None

def get_all_countries():
    """Get list of all countries with investment programs"""
    return list(investment_programs.keys())

def get_programs_by_country(country):
    """Get all programs for a specific country"""
    if country in investment_programs:
        return list(investment_programs[country].keys())
    return []

def get_investment_requirement(country, program):
    """Get minimum investment required for a program"""
    try:
        return investment_programs[country][program].get("Investment Required", "N/A")
    except KeyError:
        return "N/A"

def get_processing_time(country, program):
    """Get processing time for a program"""
    try:
        return investment_programs[country][program].get("Processing Time", "N/A")
    except KeyError:
        return "N/A"
