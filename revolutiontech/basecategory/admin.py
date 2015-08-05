"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

from django.contrib import admin

from basecategory.models import Platform


class ImageInline(admin.TabularInline):
    extra = 2


class ButtonInline(admin.TabularInline):
    extra = 1


class VideoInline(admin.TabularInline):
    extra = 1


class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Platform)
