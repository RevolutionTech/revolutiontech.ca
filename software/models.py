"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

from django.db import models

from basecategory.models import Button, Image, Item, Media, Video


class Software(Item):
    class Meta(Item.Meta):
        verbose_name_plural = "Software"


class SoftwareImage(Image):

    software = models.ForeignKey(Software, on_delete=models.CASCADE)


class SoftwareButton(Button):

    software = models.ForeignKey(Software, on_delete=models.CASCADE)


class SoftwareVideo(Video):

    software = models.ForeignKey(Software, on_delete=models.CASCADE)


class SoftwareMedia(Media):

    software = models.ForeignKey(Software, on_delete=models.CASCADE)

    class Meta(Media.Meta):
        verbose_name_plural = "Software media"
