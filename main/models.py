from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Person(models.Model):
    full_name = models.CharField(max_length=500)
    phone_number = PhoneNumberField(region="UZ")
    passport = models.CharField(max_length=20, null=True)
    address = models.TextField(null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    kadastr_image = models.ImageField(upload_to="kadastr_images/")
    house_number = models.CharField(max_length=10)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = "people"
        verbose_name = "Ro'yxatga yozilgan shaxs"
        verbose_name_plural = "Ro'yxatga yozilgan shaxslar"


class PassportImage(models.Model):
    front_image = models.ImageField(upload_to="passport_images/front/")
    back_image = models.ImageField(upload_to="passport_images/back/")
    person: Person = models.ForeignKey("main.Person", on_delete=models.CASCADE, related_name="passport_images", null=True)

    class Meta:
        db_table = "passportImage"
        verbose_name = "Ro'yxatga yozilgan shaxs passport rasmlari"
        verbose_name_plural = "Ro'yxatga yozilgan shaxslar passport rasmlari"


class SubscriptionPlan(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "subscription_plans"
        verbose_name = "Ta'rif"
        verbose_name_plural = "Ta'riflar"


class SubscriptionPlanUser(models.Model):
    user: Person = models.ForeignKey(Person, on_delete=models.PROTECT)
    plan: SubscriptionPlan = models.ForeignKey(SubscriptionPlan, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.plan.title} - {self.user.full_name}"

    class Meta:
        db_table = "subscription_plan_users"
        unique_together = ("user", "plan",)
        verbose_name = "Ta'rifga obuna bo'lgan shaxs"
        verbose_name_plural = "Ta'rifga obuna bo'lgan shaxslar"
