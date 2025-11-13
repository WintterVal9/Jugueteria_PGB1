from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.lista_productos, name='lista_productos'),
    path('verificar-conexion/', views.verificar_conexion, name='verificar_conexion'),

    # 🧾 Nueva ruta para el módulo de ventas
    path('ventas/registrar/', views.registrar_venta, name='registrar_venta'),
]