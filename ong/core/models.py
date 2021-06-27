from django.db import models

class Categoria(models.Model):
    idCAtegoria = models.CharField(primary_key=True,max_length=20,verbose_name='idCategoria',default='')
    nombreCAtegoria = models.CharField(max_length=50,verbose_name='nombreCategoria',default='')
    def _str_(self):
        return self.nombreCAtegoria

class Usuario(models.Model):
    
    userName = models.CharField(primary_key=True,max_length=50,verbose_name='userName',default='')
    email = models.CharField(max_length=50,verbose_name='email',default='')
    nombre = models.CharField(max_length=50,verbose_name='nombre',default='')
    apellido = models.CharField(max_length=50,verbose_name='apellido',default='')
    fechaNacimiento = models.CharField(max_length=20,verbose_name='fechaNacimiento',default='')
    clave = models.CharField(max_length=50,verbose_name='clave',default='')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    def _str_(self):
        return self.nombre


class Servicio(models.Model):
    idCategoria = models.CharField(primary_key=True,max_length=20,verbose_name='idCategoria',default='')
    nombreServicio = models.CharField(max_length=50,verbose_name='nombreServicio',default='')
    def _str_(self):
        return self.nombreServicio

class Proveedor(models.Model):
    
    rut = models.CharField(primary_key=True,max_length=50,verbose_name='rut',default='')
    nombreProveedor = models.CharField(max_length=50,verbose_name='nombreProveedor',default='')
    razonSocial = models.CharField(max_length=50,verbose_name='razonSocial',default='')
    descripcion = models.CharField(max_length=500,verbose_name='descripcion',default='')
    telefono = models.CharField(max_length=50,verbose_name='telefono',default='')
    emailProveedor = models.CharField(max_length=50,verbose_name='emailProveedor',default='')
    tipoServicio = models.ForeignKey(Servicio,on_delete=models.CASCADE)
    def _str_(self):
        return self.rut