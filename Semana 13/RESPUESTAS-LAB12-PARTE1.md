# Laboratorio 12 — Ajax y servicios web (Parte 1)

## Recurso y preparación

Se eligió **Servicio** porque es un recurso sencillo y sin relaciones. Sus campos son `id`, `nombre` (máximo 100 caracteres) y `precio` (decimal, hasta 8 dígitos y 2 decimales). La API valida `precio`: debe ser mayor que cero; si se envía cero o un valor negativo, responde con `400 Bad Request`. El `ServicioViewSet` ofrece búsqueda por nombre con `?search=`.

- Lista: `http://127.0.0.1:8000/api/servicios/`
- Detalle: `http://127.0.0.1:8000/api/servicios/{id}/`
- Levantar Django desde `Semana 12`:

  ```powershell
  cd "C:\Users\Karla\Desktop\DJANGO-4to\Desarrollo-Aplicaciones-Empresariales-Vila\Semana 12"
  python -m venv .venv
  .\.venv\Scripts\python.exe -m pip install -r requirements.txt
  .\.venv\Scripts\python.exe manage.py runserver
  ```

- Levantar React desde otra terminal:

  ```powershell
  cd "C:\Users\Karla\Desktop\DJANGO-4to\Desarrollo-Aplicaciones-Empresariales-Vila\Semana 12\frontend"
  npm install
  npm run dev -- --host localhost
  ```

  Vite muestra la dirección local, normalmente `http://localhost:5173/`.

## Ejercicio 1 — Verificar la API

La tabla muestra los códigos esperados en una operación correcta y los errores comunes:

| Operación | Método HTTP | URL | Código esperado |
|---|---|---|---|
| Listar servicios | GET | `/api/servicios/` | 200 |
| Consultar un servicio | GET | `/api/servicios/{id}/` | 200; 404 si no existe |
| Crear un servicio válido | POST | `/api/servicios/` | 201; 400 si los datos no pasan la validación |
| Actualizar un servicio | PUT o PATCH | `/api/servicios/{id}/` | 200; 400 si los datos no pasan la validación; 404 si no existe |
| Eliminar un servicio | DELETE | `/api/servicios/{id}/` | 204; 404 si no existe |

Para comprobar la validación, se puede intentar crear un servicio con `{"nombre":"Prueba","precio":"0.00"}`. Para buscar se usa, por ejemplo, `/api/servicios/?search=baño`.

**Borrador:** La API devuelve datos en JSON, un formato que otros programas pueden leer y enviar fácilmente. Un Template de Django, en cambio, combina datos con una estructura HTML para mostrar una página. La API entrega los datos separados de la presentación. Así, React puede decidir cómo dibujarlos en el navegador.

**Capturas:** (1) terminal con `python manage.py runserver`; (2) navegador en la URL de lista mostrando la respuesta JSON de DRF; (3) archivo `veterinaria/urls.py` con la ruta del router y `serializers.py` con los campos y validación.

## Ejercicio 2 — CORS (captura antes de configurar)

Antes de habilitar CORS, con Django corriendo y React abierto en `http://localhost:5173/`, abre las herramientas del navegador (F12), selecciona **Console** y ejecuta:

```javascript
fetch('http://127.0.0.1:8000/api/servicios/')
  .then((respuesta) => respuesta.json())
  .then(console.log)
  .catch(console.error)
```

Guarda primero la captura del error que muestre el navegador. La configuración de CORS se añadirá después de obtener esa evidencia, siguiendo la pausa solicitada en el laboratorio.

**Borrador:** El navegador aplica la política de mismo origen para limitar las peticiones entre sitios distintos. El origen incluye protocolo, nombre del servidor y puerto. Aunque React y Django están en la misma computadora, `localhost:5173` y `127.0.0.1:8000` tienen orígenes diferentes, y Django debe autorizar expresamente ese origen.

**Capturas:** (1) navegador con React en `http://localhost:5173/`; (2) consola del navegador mostrando el resultado del `fetch` antes de habilitar CORS; (3) pestaña **Network** con la petición `GET` a `/api/servicios/` y el error visible. El navegador puede marcarla como bloqueada por CORS en vez de mostrar un código HTTP accesible a JavaScript.

## Ejercicio 3 — Axios y `api.js`

`frontend/src/api.js` crea una instancia Axios con la dirección base `http://127.0.0.1:8000/api` y un tiempo límite de 10 segundos. Los componentes usan rutas relativas, por ejemplo, `api.get('/servicios/')`.

**Borrador:** Centralizar la dirección del servidor hace que todos los componentes usen la misma configuración. Si cambia el servidor, se actualiza un solo archivo en vez de buscar y reemplazar la dirección por toda la aplicación. La instancia también permite compartir opciones, como el tiempo límite.

**Capturas:** (1) `frontend/src/api.js` mostrando `axios.create`; (2) terminal con `npm install axios` ya ejecutado dentro de `Semana 12\frontend`; (3) `frontend/package.json` con Axios entre las dependencias.

