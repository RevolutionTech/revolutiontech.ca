# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    def set_initial_orders(apps, schema_editor):
        GameCategory = apps.get_model("games", "GameCategory")
        for category in GameCategory.objects.all():
            category.order = category.id
            category.save()
        Game = apps.get_model("games", "Game")
        for game in Game.objects.all():
            game.order = game.id
            game.save()

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
        migrations.RunPython(set_initial_orders),
    ]
