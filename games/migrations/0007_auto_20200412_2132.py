# Generated by Django 3.0.5 on 2020-04-12 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("games", "0006_auto_20160919_0008"),
    ]

    operations = [
        migrations.AlterField(
            model_name="game",
            name="description",
            field=models.TextField(blank=True, help_text="Enter valid HTML", null=True),
        ),
        migrations.AlterField(
            model_name="game",
            name="order",
            field=models.PositiveIntegerField(
                db_index=True, editable=False, verbose_name="order"
            ),
        ),
        migrations.AlterField(
            model_name="game",
            name="release_year",
            field=models.PositiveSmallIntegerField(
                blank=True, db_index=True, null=True, verbose_name="Year released"
            ),
        ),
        migrations.AlterField(
            model_name="gamebutton",
            name="css_class",
            field=models.CharField(
                blank=True, max_length=15, null=True, verbose_name="CSS class"
            ),
        ),
        migrations.AlterField(
            model_name="gamebutton",
            name="external_url",
            field=models.URLField(blank=True, null=True, verbose_name="External URL"),
        ),
        migrations.AlterField(
            model_name="gamebutton",
            name="local_resource",
            field=models.FileField(blank=True, null=True, upload_to="download"),
        ),
        migrations.AlterField(
            model_name="gamecategory",
            name="order",
            field=models.PositiveIntegerField(
                db_index=True, editable=False, verbose_name="order"
            ),
        ),
        migrations.AlterField(
            model_name="gameimage",
            name="img",
            field=models.ImageField(upload_to="img"),
        ),
        migrations.AlterField(
            model_name="gamemedia",
            name="media",
            field=models.FileField(upload_to="download/media"),
        ),
        migrations.AlterField(
            model_name="gamevideo",
            name="youtube_url",
            field=models.URLField(verbose_name="YouTube URL"),
        ),
    ]