## Ejercicio 4 — GET con `useEffect`

`ListaPractica.jsx` carga los servicios mediante `api.get`, guarda los datos en estado y los presenta en filas con `key={servicio.id}`.

**Borrador:** `useEffect` sirve para ejecutar la petición cuando aparece la pantalla y cuando cambia la búsqueda, sin repetirla en cada renderizado. La función del efecto no se declara `async` porque React espera que devuelva nada o una función de limpieza, no una promesa. Por eso se declara e invoca dentro una función asíncrona.

**Capturas:** (1) código del `useEffect` y el `map` con la clave basada en el id; (2) página React mostrando los servicios; (3) **Network → Fetch/XHR** con la solicitud `GET /api/servicios/` y su código de respuesta.

## Ejercicio 5 — Estados de carga y error

La pantalla muestra `Cargando...` mientras espera la respuesta, `No se pudo cargar la lista.` si falla la petición y `No hay servicios registrados.` cuando la lista recibida está vacía. Si una búsqueda no encuentra coincidencias, muestra `No se encontraron servicios.`.

**Borrador:** El mensaje de carga avisa que el programa está trabajando. Si hay un error, un texto explica que la lista no se pudo obtener, en vez de dejar la pantalla vacía. Si la respuesta no trae registros, se indica que no hay resultados. Así, la persona puede distinguir entre esperar, un problema y una lista vacía.

**Capturas:** (1) código con los estados `cargando` y `error`, además de `try`, `catch` y `finally`; (2) página mostrando `Cargando...` si se logra capturar durante la petición; (3) página mostrando el mensaje de error con Django temporalmente detenido; (4) página mostrando la lista vacía, si la API no tiene servicios o una búsqueda no devuelve resultados; (5) pestaña **Network** mostrando el método y el estado de la petición correspondiente.

## Ejercicio 6 — POST con formulario controlado

El formulario guarda `nombre` y `precio` en estado. Al crearse un servicio agrega `respuesta.data` usando un arreglo nuevo y limpia los campos. Si el servidor devuelve un error de validación, muestra el detalle del campo o `detail`.

**Borrador:** Un formulario controlado mantiene sus valores en el estado de React, que se actualiza cada vez que la persona escribe. Al enviar, Axios manda esos valores al servidor con POST. Si Django acepta el registro, la respuesta se agrega a la lista y los campos se limpian. Si Django responde con un error, el formulario lo muestra para que se pueda corregir.

**Capturas:** (1) código del formulario controlado y de `api.post`; (2) formulario antes y después de crear correctamente un servicio; (3) **Network** con método `POST`, URL y estado `201`; (4) formulario con precio `0` y mensaje de validación; (5) **Network** con método `POST` y estado `400`.

## Ejercicio 7 — DELETE y PATCH

Cada fila tiene controles de edición y un botón **Eliminar**. PATCH reemplaza el registro correspondiente con `map()` y DELETE lo quita del estado con `filter()` solamente cuando el servidor confirma `204`.

**Borrador:** Al guardar cambios, PATCH envía únicamente los valores editados. Cuando Django devuelve el registro actualizado, React crea una lista nueva y reemplaza en ella el servicio que tiene ese id. Al eliminar, la aplicación espera la respuesta `204` y luego crea otra lista sin ese registro. Estas operaciones actualizan la página sin recargarla.

**Capturas:** (1) código de `api.patch`, `map()` y `api.delete`, `filter()`; (2) fila antes y después de editar; (3) **Network** con método `PATCH` y estado `200`; (4) lista después de eliminar; (5) **Network** con método `DELETE` y estado `204`.

## Ejercicio 8 — Búsqueda y verificación

El campo de búsqueda es controlado. Al cambiar, el efecto solicita la lista usando `params: { search: buscar }`; el backend busca coincidencias en el nombre del servicio.

**Borrador:** React muestra la interfaz y guarda los datos y valores de los formularios. Axios envía cada solicitud HTTP a la API. El ViewSet recibe la ruta y el método, y selecciona la operación de lista, creación, edición o eliminación. El serializer convierte los datos entre JSON y los modelos, y revisa que cumplan las reglas, como exigir un precio mayor que cero. El ORM consulta o modifica los registros en la base de datos. En este proyecto la API todavía está abierta porque no se configuraron autenticación ni permisos; por eso no exige que una persona inicie sesión. Antes de usarla en producción habría que proteger el acceso.

**Capturas:** (1) código del campo controlado, `params: { search: buscar }` y dependencia `[buscar]`; (2) página mostrando los resultados de una búsqueda; (3) **Network** con `GET /api/servicios/?search=...` y estado `200`; (4) terminal donde `npm run lint` termina sin errores ni advertencias; (5) terminal donde `npm run build` finaliza correctamente.

Para verificar desde `Semana 12\frontend`:

```powershell
npm run lint
npm run build
```
