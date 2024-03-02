from django.contrib import admin
from unfold.admin import ModelAdmin
from main.models import Person, PassportImage, SubscriptionPlan, SubscriptionPlanUser


@admin.register(Person)
class PersonAdmin(ModelAdmin):
    list_display = ("full_name", "phone_number",)
    fields = (
        "full_name",
        "phone_number",
        "passport",
        "address",
        "latitude",
        "longitude",
        "kadastr_image",
        "house_number",
    )
    search_fields = fields + ("id",)
    list_filter_submit = True


@admin.register(PassportImage)
class PassportImageAdmin(ModelAdmin):
    list_display = ("person", "front_image", "back_image",)
    fields = list_display
    search_fields = fields + ("id",)
    list_filter_submit = True


@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(ModelAdmin):
    list_display = ("title", "description", "price",)
    fields = (
        "title",
        "description",
        "price",
    )
    search_fields = fields + ("id",)
    list_filter = ("price",)
    list_filter_submit = True


@admin.register(SubscriptionPlanUser)
class SubscriptionPlanUserAdmin(ModelAdmin):
    list_display = ("user", "plan", "is_active",)
    fields = (
        "user",
        "plan",
        "is_active",
    )
    search_fields = fields + ("id",)
    list_filter = ("is_active",)
    list_filter_submit = True
