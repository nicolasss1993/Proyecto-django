from django.urls import path
from cursos.views import *


urlpatterns = [
    path("", CursoListView.as_view(), name="curso_list"),
    path("nuevo/", CursoCreateView.as_view(), name="curso_create"),
    path("<str:code>/", CursoDetailView.as_view(), name="curso_detail"),
    path("<str:code>/editar", CursoUpdateView.as_view(), name="curso_edit"),
    path("<int:nro_comision>", CursoDeleteView.as_view(), name="curso_delete"),
] # Tenemos el CRUD hecho.