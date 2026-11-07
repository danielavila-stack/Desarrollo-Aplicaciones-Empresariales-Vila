import { useState } from 'react'

function InsumoCard({ id, nombre, precio, stock = 0 }) {
  const [solicitados, setSolicitados] = useState(0)

  return (
    <article className="item-card" data-insumo-id={id}>
      <div className="item-card-heading">
        <h3>{nombre}</h3>
        <span className="price-badge">S/ {Number(precio).toFixed(2)}</span>
      </div>
      <div className="stock-summary">
        <span
          className={`status-badge ${stock === 0 ? 'status-out' : 'status-available'}`}
        >
          {stock === 0 ? 'Agotado' : 'Disponible'}
        </span>
        <span className="stock-count">
          {stock === 0 ? 'Sin stock' : `Unidades: ${stock}`}
        </span>
      </div>
      {stock <= 5 && (
        <p className="stock-alert">⚠️ Reabastecer urgente</p>
      )}
      <div className="request-row">
        <button
          className="request-button"
          type="button"
          onClick={() => setSolicitados((cantidad) => cantidad + 1)}
          disabled={stock === 0}
        >
          + Solicitar
        </button>
        <span className="stock-count" aria-live="polite">
          Solicitados: {solicitados}
        </span>
      </div>
    </article>
  )
}

export default InsumoCard
