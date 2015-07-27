"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

from django.db import models

from basecategory.models import Category, Image, Button, Item


class GameCategory(Category):

    class Meta(Category.Meta):
        verbose_name_plural = "Game categories"


class Game(Item):

    category = models.ForeignKey(GameCategory)
    min_players = models.PositiveSmallIntegerField(null=True, blank=True)
    max_players = models.PositiveSmallIntegerField(null=True, blank=True)


class GameImage(Image):

    game = models.ForeignKey(Game)


class GameButton(Button):

    game = models.ForeignKey(Game)
