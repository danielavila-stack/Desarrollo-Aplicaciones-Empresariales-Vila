function Buscador({ valor, onCambiar }) {
  return (
    <label className="practica-search" htmlFor="buscador-productos">
      Buscar insumos veterinarios
      <input
        id="buscador-productos"
        type="text"
        value={valor}
        onChange={(e) => onCambiar(e.target.value)}
        placeholder="Escribe el nombre del producto..."
      />
    </label>
  );
}

export default Buscador;
