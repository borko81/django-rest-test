from django.contrib import admin

from .models import City, Country, CountyCount, CityCount, Film

admin.site.register(Country)
admin.site.register(City)
admin.site.register(CountyCount)
admin.site.register(CityCount)
admin.site.register(Film)
