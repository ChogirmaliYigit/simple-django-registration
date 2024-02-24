from django.shortcuts import render
from main.models import Person


def index(request):
    template_name = "main/index.html"

    if request.method == "POST":
        print(request.POST)

        full_name = request.POST.get("full_name", "")
        phone_number = request.POST.get("phone_number", "")
        passport = request.POST.get("passport", "")
        address = request.POST.get("address", "")
        latitude = request.POST.get("latitude")
        longitude = request.POST.get("longitude")

        Person.objects.create(
            full_name=full_name,
            phone_number=phone_number,
            passport=passport,
            address=address,
            latitude=latitude,
            longitude=longitude,
        )

        template_name = "main/done.html"

    return render(request, template_name)
