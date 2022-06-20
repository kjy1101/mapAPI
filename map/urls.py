from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('land/', land, name="land"),
    path('data/', data, name="data"),
    path('api/', APItest, name="APItest"),
    path('landData/', landData, name="landData")
]