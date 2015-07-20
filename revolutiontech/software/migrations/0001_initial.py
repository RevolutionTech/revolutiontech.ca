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
            name='Software',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=75)),
                ('img', models.ImageField(null=True, upload_to=basecategory.models.get_img_upload_dir, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('hero', models.BooleanField(default=False)),
                ('button', models.ManyToManyField(to='basecategory.Button')),
                ('platform', models.ManyToManyField(to='basecategory.Platform')),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'Software',
            },
        ),
    ]
