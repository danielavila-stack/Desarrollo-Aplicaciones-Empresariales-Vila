# Sistema de Gestión Veterinaria — Pet Care (Semana 11)

Aplicación frontend desarrollada en **React + Vite** enfocada en la **comunicación entre componentes**, elevación del estado (*Lifting State Up*), cálculo de datos derivados y manejo del ciclo de vida con `useEffect`.

## Estructura del Proyecto

- `frontend/src/practica/`: Mini catálogo interactivo con carrito de compras y buscador compartido desarrollado para la **Parte 1** del laboratorio.
- `frontend/src/components/`: Componentes modulares del **Panel Administrativo de Veterinaria Pet Care** (**Parte 2**)[cite: 1].

## Descripción de la Pantalla del Panel Administrativo

La pantalla principal del panel gestiona el inventario de **insumos y productos veterinarios** de Pet Care bajo una arquitectura de flujo de datos unidireccional[cite: 1]:

- **Componente Padre (Estado Elevado):** Centraliza la lista de registros en un único `useState`, el texto del filtro de búsqueda y las funciones inmutables (`spread`, `map`, `filter`) para agregar, actualizar estado/stock y eliminar registros[cite: 1].
- **Listado y Filas (`InsumoLista` / Fila):** Reciben los registros filtrados por *props* y renderizan cada elemento con su `key` única. Cada fila incluye botones de acción que notifican eventos al padre mediante funciones *callback*[cite: 1].
- **Formulario de Alta (`InsumoForm`):** Formulario controlado con validaciones de campos obligatorios y valores numéricos positivos antes de enviar el nuevo registro al padre vía `onGuardar`[cite: 1].
- **Resumen Derivado:** Componente hermano del listado que calcula métricas en tiempo real (total de registros, unidades en stock o conteo por estado) sin duplicar estados con `useState`[cite: 1].
- **Buscador Compartido:** Campo de texto controlado que actualiza el filtro en el componente padre para actualizar dinámicamente los resultados mostrados en el listado[cite: 1].
- **Ciclo de Vida (`useEffect`):** Sincronización dinámica del título de la pestaña del navegador (`document.title`) y notificaciones temporales con limpieza de temporizadores (`clearTimeout`)[cite: 1].

## Ejecución Local

```bash
cd "Semana 11/frontend"
npm install
npm run dev
```


## Captura Final
<img width="1251" height="840" alt="image" src="https://github.com/user-attachments/assets/fa398258-358d-45e7-9d7e-1394034152ff" />
