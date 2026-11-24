# Laboratorio 13 — Parte 1 (Ejercicios 1 al 8)

## Contexto

Este laboratorio plantea la evolución de **Veterinaria Pet Care**, una tienda en línea de vacunas, antipulgas, shampoos medicados, alimentos especializados e insumos veterinarios. React se encarga de la interfaz y Django REST Framework (DRF) de exponer los datos y aplicar las reglas del servidor.

## Ejercicio 1 — Tipo de comercio y canales

| Tipo (B2C, B2B, C2C) | Quién vende a quién | Ejemplo peruano |
|---|---|---|
| B2C (Business to Consumer) | Una empresa vende directamente a una persona consumidora. | Platanitos vende calzado a consumidores mediante sus canales comerciales. |
| B2B (Business to Business) | Una empresa vende productos o servicios a otra empresa. | Alicorp comercializa productos de consumo masivo con bodegas y otros negocios minoristas. |
| C2C (Consumer to Consumer) | Una persona vende a otra persona, normalmente mediante una plataforma intermediaria. | En Mercado Libre Perú, una persona puede publicar un artículo y venderlo a otra persona. |

**Veterinaria Pet Care es B2C:** la tienda vende productos veterinarios a las personas responsables de sus mascotas. En el futuro, si la tienda ofreciera compras por volumen a clínicas o veterinarias, esa relación con empresas sería B2B; no cambia el modelo principal descrito aquí.

La web, una aplicación móvil y las redes sociales pueden consumir **la misma API REST de Django**. Cada canal envía solicitudes HTTP y recibe respuestas JSON: por ejemplo, la web y la app pueden consultar el catálogo con `GET`, y una integración autorizada puede iniciar un pedido con `POST`. La API centraliza los datos y las validaciones para que los canales no mantengan catálogos o precios independientes.

*M-commerce* describe una compra hecha mediante un dispositivo móvil; *social commerce* describe el canal o contexto de compra desde una red social. Son formas de acceder al comercio, no tipos de relación entre vendedor y comprador: ambas pueden seguir siendo B2C.

## Ejercicio 2 — Módulos y roles

### Mapa de módulos y planificación

```text
Veterinaria Pet Care
├── S14: Catálogo ─── Carrito ─── Usuarios y roles
├── S15: Pedidos ─── Pagos ─── Inventario
└── S16: Panel administrativo ─── Seguridad ─── Notificaciones
```

La distribución S14–S16 es una planificación propuesta para construir el flujo por etapas, no una afirmación de que esos módulos ya estén implementados.

| Semana | Módulos | Alcance |
|---|---|---|
| S14 | Catálogo, carrito, usuarios y roles | Consultar productos veterinarios, reunirlos temporalmente en el carrito y distinguir visitante, cliente y administrador. |
| S15 | Pedidos, pagos e inventario | Registrar pedidos, integrar una pasarela tokenizada y validar/actualizar existencias. |
| S16 | Panel administrativo, seguridad y notificaciones | Gestionar productos y pedidos, reforzar permisos y comunicar cambios de estado. |

### Roles

| Rol | Qué puede hacer | Qué pantalla usa |
|---|---|---|
| Visitante | Explorar y buscar productos, ver precios y añadir productos a un carrito temporal. Para confirmar una compra debe identificarse. | Inicio, catálogo y carrito. |
| Cliente | Administrar sus datos, confirmar compras y consultar únicamente sus pedidos y estados. | Catálogo, carrito, checkout y «Mis pedidos». |
| Administrador | Gestionar productos, existencias y pedidos; consultar el panel con operaciones de la tienda. | Panel administrativo y gestión de catálogo/inventario/pedidos. |

Los permisos se validan en Django; ocultar una opción en la interfaz de React no sustituye la autorización del servidor.

## Ejercicio 3 — Requisitos

### Requisitos funcionales

