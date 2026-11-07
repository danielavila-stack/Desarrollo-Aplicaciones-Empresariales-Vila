function DetalleRecetaItem({
  insumo_nombre,
  cantidad,
  indicaciones_uso,
  insumo_precio,
}) {
  return (
    <li>
      <span>
        {insumo_nombre} × {cantidad}
      </span>
      <span>{indicaciones_uso}</span>
      <span>S/ {Number(insumo_precio).toFixed(2)} c/u</span>
    </li>
  )
}

export default DetalleRecetaItem
