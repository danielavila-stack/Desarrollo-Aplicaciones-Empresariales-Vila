import { useState } from 'react'
import Tarjeta from './Tarjeta.jsx'

function InsumoForm({ onAgregarInsumo }) {
  const [nombre, setNombre] = useState('')
  const [precio, setPrecio] = useState('')
  const [stock, setStock] = useState('')
  const [error, setError] = useState('')

  function handleSubmit(event) {
    event.preventDefault()

    const precioNumerico = Number(precio)
    const stockNumerico = Number(stock)

    if (
      !nombre.trim() ||
      precio === '' ||
      stock === '' ||
      !Number.isFinite(precioNumerico) ||
      precioNumerico <= 0 ||
      !Number.isInteger(stockNumerico) ||
      stockNumerico < 0
    ) {
      setError('Ingresa un nombre, un precio mayor a cero y un stock igual o mayor a cero.')
      return
    }

    onAgregarInsumo({
      nombre: nombre.trim(),
      precio: precioNumerico.toFixed(2),
      stock: stockNumerico,
    })
    setNombre('')
    setPrecio('')
    setStock('')
    setError('')
  }

  return (
    <Tarjeta titulo="Agregar insumo" className="form-section">
      <form className="supply-form" onSubmit={handleSubmit} noValidate>
        <label>
          Nombre
          <input
            className="form-input"
            type="text"
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
            min="0.01"
            step="0.01"
            value={precio}
            onChange={(event) => setPrecio(event.target.value)}
            required
          />
        </label>
        <label>
          Stock
          <input
            className="form-input"
            type="number"
            min="0"
            step="1"
            value={stock}
            onChange={(event) => setStock(event.target.value)}
            required
          />
        </label>
        <button className="submit-button" type="submit">
          Agregar insumo
        </button>
      </form>
      {error && (
        <p className="form-error" role="alert">
          {error}
        </p>
      )}
    </Tarjeta>
  )
}

export default InsumoForm
