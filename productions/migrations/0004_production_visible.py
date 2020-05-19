from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("productions", "0003_productionmedia")]

    operations = [
        migrations.AddField(
            model_name="production",
            name="visible",
            field=models.BooleanField(default=True, db_index=True),
        )
    ]
