from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Producto
from .utils.mongo_storage import guardar_imagen
from bson.objectid import ObjectId

def lista_productos_admin(request):
    productos = Producto.objects.all()
    return render(request, 'admin/productos_list.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        codigo = request.POST.get('codigo')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        linea = request.POST.get('linea')
        descripcion = request.POST.get('descripcion')
        imagen = request.FILES.get('imagen')

        producto = Producto(
            nombre=nombre,
            codigo=codigo,
            precio=precio,
            stock=stock,
            linea=linea,
            descripcion=descripcion
        )

        if imagen:
            file_id = guardar_imagen(imagen, imagen.name)
            producto.linea = str(file_id)  # guardamos ID del archivo en Mongo

        producto.save()
        return redirect('admin_productos')

    return render(request, 'admin/crear_producto.html')
