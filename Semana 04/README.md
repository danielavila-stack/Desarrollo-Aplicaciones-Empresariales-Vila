# Sistema de Gestión Veterinaria 


 Este sistema gestiona el flujo operativo de una clínica veterinaria aplicando persistencia con **Django ORM**, base de datos **SQLite**, y una interfaz moderna con **Bootstrap 5**.

---
##  Integrantes
- Vila Ramos Daniela Fransua
- Chavez Lazo Karla Estefany


---

##  Resumen del Laboratorio 

### Integridad de Base de Datos y Modelado
- Definición de relaciones clave del dominio veterinario:
  - **1:1 (`OneToOneField`)**: `PerfilVeterinario` con `User` y `FichaMedica` con `Mascota`.
  - **1:N (`ForeignKey`)**: `Especie` a `Mascota`, y `Mascota`/`PerfilVeterinario` a `CitaMedica`.
  - **N:M (`ManyToManyField` con `through`)**: `CitaMedica` e `Insumo` a través del modelo intermedio `DetalleReceta`.

### Diseño e Interfaz UI/UX con Bootstrap 5
- Migración de vistas básicas HTML a un diseño web profesional utilizando **Bootstrap 5 (CSS, JS e Icons)**.
- Implementación de plantillas reutilizables (`base.html`), barras de navegación responsivas, tablas estilizables y formularios interactivos (`*_form.html`, `*_list.html`).

###  Ciclo de Vida CRUD en Relación N:M
- Implementación de operaciones completas sobre la tabla intermedia `DetalleReceta`:
  - **Agregar**: Vincular un insumo a una cita médica definiendo **atributos propios** (`cantidad` e `indicaciones_uso`).
  - **Modificar**: Actualizar la dosis o las indicaciones de uso de un detalle de receta existente.
  - **Quitar**: Eliminar la prescripción de un insumo dentro de una cita médica sin alterar los registros base de `CitaMedica` ni de `Insumo`.

---

## Diagrama Entidad-Relación:
<img width="1232" height="1078" alt="Captura de pantalla 2026-09-13 193354" src="https://github.com/user-attachments/assets/4e4af117-4c92-412b-9077-84bcd65f2cad" />
