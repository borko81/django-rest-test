from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


class Problem(models.Model):
    description = models.TextField()
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CharField)
    date_add = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['-date_add']

    def __str__(self):
        return f"{self.type} - {self.description[:10]}"
