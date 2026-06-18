from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('planificador.urls')),  # Todas las URLs van a la app planificador
]