from django.http import JsonResponse
from django.db import connection, OperationalError
import logging

logger = logging.getLogger(__name__)

def verificar_conexion(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT DATABASE();")
            db_name = cursor.fetchone()[0]
        logger.info(f"✅ Conectado a la base de datos: {db_name}")
        return JsonResponse({"status": "ok", "database": db_name})
    except OperationalError as e:
        logger.error(f"❌ Error de conexión: {e}")
        return JsonResponse({"status": "error", "message": str(e)}, status=500)
    except Exception as e:
        logger.exception("❌ Error inesperado")
        return JsonResponse({"status": "error", "message": str(e)}, status=500)
