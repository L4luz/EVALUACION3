from rest_usuario.viewslogin import login
from django.urls import path
from .views import lista_proveedores,modificar_proveedor,actualizar_proveedor
urlpatterns = [
    path('proveedores', lista_proveedores, name="lista_proveedores"),
    path('proveedor', modificar_proveedor, name="modificar_proveedor"),
    path('proveedorr/<id>', actualizar_proveedor, name="actualizar_proveedor"),
    path('login',login,name="login"),
]