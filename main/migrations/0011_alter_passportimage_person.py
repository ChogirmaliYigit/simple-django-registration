# Generated by Django 5.0.2 on 2024-03-04 10:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0010_alter_person_passport"),
    ]

    operations = [
        migrations.AlterField(
            model_name="passportimage",
            name="person",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="passport_images",
                to="main.person",
            ),
        ),
    ]