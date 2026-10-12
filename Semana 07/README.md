# Pet Care - Sistema de Gestión de Clínica Veterinaria

## Laboratorio 07: Optimización y Manejo Avanzado del ORM en Django

Este repositorio contiene la implementación del **Laboratorio 07** para el sistema de clínica veterinaria **Pet Care**. El objetivo principal de este laboratorio fue optimizar el rendimiento de la base de datos, garantizar la integridad transaccional en operaciones críticas y encapsular la lógica de negocio mediante el ORM de Django.

---

## Aspectos Clave Implementados

### 1. Transacciones Atómicas e Integridad de Datos
* **Ubicación:** `recetas/views.py` (o `citas/views.py`)
* **Implementación:** Se utilizó `@transaction.atomic` y bloques `with transaction.atomic():` para procesar la emisión de recetas médicas.
* **Expresiones F():** Se implementaron para realizar el descuento de stock directamente en la base de datos (`F('stock') - cantidad`), evitando problemas de concurrencia y garantizando que si no existe stock suficiente, la transacción realice un *rollback* completo.

### 2. Reportes Analíticos con Agregaciones y Anotaciones
* **Ubicación:** `reportes/views.py` / `citas/views.py`
* **Agregaciones (`aggregate()`):** Para el cálculo de totales globales en el inventario (ej. suma de stock total con `Sum('stock')`), devolviendo un resumen estructurado en formato diccionario.
* **Anotaciones (`annotate()`):** Uso del equivalente a `GROUP BY` en SQL para calcular métricas por objeto, como el total de citas por mascota (`Count('citas')`) y el conteo de citas agrupadas por su estado (*Pendiente*, *Atendida*, *Completado*).

### 3. QuerySets Personalizados y Reutilización de Código (DRY)
* **Ubicación:** `citas/models.py`
* **Clase Creada:** `CitaMedicaQuerySet` (hereda de `models.QuerySet`).
* **Métodos de Negocio:**
  * `.completadas()`: Filtra las citas en estado "Completado" o "Atendida".
  * `.del_mes()`: Filtra las citas programadas dentro del mes y año en curso.
* **Vinculación:** Se asignó al modelo mediante `objects = CitaMedicaQuerySet.as_manager()`, permitiendo encadenar búsquedas limpias como `CitaMedica.objects.completadas().del_mes()`.

### 4. Diagnóstico y Solución del Problema N+1
* **Ubicación:** `citas/views.py`
* **Diagnóstico:** Se monitoreó el número de peticiones a la base de datos utilizando `django.db.connection` y `connection.queries`.
* **Optimización:** Se reemplazó la consulta básica por `CitaMedica.objects.select_related('mascota', 'veterinario')`, realizando un `INNER JOIN` en SQL que redujo drásticamente el volumen de peticiones (de $N + 1$ consultas a **1 sola consulta SQL**).

---

## Estructura del Proyecto

```text
petcare_project/
├── citas/
│   ├── models.py      # Modelo CitaMedica y CitaMedicaQuerySet
│   ├── views.py       # Optimización con select_related y monitoreo de consultas
│   └── urls.py
├── recetas/
│   ├── models.py      # Modelos Insumo y Receta
│   ├── views.py       # Transacciones atómicas y expresiones F()
│   └── urls.py
├── reportes/
│   └── views.py       # Agregaciones (aggregate) y Anotaciones (annotate)
├── manage.py
└── README.md
