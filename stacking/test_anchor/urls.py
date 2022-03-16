from django.urls import path
from .views import *


urlpatterns = [
    path('', anchor),
    path('test/', test),
]
