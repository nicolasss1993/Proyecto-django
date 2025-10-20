from django.db import models


class Estudiante(models.Model): # Nombre de la tabla
    nombre = models.CharField(max_length=100) # Los campos de la tabla
    apellido = models.CharField(max_length=50)
    documento = models.CharField(max_length=15)
    fecha_de_nacimiento = models.DateField(null=True, blank=True)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    nro_estudiante = models.IntegerField(unique=True)
    nro_telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"Estudiante: {self.nombre}, {self.apellido} - Nro: {self.nro_estudiante}"
