#!/usr/bin/env python
"""
Migration script to initialize residency platform database
Run this after updating models.py
"""

from app import app, db

def init_database():
    """Initialize the database with new models"""
    with app.app_context():
        # Create all tables
        db.create_all()
        print("✓ Database tables created successfully")
        
        # Initialize with sample data (optional)
        from models import ResidencyConsultant, ResidencyBlogPost
        
        # Add sample consultant if none exist
        if ResidencyConsultant.query.count() == 0:
            sample_consultant = ResidencyConsultant(
                name="John Smith",
                email="john@example.com",
                phone="+1-555-0100",
                specializations="Portugal, Malta, Greece",
                experience_years=15,
                bio="Immigration expert with 15 years of experience helping clients obtain residency worldwide.",
                hourly_rate=150.0,
                verified=True,
                rating=4.9,
                total_reviews=47
            )
            db.session.add(sample_consultant)
            db.session.commit()
            print("✓ Sample consultant created")
        
        # Add sample blog post if none exist
        if ResidencyBlogPost.query.count() == 0:
            sample_post = ResidencyBlogPost(
                title="Guide to Portugal Golden Visa Program",
                slug="portugal-golden-visa-guide",
                content="<h2>Overview</h2><p>The Portugal Golden Visa is one of Europe's most popular investment residency programs...</p>",
                excerpt="Complete guide to Portugal's Golden Visa program for real estate investors.",
                category="Guide",
                countries="Portugal",
                author="Aidni Global Team",
                published=True,
                views=150
            )
            db.session.add(sample_post)
            db.session.commit()
            print("✓ Sample blog post created")
        
        print("\n✓ Database initialization complete!")
        print("You can now use the Nexora platform.")

if __name__ == '__main__':
    init_database()
