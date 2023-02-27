"""
WSGI config for smart_work project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""
import os
from django.core.wsgi import get_wsgi_application
import environ


# Export Django settings env variable
env = environ.Env()
ROOT_DIR = environ.Path(__file__) - 2
READ_DOT_ENV_FILE = env.bool('DJANGO_READ_DOT_ENV_FILE', default=True)

if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(ROOT_DIR.path('.env')))

ENV = 'smart_work.settings.' + env('ENV')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', ENV)

application = get_wsgi_application()
