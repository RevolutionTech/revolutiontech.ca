# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


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
                ('description', models.TextField(help_text=b'Enter valid HTML', null=True, blank=True)),
                ('hero', models.BooleanField(default=False, db_index=True)),
                ('min_players', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('max_players', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('button', models.ManyToManyField(to='basecategory.Button')),
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
        migrations.AddField(
            model_name='game',
            name='category',
            field=models.ForeignKey(to='games.GameCategory'),
        ),
        migrations.AddField(
            model_name='game',
            name='image',
            field=models.ManyToManyField(to='basecategory.Image'),
        ),
        migrations.AddField(
            model_name='game',
            name='platform',
            field=models.ManyToManyField(to='basecategory.Platform'),
        ),
    ]
