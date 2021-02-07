from django.urls import path

from . import views 

urlpatterns = [
    path("", views.controls, name="controls"),
    path("off", views.off, name="off"),
    path("on", views.on, name="on"),
    path("red", views.red, name="red"),
    path("blue", views.blue, name="blue"),
    path("color", views.color, name="color"),
]
