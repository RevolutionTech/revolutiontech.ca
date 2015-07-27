"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

from django.db import models

from basecategory.models import Category, Image, Button, Item


class ProductionCategory(Category):

    class Meta(Category.Meta):
        verbose_name_plural = "Production categories"


class Production(Item):

    category = models.ForeignKey(ProductionCategory)


class ProductionImage(Image):

    production = models.ForeignKey(Production)


class ProductionButton(Button):

    production = models.ForeignKey(Production)
