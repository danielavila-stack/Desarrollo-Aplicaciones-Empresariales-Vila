import './App.css'

const clinica = 'Veterinaria Pet Care'

const servicios = [
  { id: 1, nombre: 'Consulta general', precio: '50.00' },
  { id: 2, nombre: 'Vacunación', precio: '42.00' },
  { id: 3, nombre: 'Desparasitación', precio: '35.90' },
  { id: 4, nombre: 'Baño medicado', precio: '65.00' },
  { id: 5, nombre: 'Control veterinario', precio: '30.00' },
]

const insumos = [
  { id: 1, nombre: 'Alimento para cachorro', stock: 18, precio: '25.50' },
  { id: 2, nombre: 'Vacuna antirrábica', stock: 4, precio: '42.00' },
  { id: 3, nombre: 'Antipulgas', stock: 0, precio: '35.90' },
  { id: 4, nombre: 'Vendas', stock: 3, precio: '8.75' },
  { id: 5, nombre: 'Shampoo medicado', stock: 12, precio: '19.99' },
]

const citasMedicas = [
  {
    id: 101,
    mascota: 1,
    mascota_nombre: 'Luna',
    dueno_nombre: 'María Torres',
    fecha_hora: '2026-10-18T09:30:00',
    motivo: 'Control general',
    estado: 'Atendida',
    detalles: [
      {
        id: 1,
        insumo: 2,
        insumo_nombre: 'Vacuna antirrábica',
        cantidad: 1,
        indicaciones_uso: 'Aplicar una dosis.',
        insumo_precio: '42.00',
      },
      {
        id: 2,
        insumo: 4,
        insumo_nombre: 'Vendas',
        cantidad: 2,
        indicaciones_uso: 'Usar para proteger la zona tratada.',
        insumo_precio: '8.75',
      },
    ],
  },
  {
    id: 102,
    mascota: 2,
    mascota_nombre: 'Max',
    dueno_nombre: 'José Ramírez',
    fecha_hora: '2026-10-19T11:00:00',
    motivo: 'Tratamiento antipulgas',
    estado: 'Pendiente',
    detalles: [
      {
        id: 3,
        insumo: 3,
        insumo_nombre: 'Antipulgas',
        cantidad: 1,
        indicaciones_uso: 'Administrar según indicación veterinaria.',
        insumo_precio: '35.90',
      },
    ],
  },
]

function App() {
  return (
    <main className="dashboard">
      <header className="dashboard-header">
        <p className="eyebrow">Cuidamos a quienes más quieres</p>
        <h1 style={{ color: '#1e3d34' }}>
          🐾 Sistema de Gestión Veterinaria Pet Care 🐾
        </h1>
        <p>
          Bienvenidos a <strong>{clinica}</strong>, tu clínica veterinaria de
          confianza.
        </p>
      </header>

      <section className="panel" aria-labelledby="services-title">
        <div className="section-heading">
          <div>
            <p className="eyebrow">Atención profesional</p>
            <h2 id="services-title">Servicios veterinarios</h2>
          </div>
          <span className="summary-badge" style={{ backgroundColor: '#e8f4ff' }}>
            {servicios.length} servicios
          </span>
        </div>

        {servicios.length === 0 ? (
          <p className="empty-state">No hay servicios registrados.</p>
        ) : (
          <div className="inventory-grid">
            {servicios.map((servicio) => (
              <article className="item-card service-card" key={servicio.id}>
                <div className="item-card-heading">
                  <h3>🩺 {servicio.nombre}</h3>
                  <span className="price-badge">
                    S/ {Number(servicio.precio).toFixed(2)}
                  </span>
                </div>
              </article>
            ))}
          </div>
        )}
      </section>

      <section className="panel" aria-labelledby="supplies-title">
        <div className="section-heading">
          <div>
            <p className="eyebrow">Control de inventario</p>
            <h2 id="supplies-title">Insumos de la clínica</h2>
          </div>
          <span className="summary-badge">
            {insumos.length} insumos
          </span>
        </div>

        {insumos.length === 0 ? (
          <p className="empty-state">No hay insumos registrados.</p>
        ) : (
          <div className="inventory-grid">
            {insumos.map((insumo) => (
              <article className="item-card" key={insumo.id}>
                <div className="item-card-heading">
                  <h3>{insumo.nombre}</h3>
                  <span className="price-badge">
                    S/ {Number(insumo.precio).toFixed(2)}
                  </span>
                </div>
                <div className="stock-summary">
                  <span
                    className={`status-badge ${insumo.stock === 0 ? 'status-out' : 'status-available'}`}
                    style={{
                      borderRadius: '12px',
                      padding: '7px 12px',
                    }}
                  >
                    {insumo.stock === 0 ? 'Agotado' : 'Disponible'}
                  </span>
                  <span className="stock-count">
                    {insumo.stock === 0
                      ? 'Sin Stock'
                      : `Unidades: ${insumo.stock}`}
                  </span>
                </div>
                {insumo.stock <= 5 && (
                  <p className="stock-alert">⚠️ Reabastecer Urgente</p>
                )}
              </article>
            ))}
          </div>
        )}
      </section>

      <section className="panel" aria-labelledby="appointments-title">
        <div className="section-heading">
          <div>
            <p className="eyebrow">Atención médica</p>
            <h2 id="appointments-title">
              Historial de Citas Médicas y Recetas Anidadas
            </h2>
          </div>
          <span className="summary-badge">
            {citasMedicas.length} citas
          </span>
        </div>

        {citasMedicas.length === 0 ? (
          <p className="empty-state">No hay citas médicas registradas.</p>
        ) : (
          <div className="appointments-list">
            {citasMedicas.map((cita) => {
              const costoTotal = cita.detalles.reduce(
                (total, detalle) =>
                  total + Number(detalle.insumo_precio) * detalle.cantidad,
                0,
              )

              return (
                <article className="appointment-card" key={cita.id}>
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
                    {new Date(cita.fecha_hora).toLocaleString('es-PE')} ·{' '}
                    {cita.motivo}
                  </p>
                  <h4>Receta médica</h4>
                  {cita.detalles.length === 0 ? (
                    <p className="empty-state">Esta cita no tiene detalles de receta.</p>
                  ) : (
                    <ul className="prescription-list">
                      {cita.detalles.map((detalle) => (
                        <li key={detalle.id}>
                          <span>
                            {detalle.insumo_nombre} × {detalle.cantidad}
                          </span>
                          <span>{detalle.indicaciones_uso}</span>
                          <span>
                            S/ {Number(detalle.insumo_precio).toFixed(2)} c/u
                          </span>
                        </li>
                      ))}
                    </ul>
                  )}
                  <p className="appointment-total">
                    Total general de la receta:{' '}
                    <strong>S/ {costoTotal.toFixed(2)}</strong>
                  </p>
                </article>
              )
            })}
          </div>
        )}
      </section>
      <footer className="dashboard-footer">
        Datos de demostración estáticos para el Laboratorio 09
      </footer>
    </main>
  )
}

export default App
