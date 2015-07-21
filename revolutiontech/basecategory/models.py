"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

import random

from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=50, db_index=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name


def get_item_type(item):
    return item._meta.verbose_name_plural.lower()


def get_img_upload_dir(item, filename):
    return "img/{item_type}/{filename}".format(
        item_type=get_item_type(item),
        filename=filename
    )


class Image(models.Model):

    img = models.ImageField(upload_to=get_img_upload_dir)
    caption = models.TextField()

    def __unicode__(self):
        return self.caption[:40]


class Platform(models.Model):

    name = models.CharField(max_length=20)
    css_class = models.CharField(max_length=15, verbose_name='CSS class')

    def __unicode__(self):
        return self.name


class Button(models.Model):

    text = models.CharField(max_length=30)
    css_class = models.CharField(max_length=15, null=True, blank=True, verbose_name='CSS class')
    local_resource = models.FileField(upload_to="download", null=True, blank=True)
    external_url = models.URLField(null=True, blank=True, verbose_name='External URL')

    def __unicode__(self):
        return "{text}: {resource}".format(
            text=self.text,
            resource=self.local_resource.name or self.external_url
        )

    def link(self):
        if self.local_resource:
            return self.local_resource.url
        elif self.external_url:
            return self.external_url
        else:
            return "#"


class Item(models.Model):

    name = models.CharField(max_length=75, db_index=True)
    image = models.ManyToManyField(Image)
    description = models.TextField(null=True, blank=True, help_text="Enter valid HTML")
    platform = models.ManyToManyField(Platform)
    button = models.ManyToManyField(Button)
    hero = models.BooleanField(default=False, db_index=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name

    def random_image(self):
        return random.choice(self.image.all())

    def description_first_letter(self):
        return self.description[0]

    def description_rest(self):
        return self.description[1:]

    def button_main(self):
        return self.button.all()[0]

    def button_rest(self):
        return self.button.all()[1:]
