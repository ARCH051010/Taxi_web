"""
URL configuration for Taxi_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from reservas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('reservas/', views.reservas, name='reservas'),
    path('reservas/nuevo/', views.reserva_create, name='reserva_create'),
    path('reservas/editar/<int:pk>/', views.reserva_edit, name='reserva_edit'),
    path('reservas/eliminar/<int:pk>/', views.reserva_delete, name='reserva_delete'),
    path('logout/', views.cerrar, name='logout'),
    path('login/', views.entrar, name='login'),
    path('clientes/', views.clientes, name='clientes'),
    path('clientes/nuevo/', views.cliente_create, name='cliente_create'),
    path('clientes/editar/<int:pk>/', views.cliente_edit, name='cliente_edit'),
    path('clientes/eliminar/<int:pk>/', views.cliente_delete, name='cliente_delete'),
    path('conductores/', views.conductor, name='conductores'),
    path('conductores/nuevo/', views.conductor_create, name='conductor_create'),
    path('conductores/editar/<int:pk>/', views.conductor_edit, name='conductor_edit'),
    path('conductores/eliminar/<int:pk>/', views.conductor_delete, name='conductor_delete'),
]
