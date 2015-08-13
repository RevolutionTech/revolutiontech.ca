# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_gamevideo'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameMedia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('media', models.FileField(upload_to=b'download/media')),
                ('game', models.ForeignKey(to='games.Game')),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'Game media',
            },
        ),
    ]