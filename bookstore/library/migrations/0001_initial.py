# Generated by Django 4.2.5 on 2023-12-06 15:24

from django.db import migrations, models

__all__ = ["Migration"]


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        default="NO_NAME",
                        max_length=33,
                        verbose_name="название",
                    ),
                ),
                (
                    "author",
                    models.CharField(
                        default="NO_AUTHOR",
                        max_length=33,
                        verbose_name="автор",
                    ),
                ),
                (
                    "publisher",
                    models.CharField(
                        default="NO_PUBLISHER",
                        max_length=33,
                        verbose_name="издательство",
                    ),
                ),
                (
                    "year",
                    models.IntegerField(
                        default="NO_YEAR",
                        max_length=4,
                        verbose_name="год",
                    ),
                ),
                ("price", models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
