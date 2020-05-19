import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("games", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="GameVideo",
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
                ("youtube_url", models.URLField(verbose_name=b"YouTube URL")),
                (
                    "game",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="games.Game"
                    ),
                ),
            ],
            options={"abstract": False},
        )
    ]
