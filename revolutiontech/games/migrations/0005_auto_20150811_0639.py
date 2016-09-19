# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_game_visible'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'ordering': ('order',)},
        ),
        migrations.AlterModelOptions(
            name='gamecategory',
            options={'ordering': ('order',), 'verbose_name_plural': 'Game categories'},
        ),
        migrations.AddField(
            model_name='game',
            name='order',
            field=models.PositiveIntegerField(default=0, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gamecategory',
            name='order',
            field=models.PositiveIntegerField(default=0, editable=False, db_index=True),
            preserve_default=False,
        ),
    ]
