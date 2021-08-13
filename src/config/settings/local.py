from .base import *  #noqa

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.str('POSTGRES_DB', 'trello_local'),
        'USER': env.str('POSTGRES_USER', 'trello'),
        'PASSWORD': env.str('POSTGRES_PASSWORD', 'trello'),
        'HOST': env.str('DB_HOST', 'postgres'),
        'PORT': env.int('DB_PORT', 5432),
    }
}
