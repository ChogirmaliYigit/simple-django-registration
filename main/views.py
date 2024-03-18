import re

from django.shortcuts import render, redirect
from main.models import Person, PassportImage


def index(request):
    errors = []
    data = request.POST
    files = request.FILES

    if request.method == "POST":
        phone_number = data.get("phone_number", "")
        house_number = data.get("house_number")

        if not re.match(
                "^\+?998?\s?-?([1-9]{2})\s?-?(\d{3})\s?-?(\d{2})\s?-?(\d{2})$",
                phone_number,
        ):
            errors.append("Phone number is not valid! Please enter the right format of your phone number: "
                          "+998XXXXXXXXX, +998-XX-XXX-XX-XX, +998 XX XXX XX XX")

        if not house_number.isdigit():
            errors.append("House number is not valid! Please enter only digits.")

        if errors:
            return render(request, "main/index.html", {"errors": errors, "data": data})

        full_name = data.get("full_name", "")
        latitude = data.get("latitude")
        longitude = data.get("longitude")
        front_image = files.get("passport_image")
        back_image = files.get("passport_secondary_image")
        kadastr_image = files.get("kadastr_image")
        address = data.get("address", "")
        passport_seria_number = data.get("passport_seria_number", "")

        person = Person.objects.create(
            full_name=full_name,
            phone_number=phone_number,
            passport=passport_seria_number,
            address=address,
            latitude=latitude,
            longitude=longitude,
            kadastr_image=kadastr_image,
            house_number=house_number,
        )

        PassportImage.objects.create(
            front_image=front_image,
            back_image=back_image,
            person=person,
        )
        return redirect("index-page")

    return render(request, "main/index.html", {"errors": errors, "data": data})
