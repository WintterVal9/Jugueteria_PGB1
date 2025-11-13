from django.urls import path
from . import views, views_productos

urlpatterns = [
    # 🔹 API
    path('api/productos/', views.api_productos, name='api_productos'),
    path('verificar-conexion/', views.verificar_conexion, name='verificar_conexion'),

    # 🔹 Usuario general
    path('productos/', views.lista_productos, name='lista_productos'),

    # 🔹 Administración
    path('admin/productos/', views_productos.lista_productos_admin, name='admin_productos'),
    path('admin/productos/nuevo/', views_productos.crear_producto, name='admin_crear_producto'),
]

