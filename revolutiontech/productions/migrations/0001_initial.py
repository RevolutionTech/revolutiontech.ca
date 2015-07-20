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
                ('name', models.CharField(max_length=75)),
                ('img', models.ImageField(null=True, upload_to=basecategory.models.get_img_upload_dir, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('hero', models.BooleanField(default=False)),
                ('button', models.ManyToManyField(to='basecategory.Button')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductionCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'Production categories',
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
