from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Producto
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView

#importaciones del fomrulario de movimiento de stock
from .forms import MovimientoForm
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from .models import MovimientoStock
from django.shortcuts import render, redirect

class ListaEmpleadosView(PermissionRequiredMixin, ListView):
    model = User
    template_name = 'listar_empleados.html'
    context_object_name = 'empleados'
    permission_required = 'auth.view_user' # Solo permitimos que el Administrador vea esto

# aqui listo los pruductos que se encuentran en la base de datos, y los muestro en la plantilla listar_productos.html
class ProductoListView(ListView):
    model = Producto
    permission_required = 'productos.view_producto' #agregamos los permisos segun roles
    template_name = 'productos/listar_productos.html'

# Vista para crear un producto
class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    fields = ['nombre', 'descripcion', 'precio','stock','categoria']
    success_url = reverse_lazy('listar_productos')
    template_name = 'productos/crear_producto.html'
    permission_required = 'productos.add_producto'
    def form_valid(self, form):
        form.instance.usuario = self.request.user # Asigna el producto al usuario logueado
        return super().form_valid(form)

# Vista para editar un producto
class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = Producto
    fields = ['nombre', 'descripcion', 'precio', 'stock']
    permission_required = 'productos.change_producto'
    success_url = reverse_lazy('listar_productos')
    template_name = 'productos/crear_producto.html'

# Vista para borrar un producto
class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = Producto
    permission_required = 'productos.delete_producto'
    success_url = reverse_lazy('listar_productos')
    template_name = 'productos/eliminar_producto.html'

# Vista para registrar un usuario
class RegistroView(CreateView):
    form_class = UserCreationForm
    template_name = 'registro.html'
    success_url = reverse_lazy('login')


def registrar_movimiento(request):
    if request.method == 'POST':
        form = MovimientoForm(request.POST)
        if form.is_valid():
            movimiento = form.save(commit=False)
            movimiento.usuario = request.user 
            
            # Actualizar stock
            producto = movimiento.producto
            if movimiento.tipo == 'ENTRADA':
                producto.stock += movimiento.cantidad
            else:
                if producto.stock >= movimiento.cantidad:
                    producto.stock -= movimiento.cantidad
                else:
                    messages.error(request, "Stock insuficiente para esta salida.")
                    return render(request, 'registrar_movimiento.html', {'form': form})
            
            producto.save()
            movimiento.save()
            messages.success(request, "Movimiento registrado con éxito.")
            return redirect('listar_productos')
    else:
        form = MovimientoForm()
    return render(request, 'movimiento_stock.html', {'form': form})

@staff_member_required
def historial_movimientos(request):
    # Traemos todos los movimientos ordenados por fecha (del más reciente al más antiguo)
    movimientos = MovimientoStock.objects.all().order_by('-fecha')
    return render(request, 'historial_movimientos.html', {'movimientos': movimientos})

