from django.urls import path
from . import views

"""Uniform Resource Locators(URLs)"""

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name="blog-about"),
]
