export const clinica = 'Veterinaria Pet Care'

export const servicios = [
  { id: 1, nombre: 'Consulta general', precio: '50.00' },
  { id: 2, nombre: 'Vacunación', precio: '42.00' },
  { id: 3, nombre: 'Desparasitación', precio: '35.90' },
  { id: 4, nombre: 'Baño medicado', precio: '65.00' },
  { id: 5, nombre: 'Control veterinario', precio: '30.00' },
]

export const insumos = [
  { id: 1, nombre: 'Alimento para cachorro', stock: 18, precio: '25.50' },
  { id: 2, nombre: 'Vacuna antirrábica', stock: 4, precio: '42.00' },
  { id: 3, nombre: 'Antipulgas', stock: 0, precio: '35.90' },
  { id: 4, nombre: 'Vendas', stock: 3, precio: '8.75' },
  { id: 5, nombre: 'Shampoo medicado', stock: 12, precio: '19.99' },
]

export const citasMedicas = [
  {
    id: 101,
    mascota: 1,
    mascota_nombre: 'Luna',
    dueno_nombre: 'María Torres',
    fecha_hora: '2026-10-18T09:30:00',
    motivo: 'Control general',
    estado: 'Atendida',
    detalles: [
      {
        id: 1,
        insumo: 2,
        insumo_nombre: 'Vacuna antirrábica',
        cantidad: 1,
        indicaciones_uso: 'Aplicar una dosis.',
        insumo_precio: '42.00',
      },
      {
        id: 2,
        insumo: 4,
        insumo_nombre: 'Vendas',
        cantidad: 2,
        indicaciones_uso: 'Usar para proteger la zona tratada.',
        insumo_precio: '8.75',
      },
    ],
  },
  {
    id: 102,
    mascota: 2,
    mascota_nombre: 'Max',
    dueno_nombre: 'José Ramírez',
    fecha_hora: '2026-10-19T11:00:00',
    motivo: 'Tratamiento antipulgas',
    estado: 'Pendiente',
    detalles: [
      {
        id: 3,
        insumo: 3,
        insumo_nombre: 'Antipulgas',
        cantidad: 1,
        indicaciones_uso: 'Administrar según indicación veterinaria.',
        insumo_precio: '35.90',
      },
    ],
  },
]
