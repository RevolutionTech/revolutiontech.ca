"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

from django import forms
from django.contrib import admin

from games.models import GameCategory, Game


class GameAdminForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'category', 'img', 'description', 'platform', 'min_players', 'max_players', 'button', 'hero',]


class GameAdmin(admin.ModelAdmin):
    form = GameAdminForm


admin.site.register(GameCategory)
admin.site.register(Game, GameAdmin)
