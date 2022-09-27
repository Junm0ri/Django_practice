from .settings_common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6o$_dt(x!j+k6*av0_v7)z8h3i0aa!7s9eey0%8gxe72jz7gb8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
   
    'loggers': {
        'django': {
            'handlers':['console'],
            'level':'INFO',
        },
        'diary': {
            'handlers':['console'],
            'level':'DEBUG',
        },
    },
    
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'dev',
        },
    },
    
    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d',
                '%(message)s'
            ])
        },
    }
}