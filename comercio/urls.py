from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resultados/', views.resultado_permisos, name='resultado_permisos'),
]