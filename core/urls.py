from django.urls import path
from core.views import *

urlpatterns = [
    path("", index , name="index"),
    path("estudiante", estudiante_list, name="estudiante_list"),
    path("estudiante/<int:nro_estudiante>/", estudiante_detail, name="estudiante_detail")
]