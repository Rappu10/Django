from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_celulares, name='lista_celulares'),
    path('<int:celular_id>/', views.detalle_celular, name='detalle_celular'),
]
