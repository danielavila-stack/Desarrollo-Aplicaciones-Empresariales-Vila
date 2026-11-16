import { useEffect } from "react";

function Aviso({ nombre, onCerrar }) {
  useEffect(() => {
    const temporizador = setTimeout(onCerrar, 3000);

    return () => clearTimeout(temporizador);
  }, [nombre, onCerrar]);

  return (
    <div className="practica-aviso" role="status" aria-live="polite">
      Agregado: {nombre}
    </div>
  );
}

export default Aviso;
