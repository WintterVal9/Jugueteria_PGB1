from django.db import models
class Producto(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    stock = models.IntegerField(default=0)
    linea = models.CharField(max_length=100, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'core_producto'
        ordering = ['nombre']

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"
class Venta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.CharField(max_length=150)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    class Meta:
        db_table = 'core_venta'
        ordering = ['-fecha']

    def __str__(self):
        return f"Venta #{self.id} - {self.cliente}"


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    class Meta:
        db_table = 'core_detalle_venta'

    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad}"
class LineaProducto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'core_linea_producto'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
