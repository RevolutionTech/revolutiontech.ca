"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

from django.contrib import admin

from ordered_model.admin import OrderedModelAdmin

from basecategory.models import Platform


class ImageInline(admin.TabularInline):
    extra = 2


class ButtonInline(admin.TabularInline):
    extra = 1


class VideoInline(admin.TabularInline):
    extra = 1


class MediaInline(admin.TabularInline):
    extra = 1


class CategoryAdmin(OrderedModelAdmin):
    list_display = ('name', 'move_up_down_links',)


class ItemAdmin(OrderedModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Platform)
