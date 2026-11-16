import ProductoCard from "./ProductoCard.jsx";

function Catalogo({ productos, onAgregar }) {
  return (
    <section className="practica-panel" aria-labelledby="catalogo-titulo">
      <h2 id="catalogo-titulo">Catálogo de insumos</h2>
      {productos.length === 0 ? (
        <p className="practica-empty">No hay productos que coincidan</p>
      ) : (
        <div className="producto-grid">
          {productos.map((producto) => (
            <ProductoCard
              key={producto.id}
              producto={producto}
              onAgregar={onAgregar}
            />
          ))}
        </div>
      )}
    </section>
  );
}

export default Catalogo;
