from django.urls import path
from .views import ProductoListView, ProductoCreateView, ProductoUpdateView, ProductoDeleteView
from . import views



# aqui defino las urls para listar y crear productos
urlpatterns = [
    path('', ProductoListView.as_view(), name='listar_productos'),
    path('crear/', ProductoCreateView.as_view(), name='crear_productos'),
    path('editar/<int:pk>/', ProductoUpdateView.as_view(), name='editar_producto'),
    path('eliminar/<int:pk>/', ProductoDeleteView.as_view(), name='eliminar_producto'),
    path('registrar/', views.registrar_movimiento, name='movimiento_stock'),
    path('historial/', views.historial_movimientos, name='historial_movimientos'),
]