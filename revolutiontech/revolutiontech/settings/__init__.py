"""
Django settings for revolutiontech project.
:Created: 12 July 2015
:Author: Lucas Connors

"""

import os

from cbsettings import switcher

from revolutiontech.settings.base import BaseSettings
from revolutiontech.settings.prod import ProdSettings


api_gateway_stage = os.environ.get('STAGE', 'dev')
switcher.register(BaseSettings, api_gateway_stage == 'dev')
switcher.register(ProdSettings, api_gateway_stage == 'production')
