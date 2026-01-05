from flask import current_app


def extract_text(image_path):
    """Extract text from image_path using pytesseract if enabled.
    Returns empty string if OCR is disabled or unavailable."""
    if not current_app.config.get('ENABLE_OCR', False):
        return ''
    try:
        from PIL import Image
        import pytesseract
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        print('OCR not available:', e)
        return ''
