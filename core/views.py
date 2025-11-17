from django.shortcuts import render, redirect, get_object_or_404
from core.forms import EstudianteForm, EstudianteEditForm
from core.models import Estudiante
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "core/index.html")

def about_me(request):
    return render(request, "core/about_me.html")


@login_required
def estudiante_list(request):
    query = request.GET.get("q", "")
    if len(query) > 0:
        estudiante_q = Estudiante.objects.filter(nombre__icontains=query).order_by("-fecha_de_creacion")
    else:
        estudiante_q = Estudiante.objects.all()
    context = {
        "lista_estudiantes": estudiante_q,
        "query": query
    }
    return render(request, "core/estudiante_list.html", context=context)

@login_required
def estudiante_detail(request, nro_estudiante):
    try:
        estudiante = Estudiante.objects.get(nro_estudiante=nro_estudiante)
    except Estudiante.DoesNotExist:
        return render(request, "core/pagina_error_estudiante.html")
    return render(request, "core/estudiante_detail.html", {"estudiante": estudiante})

@login_required
def estudiante_form(request):
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("estudiante_list")
    else:
        form = EstudianteForm()
    
    context = {
        "form": form
    }
    return render(request, "core/estudiante_form.html", context)

@login_required
def estudiante_eliminar(request, nro_estudiante):
    estudiante = get_object_or_404(Estudiante, nro_estudiante=nro_estudiante)
    estudiante.delete()
    return redirect('estudiante_list')

@login_required
def modificar_estudiante(request, nro_estudiante):
    estudiante = get_object_or_404(Estudiante, nro_estudiante=nro_estudiante)
    if request.method == "POST":
        form = EstudianteEditForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect("estudiante_list")
    else:
        form = EstudianteEditForm(instance=estudiante)

    return render(request, "core/estudiante_form.html", {"form": form, "edicion": True})
