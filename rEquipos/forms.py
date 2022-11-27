from django import forms
from rEquipos.models import Equipos

class FormEquipo(forms.ModelForm):
    class Meta:
        model=Equipos
        fields='__all__'

    marca = forms.CharField(max_length=50)
    modelo = forms.CharField(max_length=50)
    procesador = forms.CharField(max_length=50)
    grafica = forms.CharField(max_length=50)
    memoria= forms.CharField(max_length=50)
    tipo=forms.CharField(max_length=50)