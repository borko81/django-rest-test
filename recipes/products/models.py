from django.db import models


class Grops(models.Model):
    name = models.CharField(max_length=255, unique=True)
    razpad = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Simples(models.Model):
    name = models.CharField(max_length=255, unique=True)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    group = models.ForeignKey(Grops, on_delete=models.CASCADE, related_name='simples', limit_choices_to={'razpad': False}, default=1)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['pk']


class RecipeIngredient(models.Model):
    recepies = models.ForeignKey('Recepies', on_delete=models.CASCADE)
    ingredient = models.ForeignKey('Simples', on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)


class Recepies(models.Model):
    name = models.CharField(max_length=250, unique=True)
    ingredients = models.ManyToManyField(Simples, through=RecipeIngredient, db_index=True)
    group = models.ForeignKey(Grops, on_delete=models.CASCADE, related_name='recepies', limit_choices_to={'razpad': True}, default=2)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name
