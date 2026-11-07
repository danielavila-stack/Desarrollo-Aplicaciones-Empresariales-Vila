import { useState } from 'react'
import './App.css'
import CitaCard from './components/CitaCard.jsx'
import InsumoForm from './components/InsumoForm.jsx'
import InsumoLista from './components/InsumoLista.jsx'
import Tarjeta from './components/Tarjeta.jsx'
import { citasMedicas, clinica, insumos as insumosIniciales, servicios } from './datos.js'

function App() {
  const [insumos, setInsumos] = useState(insumosIniciales)

  function agregarInsumo(nuevoInsumo) {
    setInsumos((prev) => [
      ...prev,
      {
        ...nuevoInsumo,
        id: Math.max(0, ...prev.map((insumo) => insumo.id)) + 1,
      },
    ])
  }

  return (
    <main className="dashboard">
      <header className="dashboard-header">
        <p className="eyebrow">Cuidamos a quienes más quieres</p>
        <h1>🐾 Sistema de Gestión Veterinaria Pet Care 🐾</h1>
        <p>
          Bienvenidos a <strong>{clinica}</strong>, tu clínica veterinaria de
          confianza.
        </p>
      </header>

      <InsumoForm onAgregarInsumo={agregarInsumo} />
      <InsumoLista insumos={insumos} />

      <Tarjeta titulo="Servicios veterinarios">
        <div className="section-heading">
          <p className="eyebrow">Atención profesional</p>
          <span className="summary-badge service-summary">
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
      </Tarjeta>

      <Tarjeta titulo="Historial de Citas Médicas y Recetas Anidadas">
        <div className="section-heading">
          <p className="eyebrow">Atención médica</p>
          <span className="summary-badge">{citasMedicas.length} citas</span>
        </div>
        {citasMedicas.length === 0 ? (
          <p className="empty-state">No hay citas médicas registradas.</p>
        ) : (
          <div className="appointments-list">
            {citasMedicas.map((cita) => (
              <CitaCard key={cita.id} cita={cita} />
            ))}
          </div>
        )}
      </Tarjeta>

      <footer className="dashboard-footer">
        Datos de demostración estáticos para el Laboratorio 10
      </footer>
    </main>
  )
}

export default App
