function ProductoCard({ producto, onAgregar }) {
  const agotado = producto.stock === 0;

  return (
    <article className="producto-card">
      <h3>{producto.nombre}</h3>
      <p className="producto-precio">
        S/ {Number(producto.precio).toFixed(2)}
      </p>
      <span
        className={`producto-stock ${
          agotado ? "producto-stock-agotado" : "producto-stock-disponible"
        }`}
      >
        {agotado ? "Agotado" : `Stock disponible: ${producto.stock}`}
      </span>
      <button
        className="practica-button"
        type="button"
        disabled={agotado}
        onClick={() => onAgregar(producto)}
      >
        Agregar
      </button>
    </article>
  );
}

export default ProductoCard;
