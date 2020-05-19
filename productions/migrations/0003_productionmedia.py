import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("productions", "0002_productionvideo")]

    operations = [
        migrations.CreateModel(
            name="ProductionMedia",
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
                    "production",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="productions.Production",
                    ),
                ),
            ],
            options={"abstract": False, "verbose_name_plural": "Production media"},
        )
    ]
