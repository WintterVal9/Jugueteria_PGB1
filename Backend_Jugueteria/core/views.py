from django.http import JsonResponse
from django.shortcuts import render, redirect
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
            'clientes': '/api/clientes/'
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
@csrf_exempt
def api_productos(request):
    """Endpoint para obtener y crear productos"""
    if request.method == 'GET':
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
    
    elif request.method == 'POST':
        try:
            # Leer los datos del request
            data = json.loads(request.body)
            print("📦 Datos recibidos:", data)  # Para debug
            
            # Validar campos requeridos
            if not data.get('codigo') or not data.get('nombre'):
                return JsonResponse({
                    'error': 'Los campos código y nombre son requeridos'
                }, status=400)
            
            # Crear el producto en la base de datos
            producto = Producto.objects.create(
                codigo=data['codigo'],
                nombre=data['nombre'],
                precio=data.get('precio', 0),
                stock=data.get('stock', 0),
                linea=data.get('linea', ''),
                descripcion=data.get('descripcion', '')
            )
            
            # Devolver el producto creado
            return JsonResponse({
                'id': producto.id,
                'codigo': producto.codigo,
                'nombre': producto.nombre,
                'precio': str(producto.precio),
                'stock': producto.stock,
                'linea': producto.linea,
                'descripcion': producto.descripcion,
                'mensaje': 'Producto creado exitosamente'
            }, status=201)
            
        except json.JSONDecodeError:
            return JsonResponse({
                'error': 'JSON inválido en el cuerpo de la petición'
            }, status=400)
        except Exception as e:
            logger.error(f"Error al crear producto: {str(e)}")
            return JsonResponse({
                'error': f'Error al crear producto: {str(e)}'
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
    if request.method == 'POST':
        try:
            print("📦 Recibiendo POST para crear producto...")
            print("📦 Datos recibidos:", request.POST)
            producto = Producto.objects.create(
                codigo=request.POST.get('codigo'),
                nombre=request.POST.get('nombre'),
                precio=request.POST.get('precio', 0),
                stock=request.POST.get('stock', 0),
                linea=request.POST.get('linea', ''),
                descripcion=request.POST.get('descripcion', '')
            )
            print(f"✅ Producto creado: {producto.nombre} - ID: {producto.id}")
            # Redirigir al panel de administración después de guardar
            return redirect('/administracion/productos/')
            
        except Exception as e:
            print(f"❌ Error al crear producto: {str(e)}")
            return render(request, 'crear_producto.html', {
                'error': f'Error al guardar el producto: {str(e)}'
            })
    return render(request, 'crear_producto.html')

def registrar_ventas_front(request):
    """Vista para la página de registrar ventas"""
    return render(request, 'registrar_ventas.html')

def api_clientes(request):
    """Endpoint para obtener clientes (para el formulario de ventas)"""
    try:
        from .models import Cliente
        clientes = list(Cliente.objects.values(
            'id', 'codigo', 'nombre', 'email', 'telefono', 'direccion', 'fecha_registro'
        ))
        return JsonResponse(clientes, safe=False)
    except Exception as e:
        return JsonResponse({
            'error': f'Error al obtener clientes: {str(e)}',
            'clientes': []
        }, status=500)