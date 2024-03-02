import re

from django.shortcuts import render
from main.models import Person, PassportImage


def index(request):
    template_name = "main/index.html"
    errors = []
    data = request.POST
    files = request.FILES

    if request.method == "POST":
        full_name = data.get("full_name", "")
        phone_number = data.get("phone_number", "")
        passport = data.get("passport", "")
        latitude = data.get("latitude")
        longitude = data.get("longitude")
        front_image = files.get("passport_image")
        back_image = files.get("passport_secondary_image")
        kadastr_image = files.get("kadastr_image")
        house_number = data.get("house_number")
        address = data.get("address", "")

        if not re.match(
                "^\+?998?\s?-?([1-9]{2})\s?-?(\d{3})\s?-?(\d{2})\s?-?(\d{2})$",
                phone_number,
        ):
            errors.append("Phone number is not valid! Please enter the right format of your phone number: "
                          "+998XXXXXXXXX, +998-XX-XXX-XX-XX, +998 XX XXX XX XX")

        if not re.match("^([A-Za-z])[0-9]{7}$", passport):
            errors.append("Passport number and series is not valid! Please enter the right format of your passport: "
                          "ABXXXXXXX, ACXXXXXXX, ADXXXXXXX")

        if not house_number.isdigit():
            errors.append("House number is not valid! Please enter only digits.")

        if not errors:
            passport_image = PassportImage.objects.create(
                front_image=front_image,
                back_image=back_image,
            )

            Person.objects.create(
                full_name=full_name,
                phone_number=phone_number,
                passport=passport,
                address=address,
                latitude=latitude,
                longitude=longitude,
                passport_image=passport_image,
                kadastr_image=kadastr_image,
                house_number=house_number,
            )

            template_name = "main/done.html"

    return render(request, template_name, {"errors": errors, "data": data})
