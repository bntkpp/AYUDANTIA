from django import forms
from .models import Prestamo, Empleado, TipoPrestamo

class EmpleadoForms(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['rut', 'nombre', 'direccion']

class TipoPrestamoForms(forms.ModelForm):
    class Meta:
        model = TipoPrestamo
        fields = ['nombre_tipo_prestamo', 'tasa_interes']

class PrestamoForms(forms.ModelForm):
    tipo_prestamo = forms.ModelChoiceField(queryset = TipoPrestamo.objects.all(), empty_label = 'Seleccione un Tipo de Prestamo')
    rut = forms.ModelChoiceField(queryset = Empleado.objects.all(), empty_label = 'Seleccione un Rut')
    class Meta:
        model = Prestamo
        fields = ['rut', 'monto_prestamo', 'cantidad_cuotas', 'tipo_prestamo']

class TipoPrestamoForms(forms.ModelForm):
    class Meta:
        model = TipoPrestamo
        fields = ['nombre_tipo_prestamo', 'tasa_interes']

