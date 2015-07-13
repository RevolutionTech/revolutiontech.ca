"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=50)

    class Meta:
        abstract = True


def get_img_upload_dir(item, filename):
    return "img/{item_type}".format(
        item_type=item.Meta.verbose_name_plural.lower()
    )


class Item(models.Model):

    name = models.CharField(max_length=75)
    img = models.ImageField(upload_to=get_img_upload_dir, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name


class Platform(models.Model):

    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to="img/platform", verbose_name='Platform')

    def __unicode__(self):
        return self.name


class ItemPlatform(models.Model):

    platform = models.ForeignKey(Platform)

    class Meta:
        abstract = True
