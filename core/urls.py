from django.urls import path
from .views import *
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name="index" ),
    path('vehiculos', vehiculos, name="vehiculos" ),
    path('about', about, name="about" ),
    path('mecanicos', mecanicos, name="mecanicos" ),
    path('contact', contact, name="contact" ),
    path('services', services, name="services" ),
    path('listarmecanicos/', listarmecanicos, name="listarmecanicos" ),
    path('administrador', administrador, name="administrador" ),
    path('empleadosadd', empleadosadd, name="empleadosadd" ),
    path('empleadosupdate/<int:id>/', empleadosupdate, name='empleadosupdate'),
    path('empleadosdelete/<int:id>/', empleadosdelete, name='empleadosdelete'),
    path('registro', registro, name="registro" ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
