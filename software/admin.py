"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

from django import forms
from django.contrib import admin

from basecategory.admin import ImageInline, ButtonInline, VideoInline, \
    MediaInline, ItemAdmin
from software.models import Software, SoftwareImage, SoftwareButton, \
    SoftwareVideo, SoftwareMedia


class SoftwareImageInline(ImageInline):
    model = SoftwareImage


class SoftwareButtonInline(ButtonInline):
    model = SoftwareButton


class SoftwareVideoInline(VideoInline):
    model = SoftwareVideo


class SoftwareMediaInline(MediaInline):
    model = SoftwareMedia


class SoftwareAdminForm(forms.ModelForm):
    class Meta:
        model = Software
        fields = ['name', 'slug', 'release_year', 'description', 'platform', 'hero', 'visible',]


class SoftwareAdmin(ItemAdmin):
    list_display = ('name', 'release_year', 'visible', 'move_up_down_links',)
    form = SoftwareAdminForm
    inlines = [SoftwareImageInline, SoftwareButtonInline, SoftwareVideoInline, SoftwareMediaInline,]


admin.site.register(Software, SoftwareAdmin)
