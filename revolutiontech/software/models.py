"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

from django.db import models

from basecategory.models import Item, ItemPlatform


class Software(Item):

    class Meta(Item.Meta):
        verbose_name_plural = "Software"


class SoftwarePlatform(ItemPlatform):

    software = models.ForeignKey(Software)

    def __unicode__(self):
        return "({software}, {platform})".format(software=self.software, platform=self.platform)
