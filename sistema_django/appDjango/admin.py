from django.contrib import admin
from appDjango.models import *

# Register your models here.

"""
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "cui_empleado", "telefono",)
"""

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
