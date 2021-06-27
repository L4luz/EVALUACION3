from django import forms
from django.forms import ModelForm
from .models import Usuario,Proveedor

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields =['userName','email','nombre','apellido','fechaNacimiento','clave','categoria']
class ProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        fields =['rut','nombreProveedor','razonSocial','descripcion','telefono','emailProveedor','tipoServicio']