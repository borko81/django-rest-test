from django.db import models


class Groups(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Simple(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.PositiveIntegerField()
    groups = models.ForeignKey(Groups, on_delete=models.CASCADE, related_name='groups')

    def __str__(self):
        return self.name
