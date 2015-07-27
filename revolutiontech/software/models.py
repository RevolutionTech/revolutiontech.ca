"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

from django.db import models

from basecategory.models import Image, Button, Item


class Software(Item):

    class Meta(Item.Meta):
        verbose_name_plural = "Software"


class SoftwareImage(Image):

    software = models.ForeignKey(Software)


class SoftwareButton(Button):

    software = models.ForeignKey(Software)
