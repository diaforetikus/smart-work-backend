from .base import *

DEBUG = env.bool('DEBUG', False)

ALLOWED_HOSTS = ['*']

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')


DATABASES = {
    'default': env.db('DATABASE_URL', default='postgres:///django_quick_start'),
}

DATABASES['default']['ATOMIC_REQUESTS'] = True

STATIC_ROOT = os.path.join(BASE_DIR, "assets")

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
