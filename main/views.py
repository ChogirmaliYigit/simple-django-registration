from django.shortcuts import render
from main.models import Person


def index(request):
    template_name = "main/index.html"

    if request.method == "POST":
        full_name = request.POST.get("full_name", "")
        phone_number = request.POST.get("phone_number", "")
        passport = request.POST.get("passport", "")
        address = request.POST.get("address", "")

        Person.objects.create(
            full_name=full_name,
            phone_number=phone_number,
            passport=passport,
            address=address,
        )

        template_name = "main/done.html"

    return render(request, template_name)
