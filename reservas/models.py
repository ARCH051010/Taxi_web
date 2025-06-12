from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    ci = models.CharField(max_length=11, unique=True)
    contacto = models.CharField(max_length=8)

    class Meta:
        db_table = 'reservas_cliente'

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Conductor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    ci = models.CharField(max_length=11, unique=True)
    contacto = models.CharField(max_length=8)
    marca_carro = models.CharField(max_length=50)
    disponible = models.BooleanField(default=True)

    class Meta:
        db_table = 'reservas_conductor'

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Reservacion(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    destino = models.CharField(max_length=255)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE)

    class Meta:
        db_table = 'reservas_reservacion'

    def __str__(self):
        return f"Reserva para {self.cliente} el {self.fecha}"
