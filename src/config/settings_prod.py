# Production settings
import os
from pathlib import Path
import environ

env = environ.Env(
    # default value
    DEBUG=(bool, False),
)

ENV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

environ.Env.read_env(os.path.join(ENV_PATH, ".env.prod"))

SECRET_KEY = env("SECRET_KEY")

# Debug mode
DEBUG = env('DEBUG')

from .settings_base import *

# Allowed hosts
ALLOWED_HOSTS = env("DJANGO_ALLOWED_HOSTS").split(" ")

# Email backend (SMTP)
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", default=True)
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")

DATABASES = {
    "default": {
        "ENGINE": env("SQL_ENGINE"),
        "NAME": env("SQL_DATABASE"),
        "USER": env("SQL_USER"),
        "PASSWORD": env("SQL_PASSWORD"),
        "HOST": "db",
        "PORT": env("SQL_PORT"),
    }
}

# Security settings
SECURE_HSTS_SECONDS = 31536000  # Use HTTP Strict Transport Security (HSTS)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