| ID | Descripción | Prioridad | Criterio de aceptación |
|---|---|---|---|
| RF-01 | El sistema permite consultar y buscar vacunas, antipulgas, shampoos medicados, alimentos especializados e insumos por nombre o categoría. | Alta | Una búsqueda devuelve solo los productos que coinciden y cada resultado muestra nombre, precio y disponibilidad. |
| RF-02 | El cliente puede añadir, cambiar cantidades y quitar productos de su carrito. | Alta | Al cambiar una cantidad, el subtotal mostrado se actualiza y no se aceptan cantidades menores que uno. |
| RF-03 | El cliente autenticado puede confirmar una compra con sus datos de entrega. | Alta | Al aceptar una solicitud válida, Django crea un pedido asociado al cliente con sus líneas y total. |
| RF-04 | El cliente puede consultar sus pedidos y el estado de cada uno. | Media | La consulta devuelve solo pedidos del cliente autenticado, junto con fecha, total y estado. |
| RF-05 | El administrador puede crear, actualizar y desactivar productos y gestionar existencias. | Alta | Un administrador autorizado puede guardar los cambios; un usuario sin permiso recibe una respuesta de acceso denegado. |

### Requisitos no funcionales

| ID | Descripción | Prioridad | Criterio de aceptación |
|---|---|---|---|
| RNF-01 | La API debe responder a las operaciones de lectura del catálogo dentro del umbral de latencia definido para el laboratorio. | Media | En una prueba local de 20 solicitudes consecutivas con datos de prueba, cada `GET` del catálogo termina en menos de 1 segundo. |
| RNF-02 | El sistema debe usar HTTPS en producción y no almacenar números ni códigos de seguridad de tarjetas. | Alta | La configuración de producción redirige/rechaza HTTP y la inspección de la base de datos y registros no encuentra PAN ni CVV. |
| RNF-03 | Las operaciones protegidas deben requerir autenticación y permisos de rol validados por el servidor. | Alta | Una solicitud anónima o de rol insuficiente recibe `401` o `403`, según corresponda. |
| RNF-04 | Los importes se deben representar con precisión decimal y validarse en el servidor. | Alta | Las pruebas con precios de dos decimales verifican el total exacto, sin errores binarios de redondeo. |
| RNF-05 | La interfaz debe adaptarse a pantallas móviles y de escritorio. | Media | El catálogo y el checkout pueden usarse a 360 px y 1280 px de ancho sin desplazamiento horizontal de la página. |

Los **requisitos funcionales** especifican qué servicios o acciones ofrece el sistema (por ejemplo, crear un pedido). Los **no funcionales** describen cualidades, restricciones o niveles verificables de esos servicios (por ejemplo, seguridad, compatibilidad y rendimiento).

La frase vaga *«El sistema debe ser rápido y seguro»* se descompone en requisitos comprobables:

1. **Rendimiento:** «Con 20 solicitudes consecutivas en el entorno local de prueba, cada `GET /api/productos/` debe responder en menos de 1 segundo». El límite se mide con una prueba de carga/tiempo; para producción debe confirmarse y ajustarse con datos reales.
2. **Seguridad:** «En producción, las rutas de pedidos requieren autenticación; las solicitudes anónimas reciben `401`, y el servidor nunca persiste el número completo de tarjeta ni el CVV». Se verifica con pruebas de permisos y revisión de persistencia y registros.

## Ejercicio 4 — Flujo de compra y arquitectura

### Arquitectura

```text
┌─────────────────────┐    HTTP/JSON     ┌────────────────────────┐
│ React (web/móvil)   │ ◄──────────────► │ API REST con DRF       │
└─────────────────────┘                  └───────────┬────────────┘
                                                      │ reglas/servicios
                                                      ▼
                                           ┌──────────────────────┐
                                           │ Django               │
                                           └──────────┬───────────┘
                                                      │ ORM
                                                      ▼
                                           ┌──────────────────────┐
                                           │ SQLite (desarrollo)  │
                                           └──────────────────────┘
                                                      │
             Django/DRF ── solicitud segura ─────────┴──► Pasarela de pago
             Django/DRF ◄── token y confirmación/webhook ─ Pasarela de pago
```

