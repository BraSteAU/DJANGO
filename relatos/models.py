from django.db import models

# Create your models here.

#generamos dos modelos... autor: va a escribir los relatos
#relato: una historia de viaje escrita por un autor

class Autor(models.Model):
    nombre=models.CharField(max_length=100)
    email=models.EmailField(unique=True)

    def __str__(self):
        return self.nombre
    
class Relato(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha = models.DateField(auto_now_add=True) 
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE,related_name='relatos')

    def __str__(self):
        return f"{self.titulo} ({self.autor.nombre})"
    

