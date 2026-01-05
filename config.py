import os

class Config:
    # Set SECRET_KEY in the environment for production (e.g., export SECRET_KEY="your-secret").
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///instance/nexora.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEMPLATES_AUTO_RELOAD = True

    # Uploads & file storage
    # Ensure UPLOAD_FOLDER is an absolute path or a path relative to project root.
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', os.path.abspath(os.path.join(os.path.dirname(__file__), 'uploads')))
    MAX_CONTENT_LENGTH = int(os.environ.get('MAX_CONTENT_LENGTH', 2 * 1024 * 1024))  # default 2MB

    # Email (Flask-Mail) configuration - set these in production
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ('1', 'true', 'yes')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    # Note: File-based sqlite DB concurrent writes can be problematic under heavy load; prefer PostgreSQL in production.

    # Feature flags to control optional heavy dependencies for lightweight deployments
    ENABLE_OCR = os.environ.get('ENABLE_OCR', 'false').lower() in ('1','true','yes')
    ENABLE_WEASYPRINT = os.environ.get('ENABLE_WEASYPRINT', 'false').lower() in ('1','true','yes')
    # If ENABLE_WEASYPRINT is False the app will use a small FPDF fallback for basic PDF needs
