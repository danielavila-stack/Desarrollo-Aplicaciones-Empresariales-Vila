# Ejercicio 3: estructura del proyecto React

## Archivos principales

- **`index.html`** es el documento HTML inicial que entrega Vite. Contiene el elemento `<div id="root"></div>` donde React monta la aplicación y carga `src/main.jsx`. En Django, el navegador recibe una plantilla HTML renderizada por el servidor; aquí el HTML funciona como una base mínima para la interfaz.
- **`src/main.jsx`** es el punto de entrada de JavaScript: importa los estilos globales y `App.jsx`, crea la raíz React sobre `#root` y renderiza el componente. Puede compararse con el inicio del flujo de presentación de Django, aunque la vista Django genera HTML en el servidor y este punto de entrada activa la interfaz en el navegador.
- **`src/App.jsx`** contiene el componente principal de React y su interfaz declarada con JSX. Se parece en propósito a una plantilla Django porque define lo que se muestra, pero usa JavaScript y expresiones JSX en vez de etiquetas de plantilla como `{{ variable }}` y `{% for %}`.
- **`package.json`** registra los metadatos, dependencias y comandos npm del frontend (`dev`, `build`, `lint`). Cumple una función de manifiesto del proyecto JavaScript. En Django, `requirements.txt` cumple una función relacionada para declarar paquetes Python, aunque los ecosistemas y gestores de dependencias son distintos.
- **`node_modules/`** contiene las dependencias JavaScript instaladas por npm para este proyecto, incluidas React y Vite. No es código de la aplicación ni se versiona. En Django, el equivalente conceptual son los paquetes disponibles en el entorno Python (por ejemplo, un entorno virtual), no una carpeta `node_modules`.

## Estructura

La estructura completa, excluyendo dependencias instaladas (`node_modules`) y artefactos de compilación (`dist`), está en [`ej03_estructura.txt`](./ej03_estructura.txt).
