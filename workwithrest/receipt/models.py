import uuid

from django.db import models


class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=120, unique=True, verbose_name='Name')
    direction = models.CharField(max_length=120, verbose_name='Direction')
    phone = models.IntegerField()

    def __str__(self):
        return self.name


class Recipe(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True, verbose_name='Name')
    type = models.CharField(max_length=50, choices=
                                [
                                    ('BREAKFAST', 'Breakfast'),
                                    ('LUNCH', 'Lunch'),
                                    ('COFFEE', 'Coffee'),
                                    ('DINNER', 'Dinner')
                                ]
                            ),
    thumbnail = models.ImageField(upload_to='recipe_thumbnails', default='recipe_thumbnails/default.png')

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    recipe = models.ManyToManyField(Recipe)
    name = models.CharField(max_length=120, unique=True, verbose_name='Name')

    def __str__(self):
        return self.name
