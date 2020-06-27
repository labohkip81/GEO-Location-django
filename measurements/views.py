from django.shortcuts import render, get_object_or_404
from .models import Measurement
from .forms import MeasurementModelForm
from geopy.geocoders import Nominatim

from .utils import get_geo

# Create your views here.

def calculate_distance_view(request):
    obj = get_object_or_404(Measurement, id=1)
    form = MeasurementModelForm(request.POST or None)
    geolocator = Nominatim(user_agent='measurements')

    ip = '154.123.172.215'

    country, city, lat, lon = get_geo(ip)


    print('location country =', country)
    print('location city =', city)
    print('location latitude longitude =', lat, lon)

    location = geolocator.geocode(city)

    print(f'######, {location}')
   


    if form.is_valid():
        instance = form.save(commit=False)
        destination_ = form.cleaned_data.get('destination')
        destination = geolocator.geocode(destination_)
        print(destination)
        d_lat = destination.latitude
        d_long = destination.longitude
        instance.location = 'San Francisco'
        instance.distance = 5000.00

        #instance.save()


    context = {
        'distance': obj,
        'form': form,
    }

    return render(request, 'measurements/main.html', context)