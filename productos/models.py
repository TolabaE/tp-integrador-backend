from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# creamos el modelo categoria con los campos nombre y descripcion. El campo nombre es unico y el campo descripcion es opcional.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

# creo el modelo de producto con los campos nombre, descripcion, precio, stock, fecha_creacion, fecha_actualizacion y usuario.
class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL,null=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return self.nombre

class MovimientoStock(models.Model):
    TIPO_MOVIMIENTO = [
        ('ENTRADA', 'Entrada'),
        ('SALIDA', 'Salida'),
    ]
    
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    tipo = models.CharField(max_length=10, choices=TIPO_MOVIMIENTO)
    fecha = models.DateTimeField(auto_now_add=True)
    observacion = models.CharField(max_length=200, blank=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tipo} - {self.producto.nombre} por {self.usuario}"