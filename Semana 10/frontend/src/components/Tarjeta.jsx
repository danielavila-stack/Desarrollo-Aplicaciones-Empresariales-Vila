function Tarjeta({ titulo, children, className = '' }) {
  return (
    <section className={`panel ${className}`.trim()}>
      {titulo && (
        <div className="section-heading">
          <h2>{titulo}</h2>
        </div>
      )}
      {children}
    </section>
  )
}

export default Tarjeta
