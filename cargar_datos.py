import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'viajes_project.settings')
django.setup()

from planificador.models import Destino

def cargar_destinos():
    destinos = [
        {'nombre': 'París', 'pais': 'Francia', 'moneda_local': 'EUR', 'costo_vida_diario': 120.00, 'descripcion': 'La Ciudad de la Luz, famosa por la Torre Eiffel y el Louvre.'},
        {'nombre': 'Tokio', 'pais': 'Japón', 'moneda_local': 'JPY', 'costo_vida_diario': 150.00, 'descripcion': 'Metrópolis vibrante que combina tradición y tecnología avanzada.'},
        {'nombre': 'Ciudad de México', 'pais': 'México', 'moneda_local': 'MXN', 'costo_vida_diario': 60.00, 'descripcion': 'Capital de México, rica en historia, museos y gastronomía.'},
        {'nombre': 'Barcelona', 'pais': 'España', 'moneda_local': 'EUR', 'costo_vida_diario': 100.00, 'descripcion': 'Ciudad costera con arquitectura modernista y playas.'},
        {'nombre': 'Bangkok', 'pais': 'Tailandia', 'moneda_local': 'THB', 'costo_vida_diario': 45.00, 'descripcion': 'Ciudad exótica con templos y deliciosa comida callejera.'},
        {'nombre': 'Roma', 'pais': 'Italia', 'moneda_local': 'EUR', 'costo_vida_diario': 110.00, 'descripcion': 'La ciudad eterna, hogar del Coliseo y el Vaticano.'},
        {'nombre': 'Buenos Aires', 'pais': 'Argentina', 'moneda_local': 'ARS', 'costo_vida_diario': 50.00, 'descripcion': 'Capital argentina conocida por su arquitectura y el tango.'},
        {'nombre': 'Londres', 'pais': 'Reino Unido', 'moneda_local': 'GBP', 'costo_vida_diario': 130.00, 'descripcion': 'Ciudad global con historia milenaria y museos de clase mundial.'},
        {'nombre': 'Dubái', 'pais': 'Emiratos Árabes Unidos', 'moneda_local': 'AED', 'costo_vida_diario': 200.00, 'descripcion': 'Ciudad futurista con rascacielos y lujo extremo.'},
        {'nombre': 'Sídney', 'pais': 'Australia', 'moneda_local': 'AUD', 'costo_vida_diario': 140.00, 'descripcion': 'Ciudad costera famosa por la Ópera y sus playas.'},
    ]

    for data in destinos:
        destino, created = Destino.objects.get_or_create(
            nombre=data['nombre'],
            defaults=data
        )
        if created:
            print(f"✅ Destino creado: {destino.nombre}")
        else:
            print(f"⏭️ Destino ya existente: {destino.nombre}")

if __name__ == '__main__':
    print("🚀 Cargando destinos turísticos...")
    cargar_destinos()
    print("✅ ¡Carga completada!")