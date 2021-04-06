from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='APP-home'),
    path('about/', views.about, name='APP-about')
]
