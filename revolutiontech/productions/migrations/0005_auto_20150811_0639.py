# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    def set_initial_orders(apps, schema_editor):
        ProductionCategory = apps.get_model("productions", "ProductionCategory")
        for category in ProductionCategory.objects.all():
            category.order = category.id
            category.save()
        Production = apps.get_model("productions", "Production")
        for production in Production.objects.all():
            production.order = production.id
            production.save()

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
        migrations.RunPython(set_initial_orders),
    ]
