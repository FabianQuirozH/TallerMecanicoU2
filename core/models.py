from django.db import models

# Create your models here.

class tipoempleado(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

class Empleado(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField(default=0)
    imagen = models.ImageField( upload_to= "mecanicoimg", null=True)
    tipo = models.ForeignKey(tipoempleado,  on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
