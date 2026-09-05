from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EspecieForm, HistorialMedicoForm, InsumoForm, MascotaForm, ServicioForm
from .models import Especie, HistorialMedico, Insumo, Mascota, Servicio


def especie_list(request):
    query = request.GET.get('q', '').strip()
    especies = Especie.objects.all().order_by('nombre')
    if query:
        especies = especies.filter(nombre__icontains=query)
    return render(request, 'veterinaria/especie_list.html', {'especies': especies, 'query': query})


def especie_create(request):
    form = EspecieForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'La especie se registro correctamente.')
        return redirect('veterinaria:especie_list')
    return render(request, 'veterinaria/especie_form.html', {'form': form, 'title': 'Nueva especie'})


def especie_update(request, pk):
    especie = get_object_or_404(Especie, pk=pk)
    form = EspecieForm(request.POST or None, instance=especie)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'La especie se actualizo correctamente.')
        return redirect('veterinaria:especie_list')
    return render(request, 'veterinaria/especie_form.html', {'form': form, 'title': 'Editar especie'})


def especie_delete(request, pk):
    if request.method == 'POST':
        especie = get_object_or_404(Especie, pk=pk)
        especie.delete()
        messages.success(request, 'La especie se elimino correctamente.')
    return redirect('veterinaria:especie_list')


def insumo_list(request):
    query = request.GET.get('q', '').strip()
    insumos = Insumo.objects.all().order_by('nombre')
    if query:
        insumos = insumos.filter(nombre__icontains=query)
    return render(request, 'veterinaria/insumo_list.html', {'insumos': insumos, 'query': query})


def insumo_create(request):
    form = InsumoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'El insumo se registro correctamente.')
        return redirect('veterinaria:insumo_list')
    return render(request, 'veterinaria/insumo_form.html', {'form': form, 'title': 'Nuevo insumo'})


def insumo_update(request, pk):
    insumo = get_object_or_404(Insumo, pk=pk)
    form = InsumoForm(request.POST or None, instance=insumo)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'El insumo se actualizo correctamente.')
        return redirect('veterinaria:insumo_list')
    return render(request, 'veterinaria/insumo_form.html', {'form': form, 'title': 'Editar insumo'})


def insumo_delete(request, pk):
    if request.method == 'POST':
        insumo = get_object_or_404(Insumo, pk=pk)
        insumo.delete()
        messages.success(request, 'El insumo se elimino correctamente.')
    return redirect('veterinaria:insumo_list')


def servicio_list(request):
    query = request.GET.get('q', '').strip()
    servicios = Servicio.objects.all().order_by('nombre')
    if query:
        servicios = servicios.filter(nombre__icontains=query)
    return render(request, 'veterinaria/servicio_list.html', {'servicios': servicios, 'query': query})


def servicio_create(request):
    form = ServicioForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'El servicio se registro correctamente.')
        return redirect('veterinaria:servicio_list')
    return render(request, 'veterinaria/servicio_form.html', {'form': form, 'title': 'Nuevo servicio'})


def servicio_update(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    form = ServicioForm(request.POST or None, instance=servicio)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'El servicio se actualizo correctamente.')
        return redirect('veterinaria:servicio_list')
    return render(request, 'veterinaria/servicio_form.html', {'form': form, 'title': 'Editar servicio'})


def servicio_delete(request, pk):
    if request.method == 'POST':
        servicio = get_object_or_404(Servicio, pk=pk)
        servicio.delete()
        messages.success(request, 'El servicio se elimino correctamente.')
    return redirect('veterinaria:servicio_list')


def mascota_list(request):
    query = request.GET.get('q', '').strip()
    mascotas = Mascota.objects.all().order_by('nombre')
    if query:
        mascotas = mascotas.filter(Q(nombre__icontains=query) | Q(dueno_nombre__icontains=query))
    return render(request, 'veterinaria/mascota_list.html', {'mascotas': mascotas, 'query': query})


def mascota_create(request):
    form = MascotaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'La mascota se registro correctamente.')
        return redirect('veterinaria:mascota_list')
    return render(request, 'veterinaria/mascota_form.html', {'form': form, 'title': 'Nueva mascota'})


def mascota_update(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    form = MascotaForm(request.POST or None, instance=mascota)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'La mascota se actualizo correctamente.')
        return redirect('veterinaria:mascota_list')
    return render(request, 'veterinaria/mascota_form.html', {'form': form, 'title': 'Editar mascota'})


def mascota_delete(request, pk):
    if request.method == 'POST':
        mascota = get_object_or_404(Mascota, pk=pk)
        mascota.delete()
        messages.success(request, 'La mascota y sus historiales se eliminaron correctamente.')
    return redirect('veterinaria:mascota_list')


def historial_list(request):
    query = request.GET.get('q', '').strip()
    historiales = HistorialMedico.objects.all().select_related('mascota').order_by('-fecha', '-id')
    if query:
        historiales = historiales.filter(
            Q(mascota__nombre__icontains=query)
            | Q(diagnostico__icontains=query)
            | Q(tratamiento__icontains=query)
        )
    return render(request, 'veterinaria/historial_list.html', {'historiales': historiales, 'query': query})


def historial_create(request):
    form = HistorialMedicoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'El historial medico se registro correctamente.')
        return redirect('veterinaria:historial_list')
    return render(request, 'veterinaria/historial_form.html', {'form': form, 'title': 'Nuevo historial medico'})


def historial_update(request, pk):
    historial = get_object_or_404(HistorialMedico, pk=pk)
    form = HistorialMedicoForm(request.POST or None, instance=historial)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'El historial medico se actualizo correctamente.')
        return redirect('veterinaria:historial_list')
    return render(request, 'veterinaria/historial_form.html', {'form': form, 'title': 'Editar historial medico'})


def historial_delete(request, pk):
    if request.method == 'POST':
        historial = get_object_or_404(HistorialMedico, pk=pk)
        historial.delete()
        messages.success(request, 'El historial medico se elimino correctamente.')
    return redirect('veterinaria:historial_list')
