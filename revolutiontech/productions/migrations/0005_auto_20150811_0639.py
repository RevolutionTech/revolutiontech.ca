# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0004_production_visible'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='production',
            options={'ordering': ('order',)},
        ),
        migrations.AlterModelOptions(
            name='productioncategory',
            options={'ordering': ('order',), 'verbose_name_plural': 'Production categories'},
        ),
        migrations.AddField(
            model_name='production',
            name='order',
            field=models.PositiveIntegerField(default=0, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productioncategory',
            name='order',
            field=models.PositiveIntegerField(default=0, editable=False, db_index=True),
            preserve_default=False,
        ),
    ]
