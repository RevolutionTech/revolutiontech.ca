# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basecategory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=75, db_index=True)),
                ('description', models.TextField(help_text=b'Enter valid HTML', null=True, blank=True)),
                ('hero', models.BooleanField(default=False, db_index=True)),
                ('button', models.ManyToManyField(to='basecategory.Button')),
                ('image', models.ManyToManyField(to='basecategory.Image')),
                ('platform', models.ManyToManyField(to='basecategory.Platform')),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'Software',
            },
        ),
    ]
