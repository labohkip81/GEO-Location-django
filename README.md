<# GEO-Location-django

This project uses geopy, django and maxmind openmap data, It calculates the distance between your current ip location to a specified town/city around the world.

#Installation.

```git clone https://github.com/Labohkip81/GEO-Location-django.git```

```pip install -r requirements.txt```

Copy country and city map data from maxmind and paste to a ```geopy dir``` on the project level directory.

```python3 manage.py makemigrations```
```python3 manage.py migrate```
```python3 manage.py runserver```

Visit your browser on ```127.0.0.1:8000```.

Type in the location you would like to find location in the city form field provided.


#screenshots:
![foo](https://github.com/Labohkip81/GEO-Location-django/blob/master/screenshots/1.png?raw=true "django_geoloaction")

![screenshot2](https://github.com/Labohkip81/GEO-Location-django/blob/master/screenshots/4.png?raw=true, 'django-geoloacation')
