# Sistema de Citas Psicológicas — D’VIDA & MENTE

Aplicación web desarrollada en Django para la gestión de citas de consulta psicológica en memoria RAM (sin base de datos/ORM).

## 📌 Problemática
El consultorio psicológico "D’VIDA & MENTE" requiere un sistema ágil para organizar la agenda diaria de pacientes, visualizar los estados de las sesiones y filtrar consultas sin depender de persistencia en base de datos para este módulo temporal.

## 📋 Requisitos Funcionales Implementados
- **RF1:** Registro de nuevas citas con datos del paciente y sesión.
- **RF2:** Listado completo de citas agendadas.
- **RF3:** Categorización por estados (PENDIENTE, CONFIRMADA, COMPLETADA, CANCELADA).
- **RF4:** Vista detallada del motivo de consulta del paciente.
- **RF5:** Contador general y métricas de citas del día.
- **RF6:** Validación de fechas y horas futuras.
- **RF7:** Búsqueda en tiempo real por nombre o apellido del paciente.
- **RF8:** Actualización del estado de la cita en memoria.
- **RF9:** Cancelación o eliminación de citas de la lista temporal.
- **RF10:** Filtrado del listado por fecha específica.
- **RF11:** Validación de formato y longitud en el número telefónico.
- **RF12:** Mensajes emergentes de confirmación al usuario (`django.contrib.messages`).

## 🛠️ Estructura del Proyecto
- **App creada:** `citas`
- **Modelo de datos:** Estructura de listas y diccionarios estáticos (`CITAS_DB`) en `citas/models.py`.

## 🚀 Ejecución del Proyecto
1. Activar el entorno virtual:
   ```bash
   .venv\Scripts\activate