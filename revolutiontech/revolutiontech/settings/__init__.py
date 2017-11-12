"""
Django settings for revolutiontech project.
:Created: 12 July 2015
:Author: Lucas Connors

"""

import os

from cbsettings import switcher

from revolutiontech.settings.base import BaseSettings
from revolutiontech.settings.prod import ProdSettings


revolutiontech_env = os.environ.get('REVOLUTIONTECH_ENV', 'DEV')
switcher.register(BaseSettings, revolutiontech_env == 'DEV')
switcher.register(ProdSettings, revolutiontech_env == 'PROD')
