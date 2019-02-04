from django.contrib import admin
from rest_api_airports import models


admin.site.register(models.Airport)
admin.site.register(models.City)
admin.site.register(models.Country)
admin.site.register(models.UserCustom)

