# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0002_productionvideo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductionMedia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('media', models.FileField(upload_to=b'download/media')),
                ('production', models.ForeignKey(to='productions.Production')),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'Production media',
            },
        ),
    ]
