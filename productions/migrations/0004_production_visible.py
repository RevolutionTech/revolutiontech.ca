# -*- coding: utf-8 -*-
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [("productions", "0003_productionmedia")]

    operations = [
        migrations.AddField(
            model_name="production",
            name="visible",
            field=models.BooleanField(default=True, db_index=True),
        )
    ]
