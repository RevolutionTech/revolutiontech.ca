# -*- coding: utf-8 -*-
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0004_software_visible'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='software',
            options={'ordering': ('order',), 'verbose_name_plural': 'Software'},
        ),
        migrations.AddField(
            model_name='software',
            name='order',
            field=models.PositiveIntegerField(default=0, editable=False, db_index=True),
            preserve_default=False,
        ),
    ]
