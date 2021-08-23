from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class CountyCount(models.Model):
    count = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.count)


class Country(models.Model):
    name = models.CharField(max_length=30)


class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    population = models.PositiveIntegerField()


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