# Ejercicio 8: estilos, React y API REST

## Diferencia entre React (SPA) y los Templates de Django

React renderiza la interfaz en el navegador a partir de componentes y actualiza las partes necesarias cuando cambia el estado o los datos. En una SPA, la aplicación suele cargar una página base y la navegación/actualización de vistas ocurre principalmente en el cliente.

Los Templates de Django se procesan en el servidor: una vista prepara el contexto, Django inserta esos valores en la plantilla y responde con HTML. Para cada solicitud de página el servidor puede volver a generar la vista. React y los Templates resuelven la presentación en lugares distintos (navegador y servidor, respectivamente).

## ¿Qué falta para consumir la API REST?

En esta parte los arreglos están escritos manualmente y no se usa `fetch` ni HTTP. Para consumir la API hace falta conocer y configurar la URL disponible, habilitar CORS en Django si frontend y backend usan distinto origen, y hacer solicitudes HTTP desde React (por ejemplo con `fetch` o una biblioteca cliente). También hay que manejar carga, errores y respuestas vacías, y mapear/validar los datos recibidos. Para operaciones de escritura se deben enviar los métodos y datos adecuados y resolver autenticación/permisos y CSRF según la configuración del backend.

## Evidencias de validación

- [`ej08_lint.txt`](./ej08_lint.txt): salida de `npm run lint`.
- [`ej08_build.txt`](./ej08_build.txt): salida de `npm run build`.
