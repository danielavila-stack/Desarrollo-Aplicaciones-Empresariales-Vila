import { useEffect, useState } from 'react'
import api from '../api.js'
import '../App.css'

function mensajeDeError(data) {
  if (typeof data === 'string') return data
  if (!data || typeof data !== 'object') return 'No se pudo completar la operación.'
  if (typeof data.detail === 'string') return data.detail

  return Object.entries(data)
    .flatMap(([campo, errores]) => {
      const lista = Array.isArray(errores) ? errores : [errores]
      return lista
        .filter((error) => typeof error === 'string')
        .map((error) => `${campo}: ${error}`)
    })
    .join(' ')
}

function ServicioFila({ servicio, onGuardar, onEliminar }) {
  // Cada fila controla sus valores de edición sin mutar el registro recibido.
  const [nombre, setNombre] = useState(servicio.nombre)
  const [precio, setPrecio] = useState(String(servicio.precio))

  function guardar(event) {
    event.preventDefault()
    onGuardar(servicio.id, { nombre, precio: Number(precio) })
  }

  return (
    <article className="servicio-fila">
      <form className="servicio-edicion" onSubmit={guardar}>
        <label>
          Nombre
          <input
            className="form-input"
            value={nombre}
            onChange={(event) => setNombre(event.target.value)}
            required
          />
        </label>
        <label>
          Precio (S/)
          <input
            className="form-input"
            type="number"
            step="0.01"
            value={precio}
            onChange={(event) => setPrecio(event.target.value)}
            required
          />
        </label>
        <button className="submit-button" type="submit">
          Guardar cambios
        </button>
        <button
          className="delete-button"
          type="button"
          onClick={() => onEliminar(servicio.id)}
        >
          Eliminar
        </button>
      </form>
    </article>
  )
}

function ListaPractica() {
  // El componente padre conserva la lista y los estados de la pantalla.
  const [servicios, setServicios] = useState([])
  const [cargando, setCargando] = useState(true)
  const [error, setError] = useState('')
  const [errorOperacion, setErrorOperacion] = useState('')
  const [buscar, setBuscar] = useState('')
  const [nombre, setNombre] = useState('')
  const [precio, setPrecio] = useState('')

  useEffect(() => {
    const controlador = new AbortController()

    // La petición de lista se ejecuta al montar y cuando cambia la búsqueda.
    async function cargarServicios() {
      setCargando(true)
      setError('')

      try {
        const respuesta = await api.get('/servicios/', {
          params: { search: buscar },
          signal: controlador.signal,
        })
        setServicios(respuesta.data)
      } catch (err) {
        if (!controlador.signal.aborted) {
          console.error('Error al cargar los servicios:', err)
          setError('No se pudo cargar la lista.')
        }
      } finally {
        if (!controlador.signal.aborted) setCargando(false)
      }
    }

    cargarServicios()
    return () => controlador.abort()
  }, [buscar])

  async function crearServicio(event) {
    event.preventDefault()
    setErrorOperacion('')

    try {
      const respuesta = await api.post('/servicios/', {
        nombre,
        precio: Number(precio),
      })
      setServicios((actuales) => [...actuales, respuesta.data])
      setNombre('')
      setPrecio('')
    } catch (err) {
      console.error('Error al crear el servicio:', err)
      setErrorOperacion(mensajeDeError(err.response?.data))
    }
  }

  async function guardarServicio(id, cambios) {
    setErrorOperacion('')

    try {
      const respuesta = await api.patch(`/servicios/${id}/`, cambios)
      setServicios((actuales) =>
        actuales.map((servicio) => (servicio.id === id ? respuesta.data : servicio)),
      )
    } catch (err) {
      console.error(`Error al actualizar el servicio ${id}:`, err)
      setErrorOperacion(mensajeDeError(err.response?.data))
    }
  }

  async function eliminarServicio(id) {
    setErrorOperacion('')

    try {
      const respuesta = await api.delete(`/servicios/${id}/`)
      if (respuesta.status === 204) {
        setServicios((actuales) => actuales.filter((servicio) => servicio.id !== id))
      }
    } catch (err) {
      console.error(`Error al eliminar el servicio ${id}:`, err)
      setErrorOperacion(mensajeDeError(err.response?.data))
    }
  }

  return (
    <main className="dashboard">
      <header className="dashboard-header">
        <p className="eyebrow">Laboratorio 12 · Ajax y servicios web</p>
        <h1>Servicios veterinarios</h1>
        <p>Consulta y administra servicios usando la API de Django REST Framework.</p>
      </header>

      <section className="panel" aria-labelledby="crear-titulo">
        <h2 id="crear-titulo">Registrar servicio</h2>
        <form className="supply-form" onSubmit={crearServicio}>
          <label>
            Nombre
            <input
              className="form-input"
              value={nombre}
              onChange={(event) => setNombre(event.target.value)}
              required
            />
          </label>
          <label>
            Precio (S/)
            <input
              className="form-input"
              type="number"
              step="0.01"
              value={precio}
              onChange={(event) => setPrecio(event.target.value)}
              required
            />
          </label>
          <button className="submit-button" type="submit">
            Crear servicio
          </button>
        </form>
        {errorOperacion && <p className="form-error" role="alert">{errorOperacion}</p>}
      </section>

      <section className="panel" aria-labelledby="lista-titulo">
        <div className="section-heading">
          <h2 id="lista-titulo">Lista de servicios</h2>
          <span className="summary-badge">{servicios.length} servicios</span>
        </div>
        <label className="search-label search-input">
          Buscar por nombre
          <input
            className="form-input"
            value={buscar}
            onChange={(event) => setBuscar(event.target.value)}
            placeholder="Escribe para buscar..."
          />
        </label>

        {cargando ? (
          <p className="empty-state">Cargando...</p>
        ) : error ? (
          <p className="form-error" role="alert">{error}</p>
        ) : servicios.length === 0 ? (
          <p className="empty-state">
            {buscar ? 'No se encontraron servicios.' : 'No hay servicios registrados.'}
          </p>
        ) : (
          <div className="servicios-lista">
            {servicios.map((servicio) => (
              <ServicioFila
                key={servicio.id}
                servicio={servicio}
                onGuardar={guardarServicio}
                onEliminar={eliminarServicio}
              />
            ))}
          </div>
        )}
      </section>
      <footer className="dashboard-footer">Práctica de solicitudes Ajax con Axios</footer>
    </main>
  )
}

export default ListaPractica
