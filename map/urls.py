from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('road', road, name="road"),
    path('land', land, name="land"),
    path('data/', data, name="data"),
    path('road/api/', road_API, name="road_API"),
    path('land/api/', landData, name="landData"),
]