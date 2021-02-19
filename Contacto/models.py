from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    email=models.EmailField()
    contenido=models.TextField()
    
    
    def __str__(self):
        return self.nombre