React intercambia recursos serializados en JSON mediante HTTP. DRF valida y convierte las solicitudes/respuestas; Django aplica las reglas de negocio y usa el ORM para consultar la base de datos. En el flujo de pago, el proveedor devuelve un token de pago y una confirmación o rechazo; no se envían datos de tarjeta desde React a Django.

### Pasos del pedido

| Paso | Qué hace React | Qué hace Django | Estado del pedido |
|---|---|---|---|
| 1. Explorar | Solicita y presenta productos, precios y disponibilidad. | Consulta los productos activos y devuelve datos del catálogo en JSON. | Aún no existe pedido. |
| 2. Preparar carrito | Mantiene cantidades seleccionadas temporalmente y presenta un subtotal orientativo. | Todavía no registra un pedido; no confía en precios ni disponibilidad enviados por el navegador. | Carrito temporal; aún no existe pedido. |
| 3. Confirmar compra | Envía productos/cantidades y datos de entrega; no envía precios como autoridad. | Vuelve a leer precios y stock desde la base de datos, valida cantidades y crea el pedido. | `pendiente_pago`. |
| 4. Pagar | Abre el checkout seguro del proveedor y recibe un token/resultado; no recopila ni transmite el PAN/CVV a Django. | Envía o verifica el token con la pasarela y valida su respuesta o webhook. | `pendiente_pago` mientras se procesa. |
| 5. Aceptar pago | Muestra la confirmación del proveedor. | Al confirmar el pago, registra la transacción, actualiza stock dentro de una operación consistente y confirma el pedido. | `confirmado` / `en preparación`. Si se rechaza, queda `pago rechazado` o pendiente para reintento, según la política. |
| 6. Preparar y entregar | Muestra las actualizaciones del pedido al cliente. | Registra los cambios de estado y la información de despacho. | `en preparación` → `enviado` → `entregado`. |

**Tarjetas y PCI-DSS:** la tienda debe integrar un proveedor de pago que capture los datos en su checkout o campos alojados y aplique tokenización. El proveedor procesa el número de tarjeta; Django recibe solo un token y el resultado de la operación. Así se evita que la aplicación guarde PAN o CVV, se reduce la exposición de datos sensibles y se limita el alcance de cumplimiento PCI-DSS. La tokenización no elimina las responsabilidades de seguridad restantes de la tienda.

## Ejercicio 5 — Reglas de negocio y errores comunes

| Regla | Dónde se aplica (React o Django) | Qué error evita |
|---|---|---|
| El precio vigente se obtiene desde la base de datos; nunca se acepta como autoridad el precio enviado por el navegador. | Django; React solo lo presenta. | Manipular el precio desde las herramientas del navegador o cobrar un precio desactualizado. |
| Antes de confirmar el pedido, Django comprueba que la cantidad solicitada no supere el stock disponible y vuelve a comprobarlo al actualizar existencias. | Django; React puede mostrar una disponibilidad preliminar. | Vender productos sin existencias o permitir que compras concurrentes sobrevendan el inventario. |
| Los importes se calculan y persisten con `Decimal` (por ejemplo, `DecimalField`), no con `float`. | Django; React muestra los valores recibidos sin ser fuente del total final. | Errores de precisión binaria y diferencias en subtotales o totales monetarios. |
| La aplicación no almacena número completo de tarjeta ni código de seguridad; utiliza token de una pasarela. | Integración de pago en Django y checkout alojado del proveedor; React no guarda esos datos. | Exposición de datos sensibles y aumento innecesario del alcance de PCI-DSS. |
| El carrito es una selección temporal del cliente; el pedido es un registro histórico persistido en la base de datos. | Carrito: React (o almacenamiento temporal acotado). Pedido: Django/BD. | Tratar cambios del carrito como compra confirmada o perder el historial/transacción del cliente. |

El stock no puede controlarse únicamente en React: el navegador puede manipularse, conservar datos obsoletos o tener varias sesiones de compra activas al mismo tiempo. Django debe consultar y actualizar la cantidad en el servidor, con una operación consistente y validación al confirmar la compra.

