from django.http import Http404
from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ESTADOS_CITA, CitaForm
from .models import add_cita, delete_cita, get_all_citas, get_cita_by_id, update_cita_estado


def lista_citas_view(request):
	todas_las_citas = get_all_citas()
	citas = todas_las_citas
	busqueda = request.GET.get('q', '').strip()
	fecha_hora = request.GET.get('fecha_hora', '').strip()
	estado = request.GET.get('estado', '').strip()
	if busqueda:
		citas = [cita for cita in citas if busqueda.casefold() in cita['paciente_nombre'].casefold()]
	if fecha_hora:
		citas = [cita for cita in citas if cita['fecha_hora'].strftime('%Y-%m-%d') == fecha_hora]
	if estado:
		citas = [cita for cita in citas if cita['estado'] == estado]
	return render(request, 'citas/cita_list.html', {
		'citas': citas,
		'total_citas': len(todas_las_citas),
		'pendientes': sum(cita['estado'] == 'Pendiente' for cita in todas_las_citas),
		'confirmadas': sum(cita['estado'] == 'Confirmada' for cita in todas_las_citas),
		'completadas': sum(cita['estado'] in ('Atendida', 'Completada') for cita in todas_las_citas),
		'busqueda': busqueda,
		'fecha_hora': fecha_hora,
		'estado_seleccionado': estado,
	})


def crear_cita_view(request):
	form = CitaForm(request.POST or None)
	if request.method == 'POST' and form.is_valid():
		add_cita(form.cleaned_data)
		messages.success(request, 'La cita se registró correctamente.')
		return redirect('citas:lista')
	return render(request, 'citas/cita_form.html', {'form': form})


def detalle_cita_view(request, cita_id):
	cita = get_cita_by_id(cita_id)
	if cita is None:
		raise Http404('La cita no existe.')
	return render(request, 'citas/cita_detail.html', {'cita': cita})


def cambiar_estado_view(request, cita_id):
	if request.method == 'POST':
		nuevo_estado = request.POST.get('estado', '').strip()
		if nuevo_estado in dict(ESTADOS_CITA):
			cita = update_cita_estado(cita_id, nuevo_estado)
			if cita is not None:
				messages.success(request, f"El estado de la cita de {cita['paciente_nombre']} se actualizó.")
			else:
				messages.error(request, 'La cita no existe.')
		else:
			messages.error(request, 'El estado seleccionado no es válido.')
	return redirect('citas:lista')


def eliminar_cita_view(request, cita_id):
	if request.method == 'POST':
		cita = delete_cita(cita_id)
		if cita is not None:
			messages.success(request, f"La cita de {cita['paciente_nombre']} se eliminó correctamente.")
		else:
			messages.error(request, 'La cita no existe.')
	return redirect('citas:lista')
