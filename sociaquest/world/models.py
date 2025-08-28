# world/models.py
from django.db import models

class Mundo(models.Model):
    nombre = models.CharField(max_length=100)
    tema = models.CharField(
        max_length=20,
        choices=[
            ('fantasia', 'Fantasia'),
            ('ciencia_ficcion', 'Ciencia Ficción'),
            ('moderno', 'Moderno')
        ]
    )
    descripcion = models.TextField()
    es_publico = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre

class Sala(models.Model):
    mundo = models.ForeignKey(
        Mundo, 
        on_delete=models.CASCADE,  # Si se borra el mundo, se borran sus salas
        related_name='salas'       # mundo.salas.all()
    )
    nombre = models.CharField(max_length=100)
    tema_conversacion = models.CharField(max_length=200, blank=True)
    capacidad_maxima = models.IntegerField(default=50)
    fondo = models.ImageField(upload_to='salas/')
    
    class Meta:
        unique_together = ['mundo', 'nombre']  # No puede haber dos salas con mismo nombre en mismo mundo
    
    def __str__(self):
        return f"{self.mundo.nombre} - {self.nombre}"