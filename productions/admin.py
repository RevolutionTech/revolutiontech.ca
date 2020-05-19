"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

from django import forms
from django.contrib import admin

from basecategory.admin import (
    ButtonInline,
    CategoryAdmin,
    ImageInline,
    ItemAdmin,
    MediaInline,
    VideoInline,
)
from productions.models import (
    Production,
    ProductionButton,
    ProductionCategory,
    ProductionImage,
    ProductionMedia,
    ProductionVideo,
)


class ProductionImageInline(ImageInline):
    model = ProductionImage


class ProductionButtonInline(ButtonInline):
    model = ProductionButton


class ProductionVideoInline(VideoInline):
    model = ProductionVideo


class ProductionMediaInline(MediaInline):
    model = ProductionMedia


class ProductionAdminForm(forms.ModelForm):
    class Meta:
        model = Production
        fields = [
            "name",
            "slug",
            "category",
            "release_year",
            "description",
            "platform",
            "hero",
            "visible",
        ]


class ProductionAdmin(ItemAdmin):
    list_display = ("name", "category", "release_year", "visible", "move_up_down_links")
    form = ProductionAdminForm
    inlines = [
        ProductionImageInline,
        ProductionButtonInline,
        ProductionVideoInline,
        ProductionMediaInline,
    ]


admin.site.register(ProductionCategory, CategoryAdmin)
admin.site.register(Production, ProductionAdmin)
