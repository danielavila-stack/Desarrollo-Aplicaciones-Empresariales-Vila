# Ejercicio 9: tabla de equivalencias de la investigación

La API de la Semana 08 se monta bajo `/veterinaria/api/` en el servidor Django (`http://127.0.0.1:8000`). Los campos corresponden a los serializadores REST y los modelos del proyecto.

| Entidad / concepto | Campos JSON principales | Representación / regla | Endpoint de la API |
|---|---|---|---|
| `Insumo` | `id`, `nombre`, `stock`, `precio` | `precio` se entrega como decimal; `stock` es entero. `stock: 0` se muestra como “Sin Stock”; si hay pocas unidades se avisa reabastecer. | `GET/POST /veterinaria/api/insumos/`; `GET/PUT/PATCH/DELETE /veterinaria/api/insumos/{id}/` |
| `Servicio` | `id`, `nombre`, `precio` | El precio debe ser mayor que cero en la validación del serializador. | `GET/POST /veterinaria/api/servicios/`; `GET/PUT/PATCH/DELETE /veterinaria/api/servicios/{id}/` |
| `CitaMedica` | `id`, `mascota`, `mascota_nombre`, `veterinario`, `veterinario_colegiatura`, `fecha_hora`, `motivo`, `estado` | El serializador estándar representa las relaciones mediante sus identificadores e incluye nombres de lectura. | `GET/POST /veterinaria/api/citas/`; `GET/PUT/PATCH/DELETE /veterinaria/api/citas/{id}/` |
| `CitaMedica` con receta anidada | `id`, `mascota`, `mascota_nombre`, `dueno_nombre`, `fecha_hora`, `motivo`, `estado`, `detalles` | Cada elemento de `detalles` incluye `id`, `insumo`, `insumo_nombre`, `cantidad`, `indicaciones_uso`, `insumo_precio`. El costo por cita es la suma de `cantidad × insumo_precio`. | `GET /veterinaria/api/citas-completas/`; `GET /veterinaria/api/citas-completas/{id}/` |
| `estado` de la cita | `estado` (texto) | Valor inicial del modelo: `Pendiente`. La lógica de citas completadas acepta `Completado` o `Atendida`. | Se incluye en `/veterinaria/api/citas/` y `/veterinaria/api/citas-completas/`. |
| `estado` del inventario | `stock` (entero) | No existe un campo `estado` separado en `Insumo`: la interfaz calcula “Disponible” cuando `stock > 0` y “Sin Stock” cuando `stock === 0`. | `/veterinaria/api/insumos/` |

Los métodos enumerados proceden de los `ModelViewSet` (CRUD) y del `ReadOnlyModelViewSet` (solo lectura) registrados con `DefaultRouter` en la API de Django. En esta parte del laboratorio se usan objetos estáticos de JavaScript con esa forma; no se realizan solicitudes HTTP.
