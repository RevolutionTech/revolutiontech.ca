from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("software", "0002_softwarevideo")]

    operations = [
        migrations.CreateModel(
            name="SoftwareMedia",
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
                    "software",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="software.Software",
                    ),
                ),
            ],
            options={"abstract": False, "verbose_name_plural": "Software media"},
        )
    ]
