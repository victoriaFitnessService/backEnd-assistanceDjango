# Generated by Django 4.2.4 on 2023-08-04 12:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("assistance", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Service",
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
                ("name", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("category", models.CharField(max_length=200)),
            ],
            options={
                "verbose_name": "Service",
                "verbose_name_plural": "Services",
            },
        ),
    ]
