# -*- coding: utf-8 -*-
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_gamemedia'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='visible',
            field=models.BooleanField(default=True, db_index=True),
        ),
    ]
