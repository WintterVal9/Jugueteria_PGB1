from django.urls import path
from . import views, views_productos

urlpatterns = [
    # 🔹 SOLO ENDPOINTS API (bajo /api/)
    path('verificar-conexion/', views.verificar_conexion, name='verificar_conexion'),
    path('productos/', views.api_productos, name='api_productos'),
    path('clientes/', views.api_clientes, name='api_clientes'),
    


    
]


