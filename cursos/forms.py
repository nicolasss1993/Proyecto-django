from django import forms
from cursos.models import Cursos


class CursoForm(forms.ModelForm):
    class Meta:
        model = Cursos
        fields = ["nombre", "nro_comision"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "nro_comision": forms.NumberInput(attrs={"class": "form-control"}),
        }
