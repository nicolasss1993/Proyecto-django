from django.urls import path
from core.views import *

urlpatterns = [
    path("", index , name="index"),
    path("estudiante", estudiante_list, name="estudiante_list"),
    path("estudiante/<int:nro_estudiante>/", estudiante_detail, name="estudiante_detail"),
    path("estudiante/nuevo", estudiante_form, name="estudiante_form"),
    path("estudiante/<int:nro_estudiante>/eliminar", estudiante_eliminar, name="estudiante_delete"),
    path("estudiante/<int:nro_estudiante>/modificar/", modificar_estudiante , name="estudiante_edit"),
]