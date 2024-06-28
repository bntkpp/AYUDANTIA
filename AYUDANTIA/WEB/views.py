from django.shortcuts import render, redirect, get_object_or_404
from .models import Prestamo, Cuota, TipoPrestamo
from .forms import PrestamoForms
from datetime import datetime, timedelta

def registrar_prestamo(request):
    if request.method == "POST":
        form = PrestamoForms(request.POST)
        if form.is_valid():
            prestamo = form.save(commit=False)
            tipo_prestamo = prestamo.id_tipo_prestamo
            prestamo.monto_pagar = tipo_prestamo.calcular_monto_con_interes(prestamo.monto_prestamo)
            prestamo.save()

            # Generar cuotas
            cuotas = []
            for i in range(prestamo.cantidad_cuotas):
                cuota = Cuota(
                    id_prestamo=prestamo,
                    monto_cuota=prestamo.monto_pagar / prestamo.cantidad_cuotas,
                    cuota_fecha_emision=datetime.now(),
                    cuota_fecha_vencimiento=datetime.now() + timedelta(days=30 * (i + 1))
                )
                cuota.save()
                cuotas.append(cuota)

            return render(request, 'registrar_prestamo.html', {
                'form': form,
                'monto_pagar': prestamo.monto_pagar,
                'cuotas': cuotas
            })
    else:
        form = PrestamoForms()
    return render(request, 'registrar_prestamo.html', {'form': form})

def listar_prestamo(request):
    prestamo = Prestamo.objects.all()
    return render(request, 'listar_prestamo.html', {'prestamo': prestamo})
