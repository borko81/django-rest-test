from django.db import models


class CreateUpdateDateTime(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
