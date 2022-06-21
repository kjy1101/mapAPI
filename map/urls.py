from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('road', road, name="road"),
    path('land/', land, name="land"),
    path('landData/', landData, name="landData"),
    path('roadData/', roadData, name="roadData"),
    path('road/api/', road_API, name="road_API"),
    path('land/api/', land_API, name="land_API"),
    path('api/', YongIn_regionName)
]