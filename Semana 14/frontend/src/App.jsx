import { useState } from "react"

import ListaPractica from './practica/ListaPractica.jsx'
import ProductosPage from "./pages/ProductosPage.jsx"

function App() {
  const [vista, setVista] = useState("productos")

  return (
    <>
      <nav className="app-nav" aria-label="Secciones de Veterinaria Pet Care">
        <button
          type="button"
          aria-pressed={vista === "productos"}
          onClick={() => setVista("productos")}
        >
          Productos
        </button>
        <button
          type="button"
          aria-pressed={vista === "servicios"}
          onClick={() => setVista("servicios")}
        >
          Servicios veterinarios
        </button>
      </nav>
      {vista === "productos" ? <ProductosPage /> : <ListaPractica />}
    </>
  )
}

export default App
