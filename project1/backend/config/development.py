from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY= os.getenv('SECRET_KEY')

ALLOWED_HOSTS = [
  '127.0.0.1',
  'localhost',
  os.getenv("ALLOWED_HOST"),
  ]

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',  # React uygulamanızın URL'si
    'http://127.0.0.1:3000',  # React uygulamanızın URL'si
]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Email

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'