# app_cursos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Define la URL para la función index
]