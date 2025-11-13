from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import Producto
from .mongo_storage import guardar_imagen
from bson.objectid import ObjectId

# 🔹 Vista para mostrar productos en el panel administrativo
def lista_productos_admin(request):
    """
    Muestra todos los productos registrados en el panel de administración.
    """
    productos = Producto.objects.all()
    return render(request, 'admin/productos_list.html', {'productos': productos})


# 🔹 Vista para crear un nuevo producto desde formulario HTML
def crear_producto(request):
    """
    Crea un nuevo producto y guarda su imagen en Mongo (si aplica).
    """
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        codigo = request.POST.get('codigo')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        linea = request.POST.get('linea')
        descripcion = request.POST.get('descripcion')
        imagen = request.FILES.get('imagen')

        # Crear objeto del producto
        producto = Producto(
            nombre=nombre,
            codigo=codigo,
            precio=precio,
            stock=stock,
            linea=linea,
            descripcion=descripcion
        )

        # Guardar imagen en MongoDB si existe
        if imagen:
            try:
                file_id = guardar_imagen(imagen, imagen.name)
                producto.linea = str(file_id)  # Guardamos ID del archivo como referencia
            except Exception as e:
                messages.error(request, f"⚠️ Error guardando la imagen: {e}")

        producto.save()
        messages.success(request, f"✅ Producto '{producto.nombre}' registrado correctamente.")
        return redirect('admin_productos')

    # Si es GET, solo renderiza el formulario
    return render(request, 'admin/crear_producto.html')

