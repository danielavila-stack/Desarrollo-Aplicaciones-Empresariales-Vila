# Semana 06: Refactorización de Plantillas, Arquitectura Modular y Seguridad en Django

Este módulo corresponde al **Laboratorio 06** de la aplicación de Gestión Veterinaria. En esta etapa se refactorizó la capa de presentación (UI) aplicando herencia de plantillas, reutilización de componentes con `{% include %}` y auditoría de seguridad contra vulnerabilidades web nativas (CSRF y XSS).

---

## Vista Previa de la Aplicación

<img width="1357" height="412" alt="image" src="https://github.com/user-attachments/assets/329d4bfd-ff2d-455a-90e2-9b516ba198fb" />
*Figura 1: Vista relacional de Citas e Insumos recetados (Modelo Intermedio N:M) utilizando herencia de templates y componentes de Bootstrap.*

<img width="1335" height="396" alt="image" src="https://github.com/user-attachments/assets/27751cd2-b757-4a73-83fa-c43ae114979e" />
*Figura 2: Listado general de entidades con alertas y botones de acción.*

---

## Aspectos Clave Implementados

### 1. Arquitectura de Plantillas (DRY)
- **Plantilla Base (`veterinaria/base.html`):** Centralización de la estructura HTML5, estilos de Bootstrap 5, barra de navegación (`navbar`) y bloques dinámicos (`{% block title %}` y `{% block content %}`).
- **Modularización (`{% include %}`):** Abstracción del componente reutilizable de alertas/notificaciones (`_mensaje_alerta.html`) para evitar duplicación de código en los listados y formularios.

### 2. Seguridad Nativa Auditada
- **Protección CSRF:** Inclusión obligatoria del token `{% csrf_token %}` en el 100% de los formularios del sistema (`POST`).
- **Auto-Escape XSS:** Verificación de la neutralización automática de scripts maliciosos en la renderización de datos ingresados por el usuario.

---

## Entidades Integradas y Auditadas

| # | Entidad | Plantillas Principales | Relación / Descripción |
| :-: | :--- | :--- | :--- |
| 1 | **Mascota** | `mascota_list.html`, `mascota_form.html` | Registro e historial de pacientes. |
| 2 | **Cita** | `cita_list.html` | Agenda y consultas médicas. |
| 3 | **Especie** | `especie_list.html`, `especie_form.html` | Clasificación de mascotas. |
| 4 | **Historial Médico** | `historialmedico_list.html`, `historialmedico_form.html` | Antecedentes clínicos. |
| 5 | **Insumo** | `insumo_list.html`, `insumo_form.html` | Catálogo de medicamentos/materiales. |
| 6 | **Servicio** | `servicio_list.html`, `servicio_form.html` | Catálogo de atención médica. |
| 7 | **Receta / Detalle** | `receta_list.html`, `detalle_list.html`, `detalle_form.html` | Modelo intermedio $N:M$ entre Citas e Insumos. |

---
