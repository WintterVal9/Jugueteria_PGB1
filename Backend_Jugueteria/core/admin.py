from django.contrib import admin
from .models import Producto ,Cliente

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'precio', 'stock', 'linea', 'created_at')
    search_fields = ('codigo', 'nombre', 'linea')
    list_filter = ('linea',)
    ordering = ('nombre',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'email', 'telefono', 'fecha_registro']
    search_fields = ['nombre', 'email', 'codigo']
    list_filter = ['fecha_registro']
