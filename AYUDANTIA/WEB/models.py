from django.db import models

class Empleado(models.Model):
    rut = models.CharField(max_length = 20, primary_key = True)
    nombre = models.CharField(max_length = 50)
    direccion = models.CharField(max_length = 50)
    
class TipoPrestamo(models.Model):
    id_tipo_prestamo = models.AutoField(primary_key = True)
    nombre_tipo_prestamo = models.CharField(max_length = 50)
    tasa_interes = models.IntegerField()

    def calcular_monto_con_interes(self, monto):
        return monto + (monto * self.tasa_interes / 100)

class Prestamo(models.Model):
    id_prestamo = models.AutoField(primary_key = True)
    monto_prestamo = models.IntegerField()
    cantidad_cuotas = models.IntegerField()
    monto_pagar = models.IntegerField()
    rut = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    id_tipo_prestamo = models.ForeignKey(TipoPrestamo, on_delete=models.CASCADE)


class Cuota(models.Model):
    id_prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE)
    numero_cuota = models.AutoField(primary_key = True)
    monto_cuota = models.IntegerField()
    cuota_fecha_emision = models.DateTimeField()
    cuota_fecha_vencimiento = models.DateTimeField()
    cuota_fecha_pago = models.DateTimeField(null=True, blank=True)
    
class Comuna(models.Model): 
    id_comuna = models.AutoField(primary_key = True)
    nombre_comuna = models.CharField(max_length = 50)