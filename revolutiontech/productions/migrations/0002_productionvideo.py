# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductionVideo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('youtube_url', models.URLField(verbose_name=b'YouTube URL')),
                ('production', models.ForeignKey(to='productions.Production')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
