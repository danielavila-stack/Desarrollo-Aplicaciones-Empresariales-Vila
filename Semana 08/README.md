# Sistema de Gestión Veterinaria — API REST (Semana 08)

Este proyecto corresponde a la migración y estandarización del sistema de gestión veterinaria a una arquitectura **API RESTful** construida sobre **Django REST Framework (DRF)**.

---

## Características Principales e Implementaciones

1. **Estandarización con ViewSets y DefaultRouter:**
   - Exposición de endpoints bajo el prefijo unificado `/api/`.
   - Uso de `ModelViewSet` para operaciones CRUD completas y `ReadOnlyModelViewSet` para consultas protegidas.

2. **Validación Personalizada de Datos:**
   - Implementación de reglas `validate_<campo>` a nivel de serializador (ej. validación de stock positivo en `InsumoSerializer`).

3. **Optimización de Rendimiento en Base de Datos (N+1 Query Issue):**
   - Reducción de **25 a 3 consultas SQL** mediante el uso estratégico de `select_related()` (relaciones FK) y `prefetch_related()` (relaciones $1:N$ anidadas).

4. **Filtros Avanzados y Búsqueda:**
   - Integración de `SearchFilter` y `OrderingFilter` para búsquedas por texto y ordenamientos múltiples.
   - Filtrado dinámico mediante parámetros en URL (`?estado=`).

5. **Acciones Personalizadas (`@action`):**
   - Creación de endpoints a medida que reutilizan lógica de negocio de la capa de modelos (`CitaMedicaQuerySet.completadas().del_mes()`).

---

## Endpoints Disponibles de la API

| Recurso | Tipo de ViewSet | Funcionalidades / Filtros | Endpoint |
| :--- | :--- | :--- | :--- |
| **Servicios** | `ModelViewSet` | Búsqueda (`?search=`) y Ordenamiento (`?ordering=`) | `/api/servicios/` |
| **Insumos** | `ModelViewSet` | Validación en `stock` (`validate_stock`) | `/api/insumos/` |
| **Citas Médicas** | `ModelViewSet` | Gestión CRUD estándar de citas | `/api/citas/` |
| **Citas Completas** | `ReadOnlyModelViewSet` | Datos anidados optimizados con `select_related` / `prefetch_related` | `/api/citas-completas/` |
| **Filtro Estado** | `ReadOnlyModelViewSet` | Filtro dinámico por parámetro | `/api/citas-completas/?estado=COMPLETADO` |
| **Acción Del Mes** | `@action` personalizado | Reutilización de QuerySet `.completadas().del_mes()` | `/api/citas-completas/del-mes/` |

---

## Benchmark de Rendimiento SQL

* **Sin Optimización:** 25 consultas SQL execution (Problema N+1)
* **Con Optimización (`select_related` + `prefetch_related`):** 3 consultas SQL
* **Reducción del Impacto:** ~88% de consultas eliminadas en el servidor.

---
## Pruebas
<img width="1447" height="716" alt="Captura de pantalla 2026-10-11 140158" src="https://github.com/user-attachments/assets/7dc9bffb-8c9a-42d1-ab02-ace4a38809e1" />
<img width="1425" height="711" alt="Captura de pantalla 2026-10-11 140306" src="https://github.com/user-attachments/assets/a3986852-3eaf-46c3-8010-d6c78e0eeed0" />
<img width="1420" height="687" alt="Captura de pantalla 2026-10-11 140357" src="https://github.com/user-attachments/assets/a004ef3a-dc73-4245-bd71-516caf73fc07" />

