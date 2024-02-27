from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Person(models.Model):
    full_name = models.CharField(max_length=500)
    phone_number = PhoneNumberField(region="UZ")
    passport = models.CharField(max_length=20)
    address = models.TextField(null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    passport_image = models.ImageField(upload_to="passport_images/")
    kadastr_image = models.ImageField(upload_to="kadastr_images/")

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = "people"
        verbose_name = "Ro'yxatga yozilgan shaxs"
        verbose_name_plural = "Ro'yxatga yozilgan shaxslar"
