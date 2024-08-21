from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=40)
    telefono=models.IntegerField()
    email=models.EmailField()
 
class Producto(models.Model):
    codigo=models.IntegerField()
    descripcion=models.CharField(max_length=50)
    precio=models.DecimalField(decimal_places=2, max_digits=5)
    
class Vendedor(models.Model):
    nombre=models.CharField(max_length=30)
    cbu=models.IntegerField()
    
    

       