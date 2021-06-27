from rest_usuario.viewslogin import login
from django.urls import path
from .views import lista_usuario,modificar_usuario,actualizar_usuario
urlpatterns = [
    path('usuarios', lista_usuario, name="lista_usuario"),
    path('usuario', modificar_usuario, name="modificar_usuario"),
    path('usuario/<id>', actualizar_usuario, name="actualizar_usuario"),
    path('login',login,name="login"),
]