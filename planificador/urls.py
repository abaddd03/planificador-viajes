from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('destinos/', views.lista_destinos, name='lista_destinos'),
    path('destino/<int:destino_id>/', views.detalle_destino, name='detalle_destino'),
    path('planificar/', views.planificar_viaje, name='planificar_viaje'),
    path('planificar/<int:destino_id>/', views.planificar_viaje, name='planificar_viaje_destino'),
]