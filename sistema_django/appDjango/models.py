from django.db import models
from datetime import datetime
from django.forms import model_to_dict

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre', unique=True)
    
    def __str__(self):
        #return 'Nro: {} / Nombre: {}', format(self.id, self.nombre)
        return str(self.nombre)
    
    def toJSON(self):
        item = model_to_dict(self)
        return item
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']
        

class Producto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre', unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='producto/%Y/%m/%d', null=True, blank=True)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    
    def __str__(self):
        return str(self.nombre)
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']


class Cliente(models.Model):
    nombres = models.CharField(max_length=100, verbose_name='Nombres')
    apellidos = models.CharField(max_length=100, verbose_name='Apellidos')
    dpi = models.CharField(max_length=13, unique=True, verbose_name='DPI')
    fecha_nacimiento = models.DateField(default=datetime.now, verbose_name='Fecha de Nacimiento')
    direccion = models.CharField(max_length=100, null=True, blank=True, verbose_name='Direccion')
    
    def __str__(self):
        return str(self.nombres)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']
        

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_registro = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    
    def __str__(self):
        return str(self.cliente.nombres)
    
    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']
        

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cantidad = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    
    def __str__(self):
        return str(self.producto.nombre)
    
    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalles de Venta'
        ordering = ['id']
