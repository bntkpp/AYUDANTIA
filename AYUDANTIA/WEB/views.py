from django.shortcuts import render, redirect
from .models import Prestamo, Cuota, TipoPrestamo, Empleado
from .forms import PrestamoForms, EmpleadoForms, TipoPrestamoForms
from datetime import datetime, timedelta

def registrar_empleado(request):
    if request.method == "POST":
        form = EmpleadoForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_prestamo')
    else:
        form = EmpleadoForms()
    return render(request, 'registrar_empleado.html', {'form': form})

def registrar_tipo_prestamo(request):
    if request.method == "POST":
        form = TipoPrestamoForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_prestamo')
    else:
        form = TipoPrestamoForms()
    return render(request, 'registrar_tipo_prestamo.html', {'form': form})

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


