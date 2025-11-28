from django.conf import settings
from django.db import models


class Autobus(models.Model):
    matricula = models.CharField(max_length=20, unique=True)
    capacidad = models.PositiveIntegerField()
    modelo = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.matricula} ({self.modelo})"


class Conductor(models.Model):
    nombre = models.CharField(max_length=150)
    licencia = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return f"{self.nombre} - {self.licencia}"


class Ruta(models.Model):
    origen = models.CharField(max_length=120)
    destino = models.CharField(max_length=120)
    paradas = models.JSONField(blank=True, default=list, help_text="Lista de paradas intermedias")
    distancia = models.FloatField(help_text="Distancia en km")

    # Relaciones (según diagrama)
    autobus = models.ForeignKey(Autobus, on_delete=models.SET_NULL, null=True, blank=True, related_name="rutas")
    conductor = models.ForeignKey(Conductor, on_delete=models.SET_NULL, null=True, blank=True, related_name="rutas")

    # Campos que sustituyen al modelo Horario
    hora_salida = models.DateTimeField()
    frecuencia = models.CharField(max_length=50, help_text="Ej: Diario, Semanal, Cada 30 min")

    def __str__(self) -> str:
        return f"{self.origen} → {self.destino} ({self.hora_salida:%Y-%m-%d %H:%M})"


class Billete(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="billetes")
    ruta = models.ForeignKey(Ruta, on_delete=models.PROTECT, related_name="billetes")
    asiento = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    codigo_qr = models.CharField(max_length=120, blank=True)

    def __str__(self) -> str:
        return f"Billete #{self.id} - {self.usuario} - {self.ruta}"


class Pago(models.Model):
    billete = models.OneToOneField(Billete, on_delete=models.CASCADE, related_name="pago")
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=30)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    referencia = models.CharField(max_length=100, blank=True)

    def __str__(self) -> str:
        return f"Pago #{self.id} - {self.monto} por {self.billete}"

