from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.lista_productos, name='lista_productos'),
    path('verificar-conexion/', views.verificar_conexion, name='verificar_conexion'),
]

