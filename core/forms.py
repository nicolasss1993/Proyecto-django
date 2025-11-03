from django import forms
from .models import Estudiante

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'documento', 'fecha_de_nacimiento', 'nro_estudiante', 'nro_telefono']
        widgets = {
            'fecha_de_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


class EstudianteEditForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'documento', 'fecha_de_nacimiento', 'nro_telefono']
        widgets = {
            'fecha_de_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            "nombre": forms.TextInput(attrs={'class': 'form-control'}),
            "apellido": forms.TextInput(attrs={'class': 'form-control'}),
            "documento": forms.TextInput(attrs={'class': 'form-control'}),
            "nro_telefono": forms.TextInput(attrs={'class': 'form-control'}),
        }

"""
class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante                     # Modelo base
        fields = ['nombre', 'apellido']        # Campos a mostrar
        exclude = ['fecha_de_creacion']        # Campos a ocultar
        labels = {                             # Etiquetas personalizadas
            'nombre': 'Nombre del estudiante',
            'apellido': 'Apellido del estudiante'
        }
        help_texts = {                         # Textos de ayuda debajo del campo
            'documento': 'Ingresá el DNI sin puntos ni guiones.'
        }
        error_messages = {                     # Mensajes de error personalizados
            'nombre': {
                'required': 'Por favor, ingresá el nombre del estudiante.'
            },
            'nro_estudiante': {
                'unique': 'Ya existe un estudiante con ese número.'
            }
        }
        widgets = {                            # Widgets para personalizar el input HTML
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Juan'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_de_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

"""


"""
class EstudianteForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        label="Nombre",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Juan'})
    )

    apellido = forms.CharField(
        max_length=50,
        label="Apellido",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    documento = forms.CharField(
        max_length=15,
        label="Documento",
        help_text="Ingresá el DNI sin puntos ni guiones.",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    fecha_de_nacimiento = forms.DateField(
        label="Fecha de Nacimiento",
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    nro_estudiante = forms.IntegerField(
        label="Número de Estudiante",
        error_messages={'unique': 'Este número ya existe.'},
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    nro_telefono = forms.CharField(
        max_length=20,
        label="Teléfono",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

"""