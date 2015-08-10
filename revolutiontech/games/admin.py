"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

from django import forms
from django.contrib import admin

from basecategory.admin import ImageInline, ButtonInline, VideoInline, \
    MediaInline, ItemAdmin
from games.models import GameCategory, Game, GameImage, GameButton, \
    GameVideo, GameMedia


class GameImageInline(ImageInline):
    model = GameImage


class GameButtonInline(ButtonInline):
    model = GameButton


class GameVideoInline(VideoInline):
    model = GameVideo


class GameMediaInline(MediaInline):
    model = GameMedia


class GameAdminForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'slug', 'category', 'release_year', 'description', 'platform', 'min_players', 'max_players', 'hero', 'visible',]


class GameAdmin(ItemAdmin):
    list_display = ('name', 'category', 'release_year', 'visible',)
    form = GameAdminForm
    inlines = [GameImageInline, GameButtonInline, GameVideoInline, GameMediaInline,]


admin.site.register(GameCategory)
admin.site.register(Game, GameAdmin)
