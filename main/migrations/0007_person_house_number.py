# Generated by Django 5.0.2 on 2024-03-01 06:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0006_subscriptionplanuser_is_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="person",
            name="house_number",
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]