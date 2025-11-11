from django.http import JsonResponse
from django.db import connection, OperationalError
import logging

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
