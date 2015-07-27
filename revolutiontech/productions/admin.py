"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

from django import forms
from django.contrib import admin

from basecategory.admin import ImageInline, ButtonInline, ItemAdmin
from productions.models import ProductionCategory, Production, \
    ProductionImage, ProductionButton


class ProductionImageInline(ImageInline):
    model = ProductionImage


class ProductionButtonInline(ButtonInline):
    model = ProductionButton


class ProductionAdminForm(forms.ModelForm):
    class Meta:
        model = Production
        #fields = ['name', 'slug', 'category', 'productionimage', 'description', 'platform', 'productionbutton', 'hero',]
        fields = ['name', 'slug', 'category', 'description', 'platform', 'hero',]


class ProductionAdmin(ItemAdmin):
    form = ProductionAdminForm
    inlines = [ProductionImageInline, ProductionButtonInline,]


admin.site.register(ProductionCategory)
admin.site.register(Production, ProductionAdmin)
