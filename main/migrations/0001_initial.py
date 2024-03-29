# Generated by Django 5.0.2 on 2024-02-23 16:55

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Person",
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
                ("full_name", models.CharField(max_length=500)),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region="UZ"
                    ),
                ),
                ("passport", models.CharField(max_length=20)),
                ("address", models.TextField()),
            ],
            options={
                "verbose_name": "Ro'yxatga yozilgan shaxs",
                "verbose_name_plural": "Ro'yxatga yozilgan shaxslar",
                "db_table": "people",
            },
        ),
    ]
