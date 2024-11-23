from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/ships/", views.fetch_ships, name="fetch_ships"),
    path("api/hazards/", views.fetch_hazards, name="fetch_hazards"),
]
