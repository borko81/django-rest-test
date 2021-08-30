from django.contrib import admin

from .models import Snippet, Species, Person

admin.site.register(Snippet)
admin.site.register(Species)
admin.site.register(Person)
