# 🌍 Planificador de Viajes

Aplicación web para planificar viajes con **conversión de moneda en tiempo real** usando una API externa.

**🔗 Demo:** [Próximamente en PythonAnywhere]

---

## 📋 Descripción

Este proyecto permite a los usuarios:
- Explorar destinos turísticos con información de costos
- Planificar viajes seleccionando destino, días y moneda
- Calcular el presupuesto total con **conversión de moneda REAL**
- Agregar gastos personalizados (vuelo, hotel, comidas, etc.)

---

## 🛠️ Tecnologías utilizadas

- **Python 3.10**
- **Django 5.2**
- **Bootstrap 5** (diseño responsive)
- **ExchangeRate-API** (conversión de moneda en tiempo real)
- **SQLite** (desarrollo)
- **Git & GitHub**

---

## 📊 Modelos de datos

El proyecto utiliza 3 modelos relacionados:

1. **Destino**: Ciudades turísticas con su moneda y costo de vida
2. **PresupuestoViaje**: Presupuestos creados por los usuarios
3. **ItemGasto**: Gastos personalizados dentro de un presupuesto

---

## 🚀 Cómo ejecutar localmente

### 1. Clonar el repositorio
```bash
git clone https://github.com/abaddd03/planificador-viajes.git
cd planificador-viajes