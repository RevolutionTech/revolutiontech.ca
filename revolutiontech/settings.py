"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

import os

from configurations import Configuration, values


def aws_s3_bucket_url(settings_class, bucket_name_settings):
    bucket_name = getattr(settings_class, bucket_name_settings, "")
    if bucket_name:
        return f"https://{bucket_name}.s3.amazonaws.com"
    return ""


class BaseConfig(Configuration):

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    SECRET_KEY = values.SecretValue(environ_prefix="REVOLUTIONTECH")
    DEBUG = True
    ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

    # Application definition
    INSTALLED_APPS = (
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "sorl.thumbnail",
        "ordered_model",
        "django_s3_sqlite",
        "django_s3_storage",
        "basecategory",
        "games",
        "productions",
        "software",
    )
    MIDDLEWARE = (
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
        "django.middleware.security.SecurityMiddleware",
    )
    ROOT_URLCONF = "revolutiontech.urls"

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ]
            },
        }
    ]
    WSGI_APPLICATION = "revolutiontech.wsgi.application"

    # Cache and Database
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
            "LOCATION": "127.0.0.1:11211",
        }
    }
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }

    # Internationalization
    TIME_ZONE = "UTC"
    USE_L10N = True
    USE_TZ = True

    # Static files (CSS, JavaScript, Images) and Media
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")
    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
    STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
    AWS_S3_KEY_PREFIX = "media"
    AWS_S3_KEY_PREFIX_STATIC = "static"
    AWS_S3_BUCKET_AUTH = False
    AWS_S3_MAX_AGE_SECONDS = 60 * 60 * 24 * 365  # 1 year

    @property
    def MEDIA_URL(self):
        return "{aws_s3}/{media}/".format(
            aws_s3=aws_s3_bucket_url(self, "AWS_S3_BUCKET_NAME"),
            media=self.AWS_S3_KEY_PREFIX,
        )

    @property
    def STATIC_URL(self):
        return "{aws_s3}/{static}/".format(
            aws_s3=aws_s3_bucket_url(self, "AWS_S3_BUCKET_NAME_STATIC"),
            static=self.AWS_S3_KEY_PREFIX_STATIC,
        )


class ProdConfig(BaseConfig):

    DEBUG = False
    ALLOWED_HOSTS = [
        "localhost",
        "127.0.0.1",
        "revolutiontech.ca",
        "www.revolutiontech.ca",
    ]

    # Database
    DATABASES = {
        "default": {
            "ENGINE": "django_s3_sqlite",
            "NAME": "db.sqlite3",
            "BUCKET": "revolutiontech-sqlite3",
        }
    }

    # Static and media files
    DEFAULT_FILE_STORAGE = "django_s3_storage.storage.S3Storage"
    STATICFILES_STORAGE = "django_s3_storage.storage.StaticS3Storage"
    AWS_S3_BUCKET_NAME = "revolutiontech"
    AWS_S3_BUCKET_NAME_STATIC = AWS_S3_BUCKET_NAME
    AWS_ACCESS_KEY_ID = values.SecretValue(environ_prefix="REVOLUTIONTECH")
    AWS_SECRET_ACCESS_KEY = values.SecretValue(environ_prefix="REVOLUTIONTECH")
