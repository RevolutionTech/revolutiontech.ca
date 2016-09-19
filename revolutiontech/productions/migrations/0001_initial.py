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
            name='Production',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=75, db_index=True)),
                ('slug', models.SlugField(max_length=75)),
                ('release_year', models.PositiveSmallIntegerField(db_index=True, null=True, verbose_name=b'Year released', blank=True)),
                ('description', models.TextField(help_text=b'Enter valid HTML', null=True, blank=True)),
                ('hero', models.BooleanField(default=False, db_index=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductionButton',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=30)),
                ('css_class', models.CharField(max_length=15, null=True, verbose_name=b'CSS class', blank=True)),
                ('local_resource', models.FileField(null=True, upload_to=b'download', blank=True)),
                ('external_url', models.URLField(null=True, verbose_name=b'External URL', blank=True)),
                ('production', models.ForeignKey(to='productions.Production')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductionCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, db_index=True)),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'Production categories',
            },
        ),
        migrations.CreateModel(
            name='ProductionImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', models.ImageField(upload_to=b'img')),
                ('caption', models.TextField(null=True, blank=True)),
                ('production', models.ForeignKey(to='productions.Production')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='production',
            name='category',
            field=models.ForeignKey(to='productions.ProductionCategory'),
        ),
        migrations.AddField(
            model_name='production',
            name='platform',
            field=models.ManyToManyField(to='basecategory.Platform'),
        ),
    ]
