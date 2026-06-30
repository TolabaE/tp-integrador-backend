from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Producto
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView

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
    fields = ['nombre', 'descripcion', 'precio','stock']
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