## Ejercicio 6 — Proyecto y aplicaciones Django

Un **proyecto Django** es la configuración global del sitio: ajustes, base de datos, middleware y enrutamiento raíz (en este caso, el paquete `config`). Una **aplicación** agrupa una parte funcional reutilizable y sus modelos, vistas, rutas y migraciones. Por eso `catalogo` organiza el dominio de productos y `pedidos` el de compras, mientras ambas apps se registran en el proyecto de Semana 13.

En la carpeta que contiene `manage.py` se ejecutaron:

```powershell
python manage.py startapp catalogo
python manage.py startapp pedidos
python manage.py check
```

`catalogo` y `pedidos` se añadieron a `INSTALLED_APPS`, conservando `rest_framework`, `corsheaders` y `veterinaria.apps.VeterinariaConfig`. La comprobación de Django terminó con **System check identified no issues (0 silenced)**.

## Ejercicio 7 — Estructura de React

Estructura relevante de `frontend/src`:

```text
src/
├── App.css
├── App.jsx
├── api.js
├── assets/
├── components/
│   ├── CitaCard.jsx
│   ├── DetalleRecetaItem.jsx
│   ├── InsumoCard.jsx
│   ├── InsumoForm.jsx
│   ├── InsumoLista.jsx
│   ├── ProductoCard.jsx       (nuevo, vacío)
│   └── Tarjeta.jsx
├── datos.js
├── index.css
├── main.jsx
├── pages/
│   └── ProductosPage.jsx      (nuevo, vacío)
└── practica/
```

`components/` contiene piezas reutilizables de interfaz: las tarjetas y formularios existentes de citas/insumos se conservan; `ProductoCard.jsx` queda como espacio para la futura tarjeta del catálogo. `pages/` agrupa pantallas completas que combinan componentes; `ProductosPage.jsx` queda como marcador para la futura pantalla. `api.js` centraliza la instancia Axios, la URL base `http://127.0.0.1:8000/api/` y un tiempo límite de 10 segundos para las solicitudes.

## Ejercicio 8 — Mapa de rutas y compilación

Las rutas de React son páginas que el navegador muestra. Las rutas de Django son endpoints HTTP que reciben métodos como `GET` o `POST`, validan datos y devuelven respuestas —normalmente JSON—. Una ruta de interfaz no reemplaza permisos ni validaciones de la API.

| Recurso | Ruta de la API de Django (propuesta) | Ruta de React |
|---|---|---|
| Catálogo de productos | `/api/productos/` | `/productos` |
| Carrito | `/api/carrito/` (si se persiste/sincroniza en servidor; el borrador puede ser local) | `/carrito` |
| Pedidos del cliente | `/api/pedidos/` | `/mis-pedidos` |
| Servicios veterinarios | `/api/servicios/` | `/servicios` |
| Insumos e inventario | `/api/insumos/` | `/admin/inventario` |
| Administración de productos | `/api/productos/` (con autorización de administrador) | `/admin/productos` |
| Pago | `/api/pagos/` (inicia/verifica el flujo tokenizado) | `/checkout` |

Las rutas de productos, carrito, pedidos, pagos y las pantallas React son el mapa previsto para las siguientes etapas; esta Parte 1 no las implementa. **Nota sobre el enrutamiento actual:** el router DRF existente incluye servicios, citas e insumos dentro de `veterinaria/urls.py`, y `config/urls.py` lo monta bajo `veterinaria/`; por eso, hoy la ruta real de servicios es `/veterinaria/api/servicios/` (análogamente para citas e insumos). La tabla muestra el contrato raíz `/api/...` propuesto para el mapa del laboratorio; antes de consumir esos endpoints desde la interfaz, el enrutamiento Django debe alinearse con ese contrato.

Desde `Semana 13/frontend` se ejecutó:

```powershell
npm run build
```

El comando terminó sin errores y Vite compiló los 77 módulos. La compilación comprueba que Vite puede empaquetar el código de React, pero no sustituye las pruebas de la API ni de las reglas de negocio.
