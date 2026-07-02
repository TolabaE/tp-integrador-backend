from django.contrib import admin
from .models import Producto, MovimientoStock, Categoria

admin.site.register(Producto)
admin.site.register(MovimientoStock)
admin.site.register(Categoria)