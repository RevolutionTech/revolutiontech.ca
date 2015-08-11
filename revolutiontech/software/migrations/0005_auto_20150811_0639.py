# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    def set_initial_orders(apps, schema_editor):
        Software = apps.get_model("software", "Software")
        for software in Software.objects.all():
            software.order = software.id
            software.save()

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
        migrations.RunPython(set_initial_orders),
    ]
