from .views import AiroportView, CityView, CountryView, UserCreateView
from rest_framework.routers import DefaultRouter
from django.urls import path, include


app_name ='airports_api'
router = DefaultRouter()
router.register('airports', AiroportView)
router.register('cities', CityView)
router.register('countries', CountryView)
router.register('users', UserCreateView, base_name='users')

urlpatterns = [
    path('v1/', include((router.urls, app_name)))
]
