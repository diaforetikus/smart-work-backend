import os
from importlib.util import find_spec
from django.apps import apps
from django.conf import settings
from django.core.wsgi import get_wsgi_application
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.staticfiles import StaticFiles
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

apps.populate(settings.INSTALLED_APPS)

# This endpoint imports should be placed below the settings env declaration
# Otherwise, django will throw a configure() settings error
from smart_work.api_router import router as api_router

# Get the Django WSGI application we are working with
application = get_wsgi_application()

# This can be done without the function, but making it functional
# tidies the entire code and encourages modularity

def get_application() -> FastAPI:
	# Main Fast API application
	app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json", debug=settings.DEBUG)

	# Set all CORS enabled origins
	app.add_middleware(CORSMiddleware, allow_origins = [str(origin) for origin in settings.ALLOWED_HOSTS] or ["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"],)

	# Include all api endpoints
	app.include_router(api_router, prefix=settings.API_V1_STR)

	app.mount("/assets", StaticFiles(directory="frontend/dist/assets"), name="assets")

	# Mounts an independent web URL for Django WSGI application
	app.mount(f"{settings.WSGI_APP_URL}", WSGIMiddleware(application))

	return app

app = get_application()