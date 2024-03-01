from django.shortcuts import render
from main.models import Person, PassportImage


def index(request):
    template_name = "main/index.html"
    if request.method == "POST":
        data = request.POST
        
         
        passport_image = PassportImage.objects.create(
            front_image=request.FILES.get("front_image"),
            back_image=request.FILES.get("back_image")
        )
        person = Person.objects.create(
            full_name=data.get("full_name", ""),
            phone_number=data.get("phone_number", ""),
            passport=data.get("passport", ""),
            address=data.get("address", ""),
            latitude=float(data.get("latitude", 0)),
            longitude=float(data.get("longitude", 0)),
            passport_image=passport_image,
            kadastr_image=request.FILES.get("kadastr_image")
        )
        template_name = "main/done.html"
    
    else:
        return render(request, template_name)

