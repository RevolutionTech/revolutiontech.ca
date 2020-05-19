from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("games", "0003_gamemedia")]

    operations = [
        migrations.AddField(
            model_name="game",
            name="visible",
            field=models.BooleanField(default=True, db_index=True),
        )
    ]
