from django.db import models
from django.contrib.auth.models import AbstractUser


class CommonInfo(models.Model):
    eng_name = models.CharField(max_length=256, blank=False)
    rus_name = models.CharField(max_length=256, blank=False)

    class Meta:
        abstract = True


class Country(CommonInfo):
    iso_code = models.CharField(max_length=2)

    def __str__(self):
        return self.eng_name


class City(CommonInfo):
    country = models.ForeignKey(
        Country, related_name='cities', on_delete=models.CASCADE, blank=False
    )

    def __str__(self):
        return self.eng_name


class Airport(CommonInfo):
    icao = models.CharField(max_length=4, blank=False)
    city = models.ForeignKey(
        City, related_name='airports', on_delete=models.CASCADE, blank=False
    )
    airstrip_length = models.FloatField(blank=True, null=True)
    phone_number = models.CharField(max_length=17, blank=True)

    def __str__(self):
        return self.eng_name


class UserCustom(AbstractUser):
    phone_number = models.CharField( max_length=17, blank=True)
    patronymic = models.CharField(max_length=256, blank=False)

