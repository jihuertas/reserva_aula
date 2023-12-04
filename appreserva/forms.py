from django import forms
from .models import ReservaAula

class ReservaAulaForm(forms.ModelForm):
    class Meta:
        model = ReservaAula
        fields = ['aula', 'fecha_inicio', 'fecha_fin', 'nombre_reservante', 'email_reservante']
        