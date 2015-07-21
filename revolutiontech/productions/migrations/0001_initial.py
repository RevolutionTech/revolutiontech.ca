# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


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
                ('description', models.TextField(help_text=b'Enter valid HTML', null=True, blank=True)),
                ('hero', models.BooleanField(default=False, db_index=True)),
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
                ('name', models.CharField(max_length=50, db_index=True)),
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
            name='image',
            field=models.ManyToManyField(to='basecategory.Image'),
        ),
        migrations.AddField(
            model_name='production',
            name='platform',
            field=models.ManyToManyField(to='basecategory.Platform'),
        ),
    ]
