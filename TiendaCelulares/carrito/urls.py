from django.urls import path
from . import views

urlpatterns = [
    path('', views.ver_carrito, name='ver_carrito'),
    path('agregar/<int:celular_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
]
