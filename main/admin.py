from django.contrib import admin
from unfold.admin import ModelAdmin
from main.models import Person


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
        "passport_image",
        "passport_secondary_image",
        "kadastr_image",
    )
    search_fields = fields + ("id",)
    list_filter_submit = True
