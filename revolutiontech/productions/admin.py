"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

from django import forms
from django.contrib import admin

from productions.models import ProductionCategory, Production


class ProductionAdminForm(forms.ModelForm):
    class Meta:
        model = Production
        fields = ['name', 'category', 'img', 'description', 'platform', 'button', 'hero',]


class ProductionAdmin(admin.ModelAdmin):
    form = ProductionAdminForm


admin.site.register(ProductionCategory)
admin.site.register(Production, ProductionAdmin)
