from django.db import models


class Grops(models.Model):
    name = models.CharField(max_length=255, unique=True)
    razpad = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Simples(models.Model):
    name = models.CharField(max_length=255, unique=True)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    group = models.ForeignKey(Grops, on_delete=models.CASCADE, related_name='simples', limit_choices_to={'razpad': False})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['pk']


class Recepies(models.Model):
    name = models.CharField(max_length=255, unique=True)
    group = models.ForeignKey(Grops, on_delete=models.CASCADE, related_name='recepies', limit_choices_to={'razpad': True})
    simple = models.ManyToManyField(Simples, related_name='recepies')
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['pk']
