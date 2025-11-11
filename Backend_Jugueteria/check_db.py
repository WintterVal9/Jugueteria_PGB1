#!/usr/bin/env python
import os
import django
from django.db import connections
from django.db.utils import OperationalError


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_django.settings')
django.setup()

def check_database():
    print("🔍 Verificando conexión con la base de datos MySQL...\n")
    db_conn = connections['default']
    try:
        db_conn.cursor()
        print("✅ Conexión establecida correctamente con MySQL.")
    except OperationalError as e:
        print("❌ Error al conectar con MySQL.")
        print(f"Detalles del error:\n{e}")

if __name__ == "__main__":
    check_database()
