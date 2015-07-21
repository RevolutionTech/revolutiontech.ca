# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import basecategory.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Button',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=30)),
                ('css_class', models.CharField(max_length=15, null=True, verbose_name=b'CSS class', blank=True)),
                ('local_resource', models.FileField(null=True, upload_to=b'download', blank=True)),
                ('external_url', models.URLField(null=True, verbose_name=b'External URL', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', models.ImageField(upload_to=basecategory.models.get_img_upload_dir)),
                ('caption', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('css_class', models.CharField(max_length=15, verbose_name=b'CSS class')),
            ],
        ),
    ]
