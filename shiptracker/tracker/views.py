import os
import requests
from django.http import JsonResponse
from .models import Hazard
from django.shortcuts import render


def fetch_ships(request):
    lat = request.GET.get("lat")
    lon = request.GET.get("lon")
    radius = request.GET.get("radius", 10)  # Радиус по умолчанию

    api_key = os.getenv("MYSHIPTRACKING_API_KEY")
    url = f"https://api.myshiptracking.com/vessels?lat={lat}&lon={lon}&radius={radius}&apikey={api_key}"

    response = requests.get(url)
    if response.status_code == 200:
        return JsonResponse(response.json())
    return JsonResponse({"error": "Unable to fetch data"}, status=500)


def fetch_hazards(request):
    hazards = Hazard.objects.all().values("latitude", "longitude", "description")
    return JsonResponse(list(hazards), safe=False)


def index(request):
    return render(request, "tracker/index.html")
