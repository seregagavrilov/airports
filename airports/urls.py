from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('airports_api/', include('rest_api_airports.urls'))
]
