from django.urls import path
from main.views import index, check_password


urlpatterns = [
    path("", index, name="index-page"),
    path("check-passport", check_password, name="check-passport"),
]
