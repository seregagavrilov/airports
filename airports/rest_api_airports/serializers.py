from rest_framework import serializers
from .models import Airport, Country, City
from django.contrib.auth import get_user_model


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'eng_name', 'rus_name', 'iso_code')


class CitySerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = City
        fields = ('__all__')


class AirportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Airport
        fields = ('__all__')


class AiroportReadSerializer(AirportSerializer):
    city = CitySerializer(read_only=True)
    country = CountrySerializer(read_only=True)


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super(UserSerializer, self).update(instance, validated_data)

    class Meta:
        model = get_user_model()
        fields = ("__all__")


