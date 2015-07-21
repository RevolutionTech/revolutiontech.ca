"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

from django.contrib import admin

from basecategory.models import Image, Platform, Button


admin.site.register(Image)
admin.site.register(Platform)
admin.site.register(Button)
