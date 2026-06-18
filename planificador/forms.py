from django import forms
from .models import Destino, ItemGasto

class PlanificarViajeForm(forms.Form):
    """Formulario para planificar un viaje"""
    destino = forms.ModelChoiceField(
        queryset=Destino.objects.all(),
        label="Destino",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    dias = forms.IntegerField(
        label="Días de viaje",
        min_value=1,
        max_value=30,
        initial=7,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    moneda_usuario = forms.ChoiceField(
        label="Tu moneda",
        choices=[
            ('USD', 'Dólar USA (USD)'),
            ('EUR', 'Euro (EUR)'),
            ('MXN', 'Peso Mexicano (MXN)'),
            ('COP', 'Peso Colombiano (COP)'),
            ('ARS', 'Peso Argentino (ARS)'),
            ('CLP', 'Peso Chileno (CLP)'),
            ('PEN', 'Sol Peruano (PEN)'),
            ('GBP', 'Libra Esterlina (GBP)'),
        ],
        widget=forms.Select(attrs={'class': 'form-select'})
    )

class ItemGastoForm(forms.ModelForm):
    """Formulario para agregar gastos personalizados"""
    class Meta:
        model = ItemGasto
        fields = ['categoria', 'descripcion', 'costo_estimado']
        widgets = {
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Vuelo Madrid-París'}),
            'costo_estimado': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00'}),
        }
        labels = {
            'categoria': 'Categoría',
            'descripcion': 'Descripción',
            'costo_estimado': 'Costo estimado',
        }