from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    #Fecha de creacion.El argumento sirve para agregar de forma automatica.
    create=models.DateTimeField(auto_now_add=True)
    #Fecha de actualizacion
    update=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
        
    def __str__(self):
        return self.nombre
    
class Post(models.Model):
    nombre=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    #Se agregan ,null=True,blank=True para que no sea obligatorio insertar imagen.
    imagen=models.ImageField(upload_to="Blog", null=True, blank=True)
    #Se agrega para eliminar todos los posts de un usuario que dejar de serlo.
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    #Relaccion varios a varios a traves de la clase categoria.
    categorias=models.ManyToManyField(Categoria)
    create=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'
        
    def __str__(self):
        return self.nombre
    
    

