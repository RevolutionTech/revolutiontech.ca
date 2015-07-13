"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

from django.contrib import admin

from productions.models import ProductionCategory, Production


admin.site.register(ProductionCategory)
admin.site.register(Production)
