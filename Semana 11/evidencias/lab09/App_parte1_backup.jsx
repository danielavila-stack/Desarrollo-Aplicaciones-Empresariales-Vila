import './App.css'

const clinica = 'Veterinaria Pet Care'

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
        <p className="eyebrow">Panel de control</p>
        <h1 style={{ color: '#174f45' }}>
          🐾 Veterinaria Pet Care - Panel de Control 🐾
        </h1>
        <p>Bienvenidos a {clinica}. El precio del servicio con IGV es S/ {(50 * 1.18).toFixed(2)}.</p>
      </header>

      <section className="panel" aria-labelledby="insumos-title">
        <div className="section-heading">
          <div>
            <p className="eyebrow">Inventario</p>
            <h2 id="insumos-title">Insumos disponibles</h2>
          </div>
          <span className="summary-badge">{insumos.length} productos</span>
        </div>

        {insumos.length === 0 ? (
          <p className="empty-state">No hay insumos registrados</p>
        ) : (
          <div className="inventory-grid">
            {/* .map() cumple un rol similar al {% for %} de Django. */}
            {insumos.map((insumo) => {
              const stock = insumo.stock

              return (
                <article className="item-card" key={insumo.id}>
                  <div className="item-card-heading">
                    <h3>{insumo.nombre}</h3>
                    <span className="price-badge">
                      S/ {Number(insumo.precio).toFixed(2)}
                    </span>
                  </div>
                  <p className="stock-line">
                    {stock === 0 ? 'Agotado' : `Stock: ${stock}`}
                  </p>
                  {stock > 0 && stock <= 5 && (
                    <span className="stock-alert">⚠️ ¡Últimas unidades!</span>
                  )}
                </article>
              )
            })}
          </div>
        )}
      </section>

      <section className="panel" aria-labelledby="appointments-title">
        <div className="section-heading">
          <div>
            <p className="eyebrow">Atención médica</p>
            <h2 id="appointments-title">Citas y recetas</h2>
          </div>
          <span className="summary-badge">{citasMedicas.length} citas</span>
        </div>

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
                    <h3>{cita.mascota_nombre}</h3>
                    <p className="muted">Dueño: {cita.dueno_nombre}</p>
                  </div>
                  <span
                    className={`status-badge ${cita.estado === 'Atendida' ? 'status-done' : 'status-pending'}`}
                  >
                    {cita.estado}
                  </span>
                </div>
                <p>
                  {new Date(cita.fecha_hora).toLocaleString('es-PE')} · {cita.motivo}
                </p>
                <h4>Receta</h4>
                <ul className="prescription-list">
                  {cita.detalles.map((detalle) => (
                    <li key={detalle.id}>
                      <span>
                        {detalle.insumo_nombre} × {detalle.cantidad}
                      </span>
                      <span>{detalle.indicaciones_uso}</span>
                    </li>
                  ))}
                </ul>
                <p className="appointment-total">
                  Costo total de insumos: S/ {costoTotal.toFixed(2)}
                </p>
              </article>
            )
          })}
        </div>
      </section>
    </main>
  )
}

export default App
