from django import urls
from django.urls import path,include
from .views import inicio,quiSom,mi_vi,comAdo,contac,seccion_gatos,seccion_perros,vista_detalles_perro,tabla_usuarios,form_usuario,proveedores,crearProveedores,modificarProveedor,elimiProveedor


urlpatterns = [

    path('', inicio, name="inicio"),
    path('quienes-somos', quiSom, name="quiSom"),
    path('mision-vision', mi_vi, name="mi_vi"),
    path('como-adoptar', comAdo, name="comAdo"),
    path('contactenos', contac, name="contac"),
    path('seccion-gatos', seccion_gatos, name="seccion_gatos"),
    path('seccion-perros', seccion_perros, name="seccion_perros"),
    path('tabla-usuarios', tabla_usuarios, name="tabla-usuarios"),
    path('form-usuario',form_usuario,name='form-usuario'),
    path('proveedores',proveedores,name='proveedores'),
    path('crearProveedores',crearProveedores,name='crearProveedores'),
    path('modificarProveedor/<id>',modificarProveedor,name='modificarProveedor'),
    path('elimiProveedor/<id>',elimiProveedor,name='elimiProveedor'),
]
