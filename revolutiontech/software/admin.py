"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

from django import forms
from django.contrib import admin

from basecategory.admin import ImageInline, ButtonInline, ItemAdmin
from software.models import Software, SoftwareImage, SoftwareButton


class SoftwareImageInline(ImageInline):
    model = SoftwareImage


class SoftwareButtonInline(ButtonInline):
    model = SoftwareButton


class SoftwareAdminForm(forms.ModelForm):
    class Meta:
        model = Software
        #fields = ['name', 'slug', 'softwareimage', 'description', 'platform', 'softwarebutton', 'hero',]
        fields = ['name', 'slug', 'description', 'platform', 'hero',]


class SoftwareAdmin(ItemAdmin):
    form = SoftwareAdminForm
    inlines = [SoftwareImageInline, SoftwareButtonInline,]


admin.site.register(Software, SoftwareAdmin)
