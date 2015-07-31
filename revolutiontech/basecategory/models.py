"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

import random
import re

from django.core.urlresolvers import reverse
from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=50, db_index=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name


def get_img_upload_dir(item, filename):
    return "img/{filename}".format(filename=filename)


class Image(models.Model):

    img = models.ImageField(upload_to=get_img_upload_dir)
    caption = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True

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

    class Meta:
        abstract = True

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
    slug = models.SlugField(max_length=75, db_index=True)
    release_year = models.PositiveSmallIntegerField(null=True, blank=True, db_index=True, verbose_name="Year released")
    description = models.TextField(null=True, blank=True, help_text="Enter valid HTML")
    platform = models.ManyToManyField(Platform)
    hero = models.BooleanField(default=False, db_index=True)

    class Meta:
        abstract = True

    @staticmethod
    def first_real_char_index(string):
        return re.match(r"(<\w*>)*", string).end()

    def __unicode__(self):
        return self.name

    def description_first_letter(self):
        index = self.first_real_char_index(self.description)
        return self.description[index]

    def description_rest(self):
        split_index = self.first_real_char_index(self.description)
        return self.description[:split_index] + self.description[split_index+1:]

    def image_all(self):
        image_model_set_name = "{item_type}image_set".format(item_type=self._meta.model_name)
        return getattr(self, image_model_set_name).all().order_by('id')

    def image_random(self):
        return random.choice(self.image_all())

    def button_all(self):
        button_model_set_name = "{item_type}button_set".format(item_type=self._meta.model_name)
        return getattr(self, button_model_set_name).all().order_by('id')

    def button_main(self):
        return self.button_all()[0]

    def button_rest(self):
        return self.button_all()[1:]

    def url(self):
        item_type = self._meta.verbose_name_plural.lower()
        return reverse(
            '{item_type}:item_details'.format(item_type=item_type),
            kwargs={'slug': self.slug}
        )
