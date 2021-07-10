from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('load_example_data/', views.loadexampledata),
    path('users/', views.users) 
]
