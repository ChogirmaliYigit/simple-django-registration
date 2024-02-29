from django.shortcuts import render
from main.models import Person, PassportImage
from UzTransliterator import UzTransliterator
obj = UzTransliterator.UzTransliterator()

def index(request):
    template_name = "main/index.html"
    if request.method == "POST":
        data = request.POST
        
        # address = obj.transliterate(address, from_="lat", to="cyr") ?
         
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
        return render(request, template_name)
    
    else:
        return render(request, template_name)

