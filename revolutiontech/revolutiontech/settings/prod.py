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
    STATIC_ROOT = None
    MEDIA_ROOT = None
    STATICFILES_STORAGE = 'revolutiontech.custom_storages.StaticStorage'
    DEFAULT_FILE_STORAGE = 'revolutiontech.custom_storages.MediaStorage'

    @property
    def AWS_ACCESS_KEY_ID(self):
        return os.environ['REVOLUTIONTECH_AWS_ACCESS_KEY_ID']

    @property
    def AWS_SECRET_ACCESS_KEY(self):
        return os.environ['REVOLUTIONTECH_AWS_SECRET_ACCESS_KEY']

    @property
    def STATIC_URL(self):
        return 'https://{aws_s3}/{static}/'.format(
            aws_s3=self.AWS_S3_CUSTOM_DOMAIN,
            static=self.STATICFILES_LOCATION
        )

    @property
    def MEDIA_URL(self):
        return 'https://{aws_s3}/{media}/'.format(
            aws_s3=self.AWS_S3_CUSTOM_DOMAIN,
            media=self.MEDIAFILES_LOCATION
        )
