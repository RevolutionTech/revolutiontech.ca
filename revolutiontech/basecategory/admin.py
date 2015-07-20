"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

from django.contrib import admin

from basecategory.models import Platform, Button


admin.site.register(Platform)
admin.site.register(Button)
