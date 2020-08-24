from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_v, name='home'),
    path('ps4/', views.ps4_v, name='ps4'),
    path('netflix/', views.netflix_v, name='netflix'),
    # path('nety/', views.nety_v, name='nety'),
    path('nintendo/', views.nintendo_v, name='nintendo'),
]
