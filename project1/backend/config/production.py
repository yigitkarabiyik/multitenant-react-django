from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = [
  '',
]

CORS_ALLOWED_ORIGINS = [
    '',  # React uygulamanızın URL'si
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.' + os.getenv('DB_ENGINE'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}


# Email

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST= os.getenv("EMAIL_HOST")
EMAIL_PORT=os.getenv("EMAIL_PORT")
EMAIL_USE_TLS=os.getenv("EMAIL_USE_TLS")
EMAIL_HOST_USER=os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD=os.getenv("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL=os.getenv("DEFAULT_FROM_EMAIL")