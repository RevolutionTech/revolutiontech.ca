# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import basecategory.models


class Migration(migrations.Migration):

    dependencies = [
        ('basecategory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=75, db_index=True)),
                ('slug', models.SlugField(max_length=75)),
                ('description', models.TextField(help_text=b'Enter valid HTML', null=True, blank=True)),
                ('hero', models.BooleanField(default=False, db_index=True)),
                ('min_players', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('max_players', models.PositiveSmallIntegerField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GameButton',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=30)),
                ('css_class', models.CharField(max_length=15, null=True, verbose_name=b'CSS class', blank=True)),
                ('local_resource', models.FileField(null=True, upload_to=b'download', blank=True)),
                ('external_url', models.URLField(null=True, verbose_name=b'External URL', blank=True)),
                ('game', models.ForeignKey(to='games.Game')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GameCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, db_index=True)),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'Game categories',
            },
        ),
        migrations.CreateModel(
            name='GameImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', models.ImageField(upload_to=basecategory.models.get_img_upload_dir)),
                ('caption', models.TextField()),
                ('game', models.ForeignKey(to='games.Game')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='game',
            name='category',
            field=models.ForeignKey(to='games.GameCategory'),
        ),
        migrations.AddField(
            model_name='game',
            name='platform',
            field=models.ManyToManyField(to='basecategory.Platform'),
        ),
    ]
