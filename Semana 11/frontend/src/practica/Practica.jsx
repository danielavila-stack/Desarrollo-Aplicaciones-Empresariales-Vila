import { useState } from "react";
import "./Practica.css";
import Aviso from "./Aviso.jsx";
import Buscador from "./Buscador.jsx";
import Carrito from "./Carrito.jsx";
import Catalogo from "./Catalogo.jsx";
import { productos } from "./datos.js";

function Practica() {
  const [carrito, setCarrito] = useState([]);
  const [busqueda, setBusqueda] = useState("");
  const [aviso, setAviso] = useState(null);

  const productosFiltrados = productos.filter((producto) =>
    producto.nombre.toLowerCase().includes(busqueda.toLowerCase())
  );

  function agregarAlCarrito(producto) {
    setCarrito((prevCarrito) => {
      const yaExiste = prevCarrito.some((linea) => linea.id === producto.id);

      if (yaExiste) {
        return prevCarrito.map((linea) =>
          linea.id === producto.id
            ? { ...linea, cantidad: linea.cantidad + 1 }
            : linea
        );
      }

      return [...prevCarrito, { ...producto, cantidad: 1 }];
    });

    setAviso({ nombre: producto.nombre, id: Date.now() });
  }

  function quitarDelCarrito(id) {
    setCarrito((prevCarrito) =>
      prevCarrito.filter((linea) => linea.id !== id)
    );
  }

  function vaciarCarrito() {
    setCarrito([]);
  }

  function cerrarAviso() {
    setAviso(null);
  }

  return (
    <main className="practica-dashboard">
      <header className="practica-header">
        <p className="practica-eyebrow">Cuidamos a quienes más quieres</p>
        <h1>Veterinaria Pet Care</h1>
        <p>Catálogo de insumos y compras para el cuidado de tus mascotas.</p>
      </header>

      {aviso && (
        <Aviso
          key={aviso.id}
          nombre={aviso.nombre}
          onCerrar={cerrarAviso}
        />
      )}

      <Buscador valor={busqueda} onCambiar={setBusqueda} />

      <div className="practica-layout">
        <Catalogo
          productos={productosFiltrados}
          onAgregar={agregarAlCarrito}
        />
        <Carrito
          lineas={carrito}
          onQuitar={quitarDelCarrito}
          onVaciar={vaciarCarrito}
        />
      </div>
    </main>
  );
}

export default Practica;
