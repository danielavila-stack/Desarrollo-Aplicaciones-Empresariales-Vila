from datetime import datetime


def _fecha_hora(texto):
	fecha_str = texto.replace('T', ' ')
	return datetime.strptime(fecha_str, '%Y-%m-%d %H:%M')


CITAS_DATA = [
	{'id': 1, 'paciente_nombre': 'Ana Torres', 'paciente_telefono': '987 654 321', 'fecha_hora': _fecha_hora('2026-09-02 09:00'), 'motivo_consulta': 'Manejo de ansiedad y estrés laboral.', 'estado': 'Confirmada'},
	{'id': 2, 'paciente_nombre': 'Luis Mendoza', 'paciente_telefono': '986 123 456', 'fecha_hora': _fecha_hora('2026-09-02 11:30'), 'motivo_consulta': 'Orientación para mejorar el sueño.', 'estado': 'Pendiente'},
	{'id': 3, 'paciente_nombre': 'Mariana Rojas', 'paciente_telefono': '985 789 012', 'fecha_hora': _fecha_hora('2026-09-03 15:00'), 'motivo_consulta': 'Acompañamiento emocional.', 'estado': 'Atendida'},
	{'id': 4, 'paciente_nombre': 'Carlos Vega', 'paciente_telefono': '984 345 678', 'fecha_hora': _fecha_hora('2026-09-04 10:00'), 'motivo_consulta': 'Evaluación de dificultades familiares.', 'estado': 'Cancelada'},
	{'id': 5, 'paciente_nombre': 'Sofía Castillo', 'paciente_telefono': '983 901 234', 'fecha_hora': _fecha_hora('2026-09-05 16:30'), 'motivo_consulta': 'Fortalecimiento de autoestima.', 'estado': 'Pendiente'},
]


def get_all_citas():
	return CITAS_DATA


def get_cita_by_id(cita_id):
	try:
		cita_id = int(cita_id)
	except (TypeError, ValueError):
		return None
	return next((cita for cita in CITAS_DATA if cita['id'] == cita_id), None)


def add_cita(data):
	next_id = max((cita['id'] for cita in CITAS_DATA), default=0) + 1
	cita = {'id': next_id, **data}
	if isinstance(cita['fecha_hora'], str):
		cita['fecha_hora'] = _fecha_hora(cita['fecha_hora'])
	CITAS_DATA.append(cita)
	return cita


def update_cita_estado(cita_id, nuevo_estado):
	cita = get_cita_by_id(cita_id)
	if cita is None:
		return None
	cita['estado'] = nuevo_estado
	return cita


def delete_cita(cita_id):
	cita = get_cita_by_id(cita_id)
	if cita is None:
		return None
	CITAS_DATA.remove(cita)
	return cita
