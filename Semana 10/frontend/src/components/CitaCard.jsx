import DetalleRecetaItem from './DetalleRecetaItem.jsx'

function CitaCard({ cita }) {
  const costoTotal = cita.detalles.reduce(
    (total, detalle) =>
      total + Number(detalle.insumo_precio) * detalle.cantidad,
    0,
  )

  return (
    <article className="appointment-card">
      <div className="appointment-heading">
        <div>
          <h3>🐾 {cita.mascota_nombre}</h3>
          <p className="muted">Dueño: {cita.dueno_nombre}</p>
        </div>
        <span
          className={`status-badge ${cita.estado === 'Atendida' ? 'status-done' : 'status-pending'}`}
        >
          {cita.estado}
        </span>
      </div>
      <p className="appointment-meta">
        {new Date(cita.fecha_hora).toLocaleString('es-PE')} · {cita.motivo}
      </p>
      <h4>Receta médica</h4>
      {cita.detalles.length === 0 ? (
        <p className="empty-state">Esta cita no tiene detalles de receta.</p>
      ) : (
        <ul className="prescription-list">
          {cita.detalles.map((detalle) => (
            <DetalleRecetaItem key={detalle.id} {...detalle} />
          ))}
        </ul>
      )}
      <p className="appointment-total">
        Total general de la receta:{' '}
        <strong>S/ {costoTotal.toFixed(2)}</strong>
      </p>
    </article>
  )
}

export default CitaCard
