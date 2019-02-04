from rest_framework import viewsets, permissions
from .serializers import (
    AirportSerializer,
    AiroportReadSerializer,
    CitySerializer,
    CountrySerializer,
    UserSerializer
)
from .models import Airport, City, Country
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import AitportPagination
from django.contrib.auth import get_user_model


class ViewMixin:
    filter_backends = (DjangoFilterBackend,)


class AiroportView(viewsets.ModelViewSet, ViewMixin):
    queryset = Airport.objects.all()
    pagination_class = AitportPagination
    filter_fields = (
       'icao',
        'eng_name',
        'rus_name',
        'city__eng_name',
        'city__rus_name',
        'city__country__eng_name',
        'city__country__rus_name',
    )

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return AiroportReadSerializer
        return AirportSerializer

    def get_permissions(self):
        if self.request.method in ['GET']:
            self.permission_classes = [permissions.BasePermission, ]
        else:
            self.permission_classes = [permissions.IsAuthenticated, ]
        return super(AiroportView, self).get_permissions()


class CityView(viewsets.ModelViewSet, ViewMixin):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_fields = (
       'eng_name',
       'rus_name',
    )

    def get_permissions(self):
        if self.request.method in ['GET']:
            self.permission_classes = [permissions.BasePermission, ]
        else:
            self.permission_classes = [permissions.IsAuthenticated, ]
        return super(CityView, self).get_permissions()


class СountryView(viewsets.ModelViewSet, ViewMixin):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_fields = (
      'eng_name',
      'rus_name',
    )

    def get_permissions(self):
        if self.request.method in ['GET']:
            self.permission_classes = [permissions.BasePermission, ]
        else:
            self.permission_classes = [permissions.IsAuthenticated, ]
        return super(СountryView, self).get_permissions()


class UserCreateView(viewsets.ModelViewSet, ViewMixin):
    serializer_class = UserSerializer

    def get_queryset(self):
        User = get_user_model()
        return User.objects.all()

    def get_permissions(self):
        self.permission_classes = [
           permissions.IsAuthenticated,
           permissions.IsAdminUser
        ]
        return super(UserCreateView, self).get_permissions()
