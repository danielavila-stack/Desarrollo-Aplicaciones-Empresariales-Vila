# Semana 05 - Laboratorio: Personalización de Django Admin

Proyecto de desarrollo web en Django para la gestión de una clínica veterinaria, enfocado en la personalización avanzada del panel de administración (`django.contrib.admin`).
## INTEGRANTES:
- Vila Ramos Daniela
- Chavez Lazo Karla
## Descripción del Proyecto

Este laboratorio implementa la configuración del panel administrativo para 10 entidades del modelo de datos de la clínica veterinaria, optimizando la visualización, filtrado, búsqueda y gestión de relaciones entre modelos.

---

## Tecnologías y Requisitos

- **Lenguaje:** Python
- **Framework:** Django
- **Base de Datos:** SQLite 3
- **Librerías:** Especificadas en `requirements.txt`

---

## Funcionalidades e Implementaciones (Parte 1 y Parte 2)

### 1. Registros y Personalización de ModelAdmin
Se personalizaron las vistas principales utilizando clases derivadas de `admin.ModelAdmin` con los siguientes atributos:
- **`list_display`**: Muestra campos clave en formato de tabla para entidades como `Mascota`, `CitaMedica`, `PerfilVeterinario`, `Factura`, `HistorialMedico`, entre otros.
- **`search_fields`**: Habilita barras de búsqueda por atributos relevantes (ej. nombre de mascota, dueño, código de chip, colegiatura).
- **`list_filter`**: Agrega filtros laterales por estado, fechas, grupo sanguíneo y otros campos categóricos.

### 2. Implementación de Inlines (Relaciones entre modelos)
- **`StackedInline` (Relación 1:1):** Integración de `FichaMedica` dentro del formulario de `Mascota`.
- **`TabularInline` (Relación N:M):** Integración de la tabla intermedia `DetalleReceta` dentro del formulario de `CitaMedica`.

### 3. Verificación de Persistencia CRUD
- Pruebas de Creación, Lectura, Edición y Borrado (CRUD) ejecutadas directamente desde el panel de administración, validando la integridad referencial y persistencia de datos en SQLite.

---
## RESULTADO:
<img width="1630" height="622" alt="image" src="https://github.com/user-attachments/assets/016f9219-d767-46d5-8d84-158d2a9e89f2" />

## Instrucciones de Ejecución

1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/danielavila-stack/Desarrollo-Aplicaciones-Empresariales-Vila.git](https://github.com/danielavila-stack/Desarrollo-Aplicaciones-Empresariales-Vila.git)
