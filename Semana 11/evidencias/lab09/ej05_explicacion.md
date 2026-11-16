# Ejercicio 5: renderizado del inventario

`insumos` es un arreglo escrito manualmente en JavaScript. Cada objeto tiene `id`, `nombre`, `stock` y `precio`; los precios se conservan como texto para imitar la respuesta JSON. `insumos.map()` produce una tarjeta por registro y `key={insumo.id}` ayuda a React a identificar cada elemento al actualizar la lista. `Number(insumo.precio).toFixed(2)` convierte el precio a número y lo presenta con dos decimales.

En el JSX hay un comentario que compara `.map()` con `{% for %}` de Django: ambos permiten repetir contenido para una colección, aunque `.map()` es una operación JavaScript que devuelve elementos React.

## Copia del renderizado del ejercicio

```jsx
{insumos.map((insumo) => (
  <article key={insumo.id}>
    <h2>{insumo.nombre}</h2>
    <p>Stock: {insumo.stock}</p>
    <p>Precio: S/ {Number(insumo.precio).toFixed(2)}</p>
  </article>
))}
```
