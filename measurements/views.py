from django.shortcuts import render, get_object_or_404
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

import folium

from .models import Measurement
from .forms import MeasurementModelForm
from .utils import get_geo

# Create your views here.

def calculate_distance_view(request):
    obj = get_object_or_404(Measurement, id=1)
    form = MeasurementModelForm(request.POST or None)
    geolocator = Nominatim(user_agent='measurements')

    ip = '154.123.172.215'

    country, city, lat, lon = get_geo(ip)

    location = geolocator.geocode(city)

    print(f'######, {location}')

    location_lat = lat
    location_lon = lon
    
    #Coordinates of the fist location
    pointA = (location_lat, location_lon)
   

   #initial folium map modification.    
    m = folium.Map(width=800, height=500, location= pointA)

    #Location marker on the map.
    folium.Marker([location_lat, location_lon], tooltip='Click here for more', popup=city['city'], icon=folium.Icon(color='purple')).add_to(m)


    if form.is_valid():
        instance = form.save(commit=False)
        destination_ = form.cleaned_data.get('destination')
        destination = geolocator.geocode(destination_)

        #destination coordinates.
        d_lat = destination.latitude
        d_long = destination.longitude
        instance.location = location
        pointB = (d_lat, d_long)
        
        #calculate distance using geodesic
        distance = round(geodesic(pointA, pointB).km, 2)
        instance.distance = distance

        # folium map modification

        #Save to the database.
        instance.save()

    #do an html representation of m
    m = m._repr_html_()


    context = {
        'distance': obj,
        'form': form,
        'map':m,
    }

    return render(request, 'measurements/main.html', context)