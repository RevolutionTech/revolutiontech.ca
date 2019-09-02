from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("games", "0002_gamevideo")]

    operations = [
        migrations.CreateModel(
            name="GameMedia",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                ("title", models.CharField(max_length=30)),
                ("media", models.FileField(upload_to=b"download/media")),
                (
                    "game",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="games.Game"
                    ),
                ),
            ],
            options={"abstract": False, "verbose_name_plural": "Game media"},
        )
    ]
