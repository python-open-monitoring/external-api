from django.urls import path

from apps.main import views

app_name = "main"

urlpatterns = [
    path("", views.main, name="main"),
    path("ping/", views.ping_check, name="ping_check"),
]
