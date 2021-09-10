from django.db import models


class Films(models.Model):
    name = models.CharField(max_length=32, unique=True)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name
