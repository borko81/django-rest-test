from django.contrib import admin

from .models import City, Country, CountyCount

admin.site.register(Country)
admin.site.register(City)
admin.site.register(CountyCount)
