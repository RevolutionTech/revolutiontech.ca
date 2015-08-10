"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

from django.db import models

from basecategory.models import Category, Image, Button, Video, Media, \
    Item


class ProductionCategory(Category):

    class Meta(Category.Meta):
        verbose_name_plural = "Production categories"


class Production(Item):

    category = models.ForeignKey(ProductionCategory)


class ProductionImage(Image):

    production = models.ForeignKey(Production)


class ProductionButton(Button):

    production = models.ForeignKey(Production)


class ProductionVideo(Video):

    production = models.ForeignKey(Production)


class ProductionMedia(Media):

    production = models.ForeignKey(Production)

    class Meta(Media.Meta):
        verbose_name_plural = "Production media"
