"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

import random
import re

from django.db import models
from django.urls import reverse

from ordered_model.models import OrderedModel


class Category(OrderedModel):

    name = models.CharField(max_length=50, db_index=True)

    class Meta(OrderedModel.Meta):
        abstract = True

    def __unicode__(self):
        return self.name


class Image(models.Model):

    img = models.ImageField(upload_to='img')
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

    def link_is_external(self):
        return self.external_url and not self.local_resource


class Video(models.Model):

    title = models.CharField(max_length=30)
    youtube_url = models.URLField(verbose_name='YouTube URL')

    class Meta:
        abstract = True

    def __unicode__(self):
        return "{title}: {url}".format(
            title=self.title,
            url=self.youtube_url
        )

    def youtube_video_code_and_params(self):
        video_code_and_params_str = self.youtube_url.split('/watch?v=')[1]
        video_code_and_params_list = video_code_and_params_str.split('&')
        video_code, params = video_code_and_params_list[0], video_code_and_params_list[1:]
        return video_code, '&'.join(params)

    def youtube_embed_url(self):
        video_code, url_params = self.youtube_video_code_and_params()
        url = "https://www.youtube.com/embed/{v}".format(v=video_code)

        if url_params:
            url += "?{params}".format(params=url_params)
        return url


class Media(models.Model):

    title = models.CharField(max_length=30)
    media = models.FileField(upload_to="download/media")

    class Meta:
        abstract = True
        verbose_name_plural = "Media"

    def __unicode__(self):
        return "{title}: {filename}".format(
            title=self.title,
            filename=self.media
        )


class Item(OrderedModel):

    name = models.CharField(max_length=75, db_index=True)
    slug = models.SlugField(max_length=75, db_index=True)
    release_year = models.PositiveSmallIntegerField(null=True, blank=True, db_index=True, verbose_name="Year released")
    description = models.TextField(null=True, blank=True, help_text="Enter valid HTML")
    platform = models.ManyToManyField(Platform)
    hero = models.BooleanField(default=False, db_index=True)
    visible = models.BooleanField(default=True, db_index=True)

    class Meta(OrderedModel.Meta):
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
        buttons = self.button_all()
        try:
            return buttons[0]
        except IndexError:
            pass

    def button_rest(self):
        return self.button_all()[1:]

    def video_all(self):
        video_model_set_name = "{item_type}video_set".format(item_type=self._meta.model_name)
        return getattr(self, video_model_set_name).all().order_by('id')

    def media_all(self):
        media_model_set_name = "{item_type}media_set".format(item_type=self._meta.model_name)
        return getattr(self, media_model_set_name).all().order_by('id')

    def url(self):
        item_type = self._meta.verbose_name_plural.lower()
        return reverse(
            '{item_type}:item_details'.format(item_type=item_type),
            kwargs={'slug': self.slug}
        )

    def youtube_only(self):
        platforms = self.platform.all()
        return len(platforms) == 1 and platforms[0].name == 'YouTube'
