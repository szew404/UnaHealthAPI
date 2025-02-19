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

SECRET_KEY = env("DJANGO_SECRET_KEY")

# Debug mode
DEBUG = env("DEBUG")

from .settings_base import *

# Allowed hosts
ALLOWED_HOSTS = env("DJANGO_ALLOWED_HOSTS").split(" ")

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

# CELERY Setup
CELERY_BROKER_URL = env("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND")
