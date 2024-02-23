from django.contrib import admin
from unfold.admin import ModelAdmin
from main.models import Person


@admin.register(Person)
class PersonAdmin(ModelAdmin):
    list_display = ("full_name", "phone_number",)
    fields = ("full_name", "phone_number", "passport", "address",)
    search_fields = fields + ("id",)
    list_filter_submit = True
