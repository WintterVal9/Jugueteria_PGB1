from django.http import JsonResponse
from django.db import connection, OperationalError
import logging
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .models import Producto
import json

logger = logging.getLogger(__name__)

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


def lista_productos(request):
    """
    Devuelve una lista de productos.
    Intenta leer de la tabla creada por un modelo Product (core_product).
    Si no existe la tabla devuelve una lista vacía y un mensaje.
    """
    try:
        with connection.cursor() as cursor:
            # Intentamos obtener columnas comunes: id, codigo, nombre, precio, stock
            # Ajusta la consulta si tu tabla tiene otros nombres de columna.
            cursor.execute("""
                SELECT id, codigo, nombre, precio, stock
                FROM core_producto
                LIMIT 100;
            """)
            rows = cursor.fetchall()
            productos = []
            for r in rows:
                productos.append({
                    "id": r[0],
                    "codigo": r[1],
                    "nombre": r[2],
                    "precio": float(r[3]) if r[3] is not None else None,
                    "stock": int(r[4]) if r[4] is not None else None,
                })
        return JsonResponse({"status": "ok", "count": len(productos), "productos": productos})
    except Exception as e:
        # Si la tabla no existe, devolvemos un JSON útil para pruebas
        logger.warning(f"No se pudo leer core_producto: {e}")
        return JsonResponse({
            "status": "ok",
            "count": 0,
            "productos": [],
            "note": "No existe la tabla core_producto. Crea el modelo y ejecuta migraciones para poblar datos."
        })

@csrf_exempt
def productos_crud(request):
    if request.method == 'GET':
        productos = list(Producto.objects.values())
        return JsonResponse({'status': 'ok', 'data': productos})

    elif request.method == 'POST':
        data = json.loads(request.body)
        producto = Producto.objects.create(
            codigo=data['codigo'],
            nombre=data['nombre'],
            descripcion=data.get('descripcion', ''),
            precio=data.get('precio', 0),
            stock=data.get('stock', 0),
            linea=data.get('linea', '')
        )
        return JsonResponse({'status': 'created', 'data': model_to_dict(producto)})

    elif request.method == 'PUT':
        data = json.loads(request.body)
        producto = Producto.objects.get(id=data['id'])
        producto.nombre = data['nombre']
        producto.precio = data['precio']
        producto.stock = data['stock']
        producto.save()
        return JsonResponse({'status': 'updated', 'data': model_to_dict(producto)})

    elif request.method == 'DELETE':
        data = json.loads(request.body)
        Producto.objects.filter(id=data['id']).delete()
        return JsonResponse({'status': 'deleted'})
    # core/views.py
def api_productos(request):
    productos = list(Producto.objects.values())
    return JsonResponse(productos, safe=False)
from django.shortcuts import render

# 🏠 Vista del index principal
def index(request):
    return render(request, 'index.html')


