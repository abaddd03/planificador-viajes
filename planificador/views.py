from django.shortcuts import render, get_object_or_404, redirect
from .models import Destino, PresupuestoViaje, ItemGasto
from .forms import PlanificarViajeForm, ItemGastoForm
from django.contrib.auth.decorators import login_required
import requests
from decimal import Decimal
from django.contrib import messages

def inicio(request):
    """Página principal con los destinos más populares (los 4 más baratos)"""
    destinos_destacados = Destino.objects.all()[:4]
    context = {
        'destinos_destacados': destinos_destacados,
    }
    return render(request, 'planificador/inicio.html', context)

def lista_destinos(request):
    """Lista completa de todos los destinos"""
    destinos = Destino.objects.all()
    context = {
        'destinos': destinos,
    }
    return render(request, 'planificador/destinos.html', context)

def detalle_destino(request, destino_id):
    """Página de detalle de un destino específico"""
    destino = get_object_or_404(Destino, id=destino_id)
    context = {
        'destino': destino,
    }
    return render(request, 'planificador/detalle_destino.html', context)

def planificar_viaje(request, destino_id=None):
    """Página para planificar un viaje"""
    import os
    from dotenv import load_dotenv
    load_dotenv()
    
    destino = None
    if destino_id:
        destino = get_object_or_404(Destino, id=destino_id)
    
    form = PlanificarViajeForm(initial={'destino': destino} if destino else None)
    gastos_form = ItemGastoForm()
    resultado = None
    gastos = []
    
    if request.method == 'POST':
        if 'calcular' in request.POST:
            # Procesar el formulario principal
            form = PlanificarViajeForm(request.POST)
            if form.is_valid():
                destino = form.cleaned_data['destino']
                dias = form.cleaned_data['dias']
                moneda_usuario = form.cleaned_data['moneda_usuario']
                
                # Calcular costo base (días * costo diario)
                costo_base = Decimal(dias) * destino.costo_vida_diario
                
                # Obtener tasa de cambio REAL desde la API
                tasa_cambio = Decimal('1.0')
                if moneda_usuario != destino.moneda_local:
                    try:
                        api_key = os.getenv('API_KEY_EXCHANGE')
                        url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{destino.moneda_local}"
                        response = requests.get(url)
                        if response.status_code == 200:
                            data = response.json()
                            if data['result'] == 'success':
                                tasa = data['conversion_rates'].get(moneda_usuario)
                                if tasa:
                                    tasa_cambio = Decimal(str(tasa))
                    except Exception as e:
                        # Si hay error, usar tasa 1:1
                        tasa_cambio = Decimal('1.0')
                
                costo_total = costo_base * tasa_cambio
                
                # Si el usuario está autenticado, guardar el presupuesto
                presupuesto = None
                if request.user.is_authenticated:
                    presupuesto = PresupuestoViaje.objects.create(
                        usuario=request.user,
                        destino=destino,
                        dias_estimados=dias,
                        moneda_usuario=moneda_usuario,
                        tasa_cambio_usada=tasa_cambio,
                        costo_total_estimado=costo_total
                    )
                    
                    # Guardar gastos si hay
                    gastos_data = request.POST.getlist('gastos')
                    if gastos_data:
                        for gasto_id in gastos_data:
                            try:
                                gasto = ItemGasto.objects.get(id=gasto_id)
                                gasto.presupuesto = presupuesto
                                gasto.save()
                            except ItemGasto.DoesNotExist:
                                pass
                
                resultado = {
                    'destino': destino,
                    'dias': dias,
                    'moneda_usuario': moneda_usuario,
                    'costo_base': costo_base,
                    'costo_total': costo_total,
                    'tasa_cambio': tasa_cambio,
                    'presupuesto': presupuesto,
                }
        
        elif 'agregar_gasto' in request.POST:
            gastos_form = ItemGastoForm(request.POST)
            if gastos_form.is_valid():
                gasto = gastos_form.save(commit=False)
                gasto.presupuesto = None
                gasto.save()
                messages.success(request, f"Gasto '{gasto.descripcion}' agregado correctamente")
                return redirect('planificar_viaje', destino_id=destino_id if destino_id else None)
    
    # Si hay un destino seleccionado, obtener sus gastos sugeridos
    gastos_sugeridos = []
    if destino:
        gastos_sugeridos = [
            {'categoria': 'VUELO', 'descripcion': f'Vuelo a {destino.nombre}', 'costo_estimado': 500},
            {'categoria': 'ALOJAMIENTO', 'descripcion': f'Hotel en {destino.nombre}', 'costo_estimado': 300},
            {'categoria': 'COMIDA', 'descripcion': 'Comidas diarias', 'costo_estimado': 50},
            {'categoria': 'TRANSPORTE', 'descripcion': 'Transporte local', 'costo_estimado': 30},
            {'categoria': 'OCIO', 'descripcion': 'Turismo y actividades', 'costo_estimado': 40},
        ]
    
    context = {
        'form': form,
        'gastos_form': gastos_form,
        'destino': destino,
        'resultado': resultado,
        'gastos_sugeridos': gastos_sugeridos,
        'titulo': 'Planificar Viaje' if not destino else f'Planificar viaje a {destino.nombre}'
    }
    return render(request, 'planificador/planificar_viaje.html', context)