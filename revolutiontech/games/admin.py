"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

from django import forms
from django.contrib import admin

from basecategory.admin import ImageInline, ButtonInline, ItemAdmin
from games.models import GameCategory, Game, GameImage, GameButton


class GameImageInline(ImageInline):
    model = GameImage


class GameButtonInline(ButtonInline):
    model = GameButton


class GameAdminForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'slug', 'category', 'description', 'platform', 'min_players', 'max_players', 'hero',]


class GameAdmin(ItemAdmin):
    form = GameAdminForm
    inlines = [GameImageInline, GameButtonInline,]


admin.site.register(GameCategory)
admin.site.register(Game, GameAdmin)
