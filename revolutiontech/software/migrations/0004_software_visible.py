# -*- coding: utf-8 -*-
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0003_softwaremedia'),
    ]

    operations = [
        migrations.AddField(
            model_name='software',
            name='visible',
            field=models.BooleanField(default=True, db_index=True),
        ),
    ]
