import { useEffect, useState } from "react"

import api from "../api.js"
import ProductoCard from "../components/ProductoCard.jsx"
import "../App.css"

function ProductosPage() {
  const [productos, setProductos] = useState([])
  const [cargando, setCargando] = useState(true)
  const [error, setError] = useState("")

  useEffect(() => {
    const controlador = new AbortController()

    async function cargarProductos() {
      try {
        const respuesta = await api.get("productos/", {
          signal: controlador.signal,
        })
        setProductos(respuesta.data)
      } catch (errorPeticion) {
        if (!controlador.signal.aborted) {
          setError(
            errorPeticion.response
              ? "No se pudieron cargar los productos de la veterinaria."
              : "No se pudo conectar con Django. Verifica que el servidor esté encendido.",
          )
        }
      } finally {
        if (!controlador.signal.aborted) setCargando(false)
      }
    }

    cargarProductos()
    return () => controlador.abort()
  }, [])

  return (
    <main className="dashboard">
      <header className="dashboard-header">
        <p className="eyebrow">Veterinaria Pet Care</p>
        <h1>Productos veterinarios</h1>
        <p>Antiparasitarios, vacunas, alimentos y cuidado para tus mascotas.</p>
      </header>

      <section className="panel" aria-labelledby="productos-titulo">
        <div className="section-heading">
          <h2 id="productos-titulo">Catálogo</h2>
          <span className="summary-badge">{productos.length} productos</span>
        </div>

        {cargando ? (
          <p className="empty-state" role="status">Cargando productos...</p>
        ) : error ? (
          <p className="form-error" role="alert">{error}</p>
        ) : productos.length === 0 ? (
          <p className="empty-state">No hay productos veterinarios registrados.</p>
        ) : (
          <div className="productos-lista">
            {productos.map((producto) => (
              <ProductoCard key={producto.id} producto={producto} />
            ))}
          </div>
        )}
      </section>
      <footer className="dashboard-footer">Tienda en línea · Veterinaria Pet Care</footer>
    </main>
  )
}

export default ProductosPage