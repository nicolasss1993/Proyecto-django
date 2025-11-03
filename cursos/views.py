from cursos.forms import CursoForm
from cursos.models import Cursos
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView


class CursoListView(ListView):
    model = Cursos
    template_name = "cursos/curso_list.html"
    context_object_name = "cursos"
    
    def get_queryset(self):
        query = self.request.GET.get("q", "")
        if len(query) > 0:
            return Cursos.objects.filter(nombre__icontains=query).order_by("-fecha_creacion")
        return Cursos.objects.all()


class CursoCreateView(CreateView):
    model = Cursos
    form_class = CursoForm
    template_name = "cursos/curso_form.html"
    success_url = reverse_lazy("curso_list")


class CursoUpdateView(UpdateView):
    model = Cursos
    form_class = CursoForm
    template_name = "cursos/curso_form.html"
    success_url = reverse_lazy("curso_list")
    slug_field = "code"
    slug_url_kwarg = "code"


class CursoDeleteView(DeleteView):
    model = Cursos
    template_name = "cursos/curso_confirm_delete.html"
    success_url = reverse_lazy("curso_list")
    slug_field = "nro_comision"
    slug_url_kwarg = "nro_comision"


class CursoDetailView(DetailView):
    model = Cursos
    template_name = "cursos/curso_detail.html"
    context_object_name = "curso"
    slug_field = "code"
    slug_url_kwarg = "code"
