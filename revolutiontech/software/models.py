"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

from django.db import models

from basecategory.models import Item


class Software(Item):

    class Meta(Item.Meta):
        verbose_name_plural = "Software"
