from .base import *

DEBUG = env.bool('DEBUG', True)

ALLOWED_HOSTS = ['*']

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'assets'),
]
