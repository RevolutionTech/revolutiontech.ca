# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Button',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=30)),
                ('css_class', models.CharField(max_length=15, null=True, blank=True)),
                ('local_resource', models.FileField(null=True, upload_to=b'download', blank=True)),
                ('external_url', models.URLField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('css_class', models.CharField(max_length=15)),
            ],
        ),
    ]
