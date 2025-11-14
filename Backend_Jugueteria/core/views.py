from django.http import JsonResponse
from django.shortcuts import render
from django.db import connection, OperationalError
import logging
from django.views.decorators.csrf import csrf_exempt
from .models import Producto
import json

logger = logging.getLogger(__name__)

# 🔹 VISTA RAIZ DEL API (NUEVA - AGREGAR ESTA)
def api_root(request):
    """Endpoint raíz de la API para verificación de conexión"""
    return JsonResponse({
        'status': 'success',
        'mensaje': 'API de Juguetería TeddyBear funcionando correctamente',
        'estado': 'conectado',
        'endpoints_disponibles': {
            'verificar_conexion': '/api/verificar-conexion/',
            'productos': '/api/productos/',
        }
    })

# 🔹 VERIFICACIÓN DE CONEXIÓN
def verificar_conexion(request):
    """
    Verifica la conexión a la base de datos (simple SELECT DATABASE()).
    """
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT DATABASE();")
            db_name = cursor.fetchone()[0]
        logger.info(f"Conectado a la base de datos: {db_name}")
        return JsonResponse({"status": "ok", "database": db_name})
    except OperationalError as e:
        logger.error(f"Error de conexión: {e}")
        return JsonResponse({"status": "error", "message": str(e)}, status=500)
    except Exception as e:
        logger.exception("Error inesperado")
        return JsonResponse({"status": "error", "message": str(e)}, status=500)

# 🔹 API PRODUCTOS
def api_productos(request):
    """Endpoint para obtener productos (para tu JavaScript)"""
    try:
        productos = list(Producto.objects.values(
            'id', 'codigo', 'nombre', 'precio', 'stock', 'descripcion', 'linea'
        ))
        return JsonResponse(productos, safe=False)
    except Exception as e:
        return JsonResponse({
            'error': f'Error al obtener productos: {str(e)}',
            'productos': []
        }, status=500)

# 🔹 VISTAS FRONTEND (Páginas HTML)
def index(request):
    return render(request, 'index.html')

def lista_productos_front(request):
    """Vista para la página de lista de productos (frontend)"""
    return render(request, 'productos_list.html')

def admin_productos_front(request):
    """Vista para la página de administración de productos (frontend)"""
    return render(request, 'admin_productos.html')

def crear_producto_front(request):
    """Vista para la página de crear producto (frontend)"""
    return render(request, 'crear_producto.html')

def registrar_ventas_front(request):
    """Vista para la página de registrar ventas"""
    return render(request, 'registrar_ventas.html')