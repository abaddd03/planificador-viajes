from django.contrib import admin
from .models import Destino, PresupuestoViaje, ItemGasto

@admin.register(Destino)
class DestinoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'pais', 'moneda_local', 'costo_vida_diario']
    search_fields = ['nombre', 'pais']
    list_filter = ['pais']

@admin.register(PresupuestoViaje)
class PresupuestoViajeAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'destino', 'fecha_creacion', 'dias_estimados', 'costo_total_estimado']
    search_fields = ['usuario__username', 'destino__nombre']
    list_filter = ['destino', 'fecha_creacion']

@admin.register(ItemGasto)
class ItemGastoAdmin(admin.ModelAdmin):
    list_display = ['presupuesto', 'categoria', 'descripcion', 'costo_estimado']
    search_fields = ['descripcion']
    list_filter = ['categoria']