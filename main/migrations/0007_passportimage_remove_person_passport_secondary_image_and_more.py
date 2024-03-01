# Generated by Django 5.0.2 on 2024-02-29 07:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_subscriptionplanuser_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='PassportImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('front_image', models.ImageField(upload_to='passport_images/')),
                ('back_image', models.ImageField(upload_to='passport_images/')),
            ],
            options={
                'verbose_name': "Ro'yxatga yozilgan shaxs passport rasmlari",
                'verbose_name_plural': "Ro'yxatga yozilgan shaxslar passport rasmlari",
                'db_table': 'passportImage',
            },
        ),
        migrations.RemoveField(
            model_name='person',
            name='passport_secondary_image',
        ),
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.TextField(blank=True, default='1'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subscriptionplan',
            name='description',
            field=models.TextField(blank=True, default='1'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subscriptionplan',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='person',
            name='passport_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.passportimage'),
        ),
    ]