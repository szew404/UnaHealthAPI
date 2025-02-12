# Development settings
import os
from pathlib import Path
import environ

env = environ.Env(
    # default value
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(str, "*"),
    SQL_ENGINE=(str, "django.db.backends.sqlite3"),
    SQL_DATABASE=(str, "db.sqlite3"),
    SQL_USER=(str, "user"),
    SQL_PASSWORD=(str, "password"),
    SQL_HOST=(str, "localhost"),
    SQL_PORT=(str, "5432"),
)

ENV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

environ.Env.read_env(os.path.join(ENV_PATH, ".env.dev"))

SECRET_KEY = env("DJANGO_SECRET_KEY")

# Debug mode
DEBUG = env("DEBUG")

from .settings_base import *

# Allowed hosts
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# Email settings for development (console backend)
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Database configuration
DATABASES = {
    "default": {
        "ENGINE": env("SQL_ENGINE"),
        "NAME": env("SQL_DATABASE"),
        "USER": env("SQL_USER"),
        "PASSWORD": env("SQL_PASSWORD"),
        "HOST": env("SQL_HOST"),
        "PORT": env("SQL_PORT"),
    }
}
