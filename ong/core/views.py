from django.shortcuts import render,redirect
from .models import Proveedor, Usuario
from .forms import ProveedorForm, UsuarioForm
# Create your views here.
def inicio(request):
    return render(request,'core/index.html')
def quiSom(request):
    return render(request,'core/quiSom.html')
def mi_vi(request):
    return render(request,'core/mi_vi.html')
def comAdo(request):
    return render(request,'core/comAdo.html')
def contac(request):
    return render(request,'core/contac.html')
def seccion_gatos(request):
    return render(request,'core/seccion-gatos.html')
def seccion_perros(request):
    return render(request,'core/seccion-perros.html')
def vista_detalles_perro(request):
    return render(request,'core/vista_detalles_perro.html')
    
def proveedores(request):
    proveedores= Proveedor.objects.all()
    datos = {
        'proveedores' : proveedores
    }
    return render(request,'core/proveedores.html',datos)
    
def tabla_usuarios(request):
    usuarios= Usuario.objects.all()
    datos = {
        'usuarios' : usuarios
    }
    return render(request,'core/tabla-usuarios.html',datos)

def form_usuario(request):
    datos = {
        'form' : UsuarioForm()
    }
    if request.method== 'POST':
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Guardados Correctamente'
    return render(request,'core/form-usuario.html',datos)

def crearProveedores(request):
    datos = {
        'form' : ProveedorForm()
    }
    if request.method== 'POST':
        formulario = ProveedorForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Guardados Correctamente'
    return render(request,'core/crearProveedores.html',datos)
    
def modificarProveedor(request,id):
    proveedor = Proveedor.objects.get(rut=id)
    datos = {
        'form' : ProveedorForm(instance=proveedor)
    }
    if request.method == 'POST':
        formulario = ProveedorForm(data=request.POST,instance=proveedor)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificados correctamente"
    return render(request,'core/modificarProveedor.html',datos)

def elimiProveedor(request,id):
    proveedor = Proveedor.objects.get(rut=id)
    proveedor.delete()
    return redirect(to="inicio")