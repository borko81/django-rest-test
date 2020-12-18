from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    city = models.CharField(max_length=50)
    objects = None

    def __str__(self):
        return self.name


class OwnerCompany(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.owner.username
