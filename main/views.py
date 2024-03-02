from django.shortcuts import render
from main.models import Person, PassportImage


def index(request):
    template_name = "main/index.html"

    if request.method == "POST":
        data = request.POST
        files = request.FILES

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

        passport_image = PassportImage(
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

    return render(request, template_name)
