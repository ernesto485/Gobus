from django.contrib import admin

from .models import Autobus, Conductor, Ruta, Billete, Pago


@admin.register(Autobus)
class AutobusAdmin(admin.ModelAdmin):
    list_display = ("matricula", "modelo", "capacidad")
    search_fields = ("matricula", "modelo")


@admin.register(Conductor)
class ConductorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "licencia")
    search_fields = ("nombre", "licencia")


@admin.register(Ruta)
class RutaAdmin(admin.ModelAdmin):
    list_display = ("origen", "destino", "hora_salida", "frecuencia", "autobus", "conductor", "distancia")
    list_filter = ("frecuencia", "hora_salida")
    search_fields = ("origen", "destino")
    autocomplete_fields = ("autobus", "conductor")


@admin.register(Billete)
class BilleteAdmin(admin.ModelAdmin):
    list_display = ("id", "usuario", "ruta", "asiento", "precio", "fecha_compra")
    list_filter = ("fecha_compra",)
    search_fields = ("usuario__username", "ruta__origen", "ruta__destino")
    autocomplete_fields = ("usuario", "ruta")


@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ("id", "billete", "monto", "metodo_pago", "fecha_pago")
    list_filter = ("metodo_pago", "fecha_pago")
    search_fields = ("billete__usuario__username", "billete__id", "referencia")
    autocomplete_fields = ("billete",)

