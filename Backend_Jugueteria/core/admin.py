from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'precio', 'stock', 'linea', 'created_at')
    search_fields = ('codigo', 'nombre', 'linea')
    list_filter = ('linea',)
    ordering = ('nombre',)
