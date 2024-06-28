from django import forms
from .models import Prestamo 

class PrestamoForms(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['rut', 'monto_prestamo', 'cantidad_cuotas', 'id_tipo_prestamo']