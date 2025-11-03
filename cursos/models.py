from django.db import models
import uuid


def generar_code():
    return uuid.uuid4().hex # aljhsasasd-asdasdasdas-afsaasfad


class Cursos(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    code = models.CharField(
        max_length=32,
        unique=True,
        default=generar_code
    )
    nro_comision = models.IntegerField(unique=True)
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Comision: {self.nro_comision}"
