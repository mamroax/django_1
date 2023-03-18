from django.urls import path
from . import views

"""Uniform Resource Locators(URLs)"""

urlpatterns = [
    path('', views.register, name='register'),
]
