from django.shortcuts import render
from core.models import Estudiante


def index(request):
    return render(request, "core/index.html")


def estudiante_list(request):
    estudiante_q = Estudiante.objects.all() # QuerySet([Estudiante(1), Estudiante(2), ...])
    context = {
        "lista_estudiantes": estudiante_q
    }
    return render(request, "core/estudiante_list.html", context=context)


def estudiante_detail(request, nro_estudiante):
    try:
        estudiante = Estudiante.objects.get(nro_estudiante=nro_estudiante)
    except Estudiante.DoesNotExist:
        return render(request, "core/pagina_error_estudiante.html")
    return render(request, "core/estudiante_detail.html", {"estudiante": estudiante})
