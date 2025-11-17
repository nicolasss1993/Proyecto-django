from django import forms
from accounts.models import Perfil
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class PerfilCreationForm(UserCreationForm):
    class Meta:
        model = Perfil
        fields = ("username", "email")


class PerfilChangeForm(UserChangeForm):
    class Meta:
        model = Perfil
        fields = ("avatar", "pais", "direccion", "first_name", "last_name", "password", "username")
        
        widgets = {
            "avatar": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "pais": forms.TextInput(attrs={"class": "form-control", "placeholder": "Pais"}),
            "direccion": forms.TextInput(attrs={"class": "form-control", "placeholder": "Direccion"}),
            "firs_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Apellido"}),
            "password": forms.PasswordInput(attrs={"class": "form-control", "readonly": "readonly"}),
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre de usuario"}),
        }
