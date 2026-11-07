import { useState } from 'react'
import InsumoCard from './InsumoCard.jsx'
import Tarjeta from './Tarjeta.jsx'

function InsumoLista({ insumos }) {
  const [busqueda, setBusqueda] = useState('')
  const insumosFiltrados = insumos.filter((insumo) =>
    insumo.nombre.toLowerCase().includes(busqueda.trim().toLowerCase()),
  )

  return (
    <Tarjeta className="supplies-section">
      <div className="section-heading">
        <div>
          <p className="eyebrow">Control de inventario</p>
          <h2>Insumos de la clínica</h2>
        </div>
        <span className="summary-badge">{insumos.length} insumos</span>
      </div>

      <label className="search-label" htmlFor="buscar-insumo">
        Buscar insumo
      </label>
      <input
        id="buscar-insumo"
        className="form-input search-input"
        type="search"
        value={busqueda}
        onChange={(event) => setBusqueda(event.target.value)}
        placeholder="Escribe el nombre de un insumo"
      />

      {insumosFiltrados.length === 0 ? (
        <p className="empty-state">No se encontraron insumos</p>
      ) : (
        <div className="inventory-grid">
          {insumosFiltrados.map((insumo) => (
            <Tarjeta key={insumo.id} className="supply-card-container">
              <InsumoCard {...insumo} />
            </Tarjeta>
          ))}
        </div>
      )}
    </Tarjeta>
  )
}

export default InsumoLista
