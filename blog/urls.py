from django.urls import path
from .views import *

urlpatterns = [
    path("", index),
    path("blogs", blogs),
    path("about", about)
]