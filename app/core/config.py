import os
from dotenv import load_dotenv

# Load .env file (but allow production env vars to override)
load_dotenv(override=False)

def _get_int(key, default=None):
    val = os.getenv(key)
    if val is None:
        return default
    try:
        return int(val)
    except (ValueError, TypeError):
        return default

# Email credentials
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp-relay.brevo.com")
SMTP_PORT = _get_int("SMTP_PORT", 587)
EMAIL_USER = os.getenv("EMAIL_USER", "")
EMAIL_PASS = os.getenv("EMAIL_PASS", "")
BREVO_API_KEY = os.getenv("BREVO_API_KEY", "")

ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "cyberarktechnologies245@gmail.com")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "subhash1234")

RAZORPAY_KEY_ID = os.getenv("RAZORPAY_KEY_ID", "")
RAZORPAY_KEY_SECRET = os.getenv("RAZORPAY_KEY_SECRET", "")

AGORA_APP_ID = os.getenv("AGORA_APP_ID", "")
AGORA_APP_CERTIFICATE = os.getenv("AGORA_APP_CERTIFICATE", "")

SECRET_KEY = os.getenv("SECRET_KEY", "edu_tech_platform_secure_jwt_secret_key_2026_project")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", "")