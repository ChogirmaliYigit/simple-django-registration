import os
import re
import easyocr

from django.conf import settings
from django.shortcuts import render, redirect
from main.models import Person, PassportImage


def index(request):
    errors = []
    data = request.POST
    request.session['data'] = data
    request.session['errors'] = errors

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

        files = {}
        file_paths = {
            "passport_image": "passport_images/front",
            "passport_secondary_image": "passport_images/back",
            "kadastr_image": "kadastr_images"
        }
        for file_name, file_obj in request.FILES.items():
            # Construct the relative directory path
            directory_path = file_paths[file_name]

            # Construct the relative file path to save
            relative_file_path = os.path.join(directory_path, file_obj.name)

            # Construct the full file path
            file_path = os.path.join(settings.MEDIA_ROOT, relative_file_path)

            # Create the directory if it doesn't exist
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            # Save the file
            with open(file_path, 'wb') as destination:
                for chunk in file_obj.chunks():
                    destination.write(chunk)

            # Store the relative file path in a dictionary
            files[file_name] = relative_file_path
        request.session["files"] = files

        return redirect("check-passport")

    return render(request, "main/index.html", {"errors": errors, "data": data})


def check_password(request):
    data = request.session.get("data")
    files = request.session.get("files")
    errors = request.session.get("errors")

    if errors:
        return render(request, "main/index.html", {"errors": errors, "data": data})

    full_name = data.get("full_name", "")
    phone_number = data.get("phone_number", "")
    latitude = data.get("latitude")
    longitude = data.get("longitude")
    front_image = files.get("passport_image")
    back_image = files.get("passport_secondary_image")
    kadastr_image = files.get("kadastr_image")
    house_number = data.get("house_number")
    address = data.get("address", "")

    passport_image_object_id = request.session.get("passport_image_object_id")
    passport_image_object = PassportImage.objects.filter(id=passport_image_object_id).first()
    if not passport_image_object:
        passport_image_object = PassportImage.objects.create(
            front_image=front_image,
            back_image=back_image,
        )
        request.session["passport_image_object_id"] = passport_image_object.id

    passport_seria_number = data.get("passport", "")
    if not passport_seria_number:
        reader = easyocr.Reader(['en'])
        result = reader.readtext(passport_image_object.front_image.path)
        if result:
            passport_seria_number = result[-1][-2][:9].upper()

    data = dict(data)
    data["passport"] = passport_seria_number

    if request.method == "POST":
        person = Person.objects.create(
            full_name=full_name,
            phone_number=phone_number,
            passport=request.POST.get("passport", passport_seria_number),
            address=address,
            latitude=latitude,
            longitude=longitude,
            kadastr_image=kadastr_image,
            house_number=house_number,
        )

        if passport_image_object:
            passport_image_object.delete()
            del request.session["passport_image_object_id"]

        PassportImage.objects.create(
            front_image=front_image,
            back_image=back_image,
            person=person,
        )

        del request.session['data']
        del request.session['files']

        return redirect("index-page")
    return render(request, "main/check_passport.html", {"data": data})
