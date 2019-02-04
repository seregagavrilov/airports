from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model

from rest_api_airports import models
from .serializers import AiroportReadSerializer, CountrySerializer, CitySerializer, AirportSerializer, UserSerializer


class LibraryTestsCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.User = get_user_model()
        self.User.objects.create_user(username="user_staff", password='123', is_staff=True)
        self.User.objects.create_user(username="user", password='123')
        country = models.Country.objects.create(eng_name='testCountry', rus_name='тест страна')
        city = models.City.objects.create(eng_name='testCity', rus_name='тест город', country=country)
        models.Airport.objects.create(eng_name='testAirpoty', rus_name='тест аэропорт', city=city)

        country = models.Country.objects.create(eng_name='testCountry2', rus_name='тест страна2')
        city = models.City.objects.create(eng_name='testCity2', rus_name='тест город2', country=country)
        models.Airport.objects.create(eng_name='testAirpoty2', rus_name='тест аэропорт2', city=city)

    def test_get_airports(self):
        self.client.login(username='user', password='123')
        res = self.client.get('/airports_api/v1/airports/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_get_airport(self):
        self.client.login(username='user', password='123')
        airports = models.Airport.objects.get(pk=1)
        serilaizer = AiroportReadSerializer(airports, many=False)
        res = self.client.get('/airports_api/v1/airports/1/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serilaizer.data)

    def test_airport_create(self):
        self.client.login(username='user_staff', password='123')
        data = {
            'eng_name': 'test_airport',
            'rus_name': 'тест русское имя',
            'city': '1',
            'icao': '1234'
        }
        res = self.client.post('/airports_api/v1/airports/', data=data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_airport_update(self):
        self.client.login(username='user', password='123')

        data = {
            'eng_name': 'test_airport_patch'
        }
        res = self.client.patch('/airports_api/v1/airports/1/', data=data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_airport_delete(self):
        self.client.login(username='user', password='123')
        res = self.client.delete('/airports_api/v1/airports/1/')
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_user(self):
        self.client.login(username='user_staff', password='123')
        user = self.User.objects.get(pk=1)
        serializer = UserSerializer(user, many=False)
        res = self.client.get('/airports_api/v1/users/1/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_cant_get_users_without_staff(self):
        self.client.login(username='user', password='123')
        res = self.client.get('/airports_api/v1/users/')
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_create(self):
        self.client.login(username='user_staff', password='123')
        data = {
            'username': 'usertest',
            'password': 123,
            'patronymic': 'test'
        }
        res = self.client.post('/airports_api/v1/users/', data=data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_get_users(self):
        self.client.login(username='user_staff', password='123')
        res = self.client.get('/airports_api/v1/users/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_cant_create_user_without_staff(self):
        self.client = APIClient()
        self.client.login(username='user', password='123')
        data = {
            'username': 'usertest',
            'password': 123,
            'patronymic': 'test'
        }
        res = self.client.post('/airports_api/v1/users/', data=data)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_delete(self):
        self.client.login(username='user_staff', password='123')
        res = self.client.delete('/airports_api/v1/users/1/')
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_cant_delete_user_without_staff(self):
        self.client.login(username='user', password='123')
        res = self.client.delete('/airports_api/v1/users/1/')
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_country(self):
        self.client.login(username='user', password='123')
        country = models.Country.objects.get(pk=1)
        serializer = CountrySerializer(country, many=False)
        res = self.client.get('/airports_api/v1/countries/1/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_get_city(self):
        self.client.login(username='user', password='123')
        city = models.City.objects.get(pk=1)
        serializer = CitySerializer(city, many=False)
        res = self.client.get('/airports_api/v1/cities/1/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)