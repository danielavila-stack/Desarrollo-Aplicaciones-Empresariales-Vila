from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Cita
from .forms import CitaForm, ESTADOS_CITA

def lista_citas_view(request):
    citas = Cita.objects.all()
    busqueda = request.GET.get('q', '').strip()
    fecha_hora = request.GET.get('fecha_hora', '').strip()
    estado = request.GET.get('estado', '').strip()

    if busqueda:
        citas = citas.filter(paciente_nombre__icontains=busqueda)
    if fecha_hora:
        citas = citas.filter(fecha_hora__date=fecha_hora)
    if estado:
        citas = citas.filter(estado=estado)

    todas_las_citas = Cita.objects.all()

    return render(request, 'citas/cita_list.html', {
        'citas': citas,
        'total_citas': todas_las_citas.count(),
        'pendientes': todas_las_citas.filter(estado='Pendiente').count(),
        'confirmadas': todas_las_citas.filter(estado='Confirmada').count(),
        'completadas': todas_las_citas.filter(estado__in=['Atendida', 'Completada']).count(),
        'busqueda': busqueda,
        'fecha_hora': fecha_hora,
        'estado_seleccionado': estado,
    })

def crear_cita_view(request):
    form = CitaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'La cita se registró correctamente.')
        return redirect('citas:lista')
    return render(request, 'citas/cita_form.html', {'form': form})

def detalle_cita_view(request, cita_id):
    cita = get_object_or_404(Cita, pk=cita_id)
    return render(request, 'citas/cita_detail.html', {'cita': cita})

def cambiar_estado_view(request, cita_id):
    if request.method == 'POST':
        nuevo_estado = request.POST.get('estado', '').strip()
        cita = get_object_or_404(Cita, pk=cita_id)
        if nuevo_estado in dict(ESTADOS_CITA):
            cita.estado = nuevo_estado
            cita.save()
            messages.success(request, f"El estado de la cita de {cita.paciente_nombre} se actualizó.")
        else:
            messages.error(request, 'El estado seleccionado no es válido.')
    return redirect('citas:lista')

def eliminar_cita_view(request, cita_id):
    if request.method == 'POST':
        cita = get_object_or_404(Cita, pk=cita_id)
        nombre = cita.paciente_nombre
        cita.delete()
        messages.success(request, f"La cita de {nombre} se eliminó correctamente.")
    return redirect('citas:lista')