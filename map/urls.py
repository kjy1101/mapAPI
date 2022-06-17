from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('data/', data, name="data"),
    path('api/', APItest, name="APItest"),
]