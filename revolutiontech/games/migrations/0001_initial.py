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
                ('name', models.CharField(max_length=75)),
                ('img', models.ImageField(null=True, upload_to=basecategory.models.get_img_upload_dir, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('min_players', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('max_players', models.PositiveSmallIntegerField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GameCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'Game categories',
            },
        ),
        migrations.CreateModel(
            name='GamePlatform',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('game', models.ForeignKey(to='games.Game')),
                ('platform', models.ForeignKey(to='basecategory.Platform')),
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
    ]
