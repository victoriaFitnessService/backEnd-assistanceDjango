# Generated by Django 4.2.4 on 2023-09-14 17:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("assistance", "0012_remove_equipment_image_equipment_imagem"),
    ]

    operations = [
        migrations.RenameField(
            model_name="equipment",
            old_name="imagem",
            new_name="image",
        ),
    ]
