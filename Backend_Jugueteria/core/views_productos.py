from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .models import Producto
import json

@csrf_exempt
def productos_crud(request):
    """CRUD completo de productos"""
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

def lista_productos_admin(request):
    """Vista para administración de productos (si la necesitas)"""
    productos = Producto.objects.all()
    # Puedes retornar JSON o renderizar un template según necesites
    return JsonResponse({'status': 'ok', 'productos': list(productos.values())})