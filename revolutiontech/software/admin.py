"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

from django import forms
from django.contrib import admin

from basecategory.admin import ImageInline, ButtonInline, VideoInline, ItemAdmin
from software.models import Software, SoftwareImage, SoftwareButton, SoftwareVideo


class SoftwareImageInline(ImageInline):
    model = SoftwareImage


class SoftwareButtonInline(ButtonInline):
    model = SoftwareButton


class SoftwareVideoInline(VideoInline):
    model = SoftwareVideo


class SoftwareAdminForm(forms.ModelForm):
    class Meta:
        model = Software
        fields = ['name', 'slug', 'release_year', 'description', 'platform', 'hero',]


class SoftwareAdmin(ItemAdmin):
    form = SoftwareAdminForm
    inlines = [SoftwareImageInline, SoftwareButtonInline, SoftwareVideoInline,]


admin.site.register(Software, SoftwareAdmin)
