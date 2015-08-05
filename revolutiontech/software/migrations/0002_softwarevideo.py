# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoftwareVideo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('youtube_url', models.URLField(verbose_name=b'YouTube URL')),
                ('software', models.ForeignKey(to='software.Software')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
