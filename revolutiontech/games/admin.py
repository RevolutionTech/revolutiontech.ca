"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

from django.contrib import admin

from games.models import GameCategory, Game


admin.site.register(GameCategory)
admin.site.register(Game)
