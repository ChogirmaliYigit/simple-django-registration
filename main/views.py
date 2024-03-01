from django.shortcuts import render
from main.models import Person


def index(request):
    template_name = "main/index.html"

    if request.method == "POST":
        full_name = request.POST.get("full_name", "")
        phone_number = request.POST.get("phone_number", "")
        passport = request.POST.get("passport", "")
        latitude = request.POST.get("latitude")
        longitude = request.POST.get("longitude")
        passport_image = request.FILES.get("passport_image")
        passport_secondary_image = request.FILES.get("passport_secondary_image")
        kadastr_image = request.FILES.get("kadastr_image")
        house_number = request.POST.get("house_number")
        address = request.POST.get("address", "")

        Person.objects.create(
            full_name=full_name,
            phone_number=phone_number,
            passport=passport,
            address=address,
            latitude=latitude,
            longitude=longitude,
            passport_image=passport_image,
            passport_secondary_image=passport_secondary_image,
            kadastr_image=kadastr_image
        )

        template_name = "main/done.html"

    return render(request, template_name)
