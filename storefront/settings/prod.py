from .common import *
import os
import dj_database_url

SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = False

ALLOWED_HOSTS = ['gurjika-prod-0bde9ea4defe.herokuapp.com']



DATABASES = {
    'default': dj_database_url.config()
}


REDIS_URL = os.environ['REDIS_URL']

CELERY_BROKER_URL = REDIS_URL


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
