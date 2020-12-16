from django.contrib import admin

from .models import *


@admin.register(Restaurant)
class Restaurant(admin.ModelAdmin):
    list_display = ('name', 'direction', 'phone')
    list_filter = ('name',)


@admin.register(Recipe)
class Recipe(admin.ModelAdmin):
    list_display = ('name', 'type')
    list_filter = ('name',)


@admin.register(Ingredient)
class Ingredient(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name',)
