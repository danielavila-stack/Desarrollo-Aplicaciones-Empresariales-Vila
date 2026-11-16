import { useEffect } from "react";

function Carrito({ lineas, onQuitar, onVaciar }) {
  const totalUnidades = lineas.reduce(
    (acumulador, linea) => acumulador + linea.cantidad,
    0
  );
  const totalPagar = lineas.reduce(
    (acumulador, linea) =>
      acumulador + Number(linea.precio) * linea.cantidad,
    0
  );

  useEffect(() => {
    console.log("Unidades totales en el carrito:", totalUnidades);
    document.title = `Carrito (${totalUnidades}) — Veterinaria Pet Care`;
  }, [totalUnidades]);

  return (
    <aside className="practica-panel" aria-labelledby="carrito-titulo">
      <h2 id="carrito-titulo">Carrito</h2>

      {lineas.length === 0 && (
        <p className="practica-empty">El carrito está vacío</p>
      )}

      {lineas.length > 0 && (
        <>
          <ul className="carrito-lista">
            {lineas.map((linea) => (
              <li className="carrito-linea" key={linea.id}>
                <div>
                  <h3>{linea.nombre}</h3>
                  <p>
                    Cantidad: {linea.cantidad} × S/{" "}
                    {Number(linea.precio).toFixed(2)}
                  </p>
                  <p>
                    Subtotal: S/{" "}
                    {(Number(linea.precio) * linea.cantidad).toFixed(2)}
                  </p>
                </div>
                <button
                  className="carrito-quitar"
                  type="button"
                  onClick={() => onQuitar(linea.id)}
                  aria-label={`Quitar ${linea.nombre} del carrito`}
                >
                  Quitar
                </button>
              </li>
            ))}
          </ul>

          <div className="carrito-resumen">
            <p>
              Unidades totales: <strong>{totalUnidades}</strong>
            </p>
            <p className="carrito-total">
              Total: <strong>S/ {totalPagar.toFixed(2)}</strong>
            </p>
            <button
              className="practica-button carrito-vaciar"
              type="button"
              onClick={onVaciar}
            >
              Vaciar carrito
            </button>
          </div>
        </>
      )}
    </aside>
  );
}

export default Carrito;
