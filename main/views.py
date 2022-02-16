import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def index(request):
    appid = "6a0349e8bb281048c9f02bf7a6bddec5"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid
    # city = "London"

    if(request.method == "POST"):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:

        res = requests.get(url.format(city.name)).json()

        if res.get('main'):
            city_info = {
                'city': city.name,
                'temp': res['main']['temp'],
                'icon': res['weather'][0]['icon'],
                'error': False,
            }

        else:
            city_info = {
                'city': city.name,
                'error': True,
            }

        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')
