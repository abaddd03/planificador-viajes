from django.db import models
from django.contrib.auth.models import User

class Destino(models.Model):
    """Modelo para los destinos turísticos"""
    nombre = models.CharField(max_length=100, verbose_name="Nombre de la ciudad")
    pais = models.CharField(max_length=100, verbose_name="País")
    moneda_local = models.CharField(max_length=3, verbose_name="Moneda local", help_text="Código ISO de 3 letras, ej: EUR, USD, MXN")
    costo_vida_diario = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="Costo de vida diario",
        help_text="Costo estimado por día para una persona"
    )
    descripcion = models.TextField(verbose_name="Descripción", blank=True)

    class Meta:
        verbose_name = "Destino"
        verbose_name_plural = "Destinos"
        ordering = ['costo_vida_diario']

    def __str__(self):
        return f"{self.nombre}, {self.pais}"


class PresupuestoViaje(models.Model):
    """Modelo para el presupuesto de un viaje"""
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='presupuestos', verbose_name="Usuario")
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE, related_name='presupuestos', verbose_name="Destino")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    dias_estimados = models.PositiveIntegerField(verbose_name="Días estimados")
    moneda_usuario = models.CharField(max_length=3, verbose_name="Moneda del usuario")
    tasa_cambio_usada = models.DecimalField(
        max_digits=10, 
        decimal_places=4, 
        verbose_name="Tasa de cambio usada",
        default=1.0
    )
    costo_total_estimado = models.DecimalField(
        max_digits=12, 
        decimal_places=2, 
        verbose_name="Costo total estimado",
        default=0.0
    )

    class Meta:
        verbose_name = "Presupuesto de viaje"
        verbose_name_plural = "Presupuestos de viaje"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"Viaje a {self.destino.nombre} - {self.usuario.username}"


class ItemGasto(models.Model):
    """Modelo para cada gasto específico del viaje"""
    CATEGORIAS = [
        ('VUELO', 'Vuelo'),
        ('ALOJAMIENTO', 'Alojamiento'),
        ('COMIDA', 'Comida'),
        ('TRANSPORTE', 'Transporte'),
        ('OCIO', 'Ocio/Entretenimiento'),
        ('OTROS', 'Otros'),
    ]
    
    presupuesto = models.ForeignKey(PresupuestoViaje, on_delete=models.CASCADE, related_name='items_gasto', verbose_name="Presupuesto")
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, verbose_name="Categoría")
    descripcion = models.CharField(max_length=200, verbose_name="Descripción")
    costo_estimado = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Costo estimado")
    
    class Meta:
        verbose_name = "Item de gasto"
        verbose_name_plural = "Items de gasto"

    def __str__(self):
        return f"{self.get_categoria_display()} - {self.descripcion}: ${self.costo_estimado}"