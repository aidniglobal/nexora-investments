# Deploying to PythonAnywhere (Quick Guide)

1. Create & activate a virtualenv on PythonAnywhere (match your Python version):

    mkvirtualenv --python=/usr/bin/python3.X nexora-venv

2. Clone the repository and install dependencies:

    git clone https://github.com/youruser/nexora-visa-assistant.git
    cd nexora-visa-assistant
    workon nexora-venv
    pip install -r requirements.txt

   Note: Packages like WeasyPrint, OpenCV, and pytesseract may require system libraries not available on PythonAnywhere; consider removing or using pure-Python fallbacks if needed.

3. Configure environment variables in the PythonAnywhere Web -> Environment Variables section:

    SECRET_KEY, DATABASE_URL (optional), UPLOAD_FOLDER, MAIL_USERNAME, MAIL_PASSWORD, MAIL_SERVER, MAIL_PORT

4. Create runtime directories and initialize DB:

    mkdir -p instance uploads
    flask db upgrade

5. Configure the WSGI file (PythonAnywhere Web tab) — add at top:

    import sys, os
    path = '/home/<youruser>/nexora-visa-assistant'
    if path not in sys.path:
        sys.path.insert(0, path)

    from app import app as application

6. Static files: set the Static files mapping in Web tab to serve `/static/` from `/home/<youruser>/nexora-visa-assistant/static/`.

7. Reload the web app and check logs on PythonAnywhere if anything fails.

8. Notes:
   - If you need background workers (Celery) or heavy system deps, use a separate worker host or a paid environment that provides those system libraries.
   - For sending mail with Gmail, use an app password or a dedicated SMTP provider (SendGrid, Mailgun) for reliable delivery.
