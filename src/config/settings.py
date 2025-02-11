# Django settings for unahealthapi project.

# Generated using djpro 0.0.1.

# For more information on this file, see
# https://docs.djangoproject.com/en/5.0/topics/settings/

# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/5.0/ref/settings/

import os
import environ

ENV_PATH_CONF = os.path.dirname(os.path.abspath(__file__))

environ.Env.read_env(os.path.join(ENV_PATH_CONF, ".env.conf"))

ENVIRONMENT = os.getenv("DJANGO_ENV", "dev")

if ENVIRONMENT == "prod":
    from .settings_prod import *
else:
    from .settings_dev import *
