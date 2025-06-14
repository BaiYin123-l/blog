from django.urls import path
from main.views import *
urlpatterns = [
    # Add your URL patterns here
    # Example: path('home/', views.home, name='home'),
    path('', index, name='index'),
]