function formatearPrecio(precio) {
  const [entero, decimales = ""] = String(precio).split(".")
  return `${entero}.${decimales.padEnd(2, "0").slice(0, 2)}`
}

function ProductoCard({ producto }) {
  return (
    <article className="producto-card">
      <div>
        <p className="producto-categoria">{producto.categoria_nombre}</p>
        <h3>{producto.nombre}</h3>
      </div>
      <p className="producto-precio">S/ {formatearPrecio(producto.precio)}</p>
      <p className={producto.stock === 0 ? "producto-agotado" : "producto-stock"}>
        {producto.stock === 0 ? "Agotado" : `Stock: ${producto.stock}`}
      </p>
    </article>
  )
}

export default ProductoCard