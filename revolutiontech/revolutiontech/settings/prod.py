"""
:Created: 11 November 2017
:Author: Lucas Connors

"""

import os

from revolutiontech.settings.base import BaseSettings


class ProdSettings(BaseSettings):

    DEBUG = False
    ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'revolutiontech.ca', 'www.revolutiontech.ca']

    # Static and media files
    DEFAULT_FILE_STORAGE = 'django_s3_storage.storage.S3Storage'
    STATICFILES_STORAGE = 'django_s3_storage.storage.StaticS3Storage'
    AWS_S3_BUCKET_NAME = 'revolutiontech'
    AWS_S3_BUCKET_NAME_STATIC = AWS_S3_BUCKET_NAME

    @property
    def AWS_ACCESS_KEY_ID(self):
        return os.environ['REVOLUTIONTECH_AWS_ACCESS_KEY_ID']

    @property
    def AWS_SECRET_ACCESS_KEY(self):
        return os.environ['REVOLUTIONTECH_AWS_SECRET_ACCESS_KEY']
