from django.db import models
#test
class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    city = models.CharField(max_length=50)
    objects = None

    def __str__(self):
        return self.name

