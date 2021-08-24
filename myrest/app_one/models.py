from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class CountyCount(models.Model):
    count = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.count)


class CityCount(models.Model):
    count = models.PositiveIntegerField(null=True, blank=True)
    town = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.town.name} has {self.count} total's"


class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    population = models.PositiveIntegerField()

    def __str__(self):
        return self.name


@receiver(pre_save, sender=Country)
def country_count_increase(sender, instance, *args, **kwargs):
    """
        Pre saved
    """
    try:
        mycount = CountyCount.objects.get(id=1)
        mycount.count += 1
        mycount.save()
    except CountyCount.DoesNotExist:
        CountyCount.objects.create(count=1)
    finally:
        print(f'Now count is {CountyCount.objects.get(id=1)}')


@receiver(pre_save, sender=City)
def city_count_increase(sender, instance, *args, **kwargs):
    try:
        c = City.objects.filter(country=Country.objects.get(name=instance.country.name))[0]
        a = CityCount.objects.get(town=Country.objects.get(name=c.country))
        a.count += 1
        a.save()
    except:
        CityCount.objects.create(town=Country.objects.get(name=instance.country.name), count=1)


class Film(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return self.title