from django.contrib import messages
from django.db import connection, reset_queries, transaction
from django.db.models import Avg, Count, F, Max, Min, Sum
from django.shortcuts import get_object_or_404, redirect, render

from .forms import (
    CitaMedicaForm,
    DetalleRecetaForm,
    EspecieForm,
    HistorialMedicoForm,
    InsumoForm,
    MascotaForm,
    ServicioForm,
)
from .models import (
    CitaMedica,
    DetalleReceta,
    Especie,
    HistorialMedico,
    Insumo,
    Mascota,
    Servicio,
)


# ==========================================
# ESPECIES
# ==========================================
def lista_especies(request):
    especies = Especie.objects.all().order_by('nombre')
    return render(request, 'veterinaria/especie_list.html', {'especies': especies})


def crear_especie(request):
    form = EspecieForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'La especie se creó correctamente.')
        return redirect('lista_especies')
    return render(request, 'veterinaria/especie_form.html', {'form': form})


def editar_especie(request, pk):
    especie = get_object_or_404(Especie, pk=pk)
    form = EspecieForm(request.POST or None, instance=especie)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'La especie se actualizó correctamente.')
        return redirect('lista_especies')
    return render(request, 'veterinaria/especie_form.html', {'form': form, 'especie': especie})


def eliminar_especie(request, pk):
    if request.method == 'POST':
        especie = get_object_or_404(Especie, pk=pk)
        especie.delete()
        messages.success(request, 'La especie se eliminó correctamente.')
    return redirect('lista_especies')


# ==========================================
# INSUMOS
# ==========================================
def lista_insumos(request):
    insumos = Insumo.objects.all().order_by('nombre')
    return render(request, 'veterinaria/insumo_list.html', {'insumos': insumos})


def crear_insumo(request):
    form = InsumoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'El insumo se creó correctamente.')
        return redirect('lista_insumos')
    return render(request, 'veterinaria/insumo_form.html', {'form': form})


def editar_insumo(request, pk):
    insumo = get_object_or_404(Insumo, pk=pk)
    form = InsumoForm(request.POST or None, instance=insumo)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'El insumo se actualizó correctamente.')
        return redirect('lista_insumos')
    return render(request, 'veterinaria/insumo_form.html', {'form': form, 'insumo': insumo})


def eliminar_insumo(request, pk):
    if request.method == 'POST':
        insumo = get_object_or_404(Insumo, pk=pk)
        insumo.delete()
        messages.success(request, 'El insumo se eliminó correctamente.')
    return redirect('lista_insumos')


# ==========================================
# SERVICIOS
# ==========================================
def lista_servicios(request):
    servicios = Servicio.objects.all().order_by('nombre')
    return render(request, 'veterinaria/servicio_list.html', {'servicios': servicios})


def crear_servicio(request):
    form = ServicioForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'El servicio se creó correctamente.')
        return redirect('lista_servicios')
    return render(request, 'veterinaria/servicio_form.html', {'form': form})


def editar_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    form = ServicioForm(request.POST or None, instance=servicio)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'El servicio se actualizó correctamente.')
        return redirect('lista_servicios')
    return render(request, 'veterinaria/servicio_form.html', {'form': form, 'servicio': servicio})


def eliminar_servicio(request, pk):
    if request.method == 'POST':
        servicio = get_object_or_404(Servicio, pk=pk)
        servicio.delete()
        messages.success(request, 'El servicio se eliminó correctamente.')
    return redirect('lista_servicios')


# ==========================================
# MASCOTAS
# ==========================================
def lista_mascotas(request):
    buscar = request.GET.get('q')
    if buscar:
        mascotas = Mascota.objects.filter(nombre__icontains=buscar).order_by('nombre')
    else:
        mascotas = Mascota.objects.all().order_by('nombre')
        
    return render(request, 'veterinaria/mascota_list.html', {'mascotas': mascotas})


def crear_mascota(request):
    form = MascotaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'La mascota se creó correctamente.')
        return redirect('lista_mascotas')
    return render(request, 'veterinaria/mascota_form.html', {'form': form})


def editar_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    form = MascotaForm(request.POST or None, instance=mascota)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'La mascota se actualizó correctamente.')
        return redirect('lista_mascotas')
    return render(request, 'veterinaria/mascota_form.html', {'form': form, 'mascota': mascota})


def eliminar_mascota(request, pk):
    if request.method == 'POST':
        mascota = get_object_or_404(Mascota, pk=pk)
        mascota.delete()
        messages.success(request, 'La mascota se eliminó correctamente.')
    return redirect('lista_mascotas')


# ==========================================
# HISTORIALES MÉDICOS
# ==========================================
def lista_historiales(request):
    historiales = HistorialMedico.objects.all().order_by('-fecha')
    return render(request, 'veterinaria/historialmedico_list.html', {'historiales': historiales})


def crear_historial(request):
    form = HistorialMedicoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'El historial médico se creó correctamente.')
        return redirect('lista_historiales')
    return render(request, 'veterinaria/historialmedico_form.html', {'form': form})


def editar_historial(request, pk):
    historial = get_object_or_404(HistorialMedico, pk=pk)
    form = HistorialMedicoForm(request.POST or None, instance=historial)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'El historial médico se actualizó correctamente.')
        return redirect('lista_historiales')
    return render(request, 'veterinaria/historialmedico_form.html', {'form': form, 'historial': historial})


def eliminar_historial(request, pk):
    if request.method == 'POST':
        historial = get_object_or_404(HistorialMedico, pk=pk)
        historial.delete()
        messages.success(request, 'El historial médico se eliminó correctamente.')
    return redirect('lista_historiales')


# ==========================================
# CITAS Y RECETAS
# ==========================================

# VISTA 1 PARA EJERCICIO 12: Métodos encadenados .completadas().del_mes()
def lista_citas(request):
    citas = CitaMedica.objects.completadas().del_mes().select_related('mascota', 'veterinario')
    return render(request, 'veterinaria/cita_list.html', {'citas': citas})


def crear_cita(request):
    form = CitaMedicaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'La cita médica se creó correctamente.')
        return redirect('cita_list')
    return render(request, 'veterinaria/cita_form.html', {'form': form})


def lista_recetas(request):
    citas = CitaMedica.objects.prefetch_related(
        'detalles_receta__insumo',
        'mascota',
    ).all()
    return render(request, 'veterinaria/receta_list.html', {'citas': citas})


# VISTA PARA EJERCICIO 13: Optimización N+1 con select_related y medición de consultas SQL
def lista_detalles(request):
    reset_queries()  # Limpia el historial de consultas
    
    # Consulta optimizada con select_related para traer en un solo JOIN: cita, insumo y mascota
    detalles = list(DetalleReceta.objects.select_related('cita', 'insumo', 'cita__mascota').all())
    
    # Mide e imprime el total de consultas SQL ejecutadas en la terminal
    print(f"--- EJERCICIO 13: Total de consultas SQL ejecutadas = {len(connection.queries)} ---")
    
    return render(request, 'veterinaria/detalle_list.html', {'detalles': detalles})


def crear_detalle(request):
    form = DetalleRecetaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'El detalle de receta se creó correctamente.')
        return redirect('lista_detalles')
    return render(request, 'veterinaria/detalle_form.html', {'form': form})


def editar_detalle(request, pk):
    detalle = get_object_or_404(DetalleReceta, pk=pk)
    form = DetalleRecetaForm(request.POST or None, instance=detalle)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'El detalle de receta se actualizó correctamente.')
        return redirect('lista_detalles')
    return render(request, 'veterinaria/detalle_form.html', {'form': form, 'detalle': detalle})


def eliminar_detalle(request, pk):
    detalle = get_object_or_404(DetalleReceta, pk=pk)
    if request.method == 'POST':
        detalle.delete()
        messages.success(request, 'El detalle de receta se eliminó correctamente.')
        return redirect('lista_detalles')
    return render(request, 'veterinaria/detalle_confirm_delete.html', {'detalle': detalle})


# ==========================================
# OPERACIÓN ATÓMICA CON F() (EJERCICIO 10)
# ==========================================
def recetar_insumo_view(request, cita_id=None):
    cita = get_object_or_404(CitaMedica, pk=cita_id) if cita_id else None
    citas = CitaMedica.objects.all()
    insumos = Insumo.objects.all()

    if request.method == 'POST':
        target_cita_id = cita_id or request.POST.get('cita')
        insumo_id = request.POST.get('insumo')
        cantidad = int(request.POST.get('cantidad', 1))
        indicaciones = request.POST.get('indicaciones', 'Uso según indicaciones médicas')

        try:
            with transaction.atomic():
                insumo = Insumo.objects.select_for_update().get(id=insumo_id)

                if insumo.stock < cantidad:
                    raise ValueError(f"Stock insuficiente. Solo quedan {insumo.stock} unidades de {insumo.nombre}.")

                insumo.stock = F('stock') - cantidad
                insumo.save()

                cita_obj = CitaMedica.objects.get(id=target_cita_id)
                cita_obj.estado = 'COMPLETADO'
                cita_obj.save()

                DetalleReceta.objects.create(
                    cita=cita_obj,
                    insumo=insumo,
                    cantidad=cantidad,
                    indicaciones_uso=indicaciones
                )

                messages.success(request, f"¡Receta registrada con éxito! Se descontaron {cantidad} unidad(es) de {insumo.nombre}.")
                return redirect('cita_list')

        except Exception as e:
            messages.error(request, f"Error en la operación: {str(e)}")

    return render(request, 'veterinaria/recetar_insumo.html', {
        'cita': cita,
        'citas': citas,
        'insumos': insumos
    })


# ==========================================
# REPORTE GENERAL (EJERCICIO 11 Y VISTA 2 DEL EJERCICIO 12)
# ==========================================
def reporte_view(request):
    resumen_insumos = Insumo.objects.aggregate(
        total_unidades=Sum('stock'),
        precio_promedio=Avg('precio'),
        precio_maximo=Max('precio'),
        precio_minimo=Min('precio')
    )

    monto_global_recetas = DetalleReceta.objects.aggregate(
        monto_total=Sum(F('cantidad') * F('insumo__precio'))
    )

    mascotas_anotadas = Mascota.objects.annotate(
        total_citas=Count('citas')
    ).order_by('-total_citas')

    citas_por_estado = CitaMedica.objects.values('estado').annotate(
        total=Count('id')
    ).order_by('-total')

    # VISTA 2 PARA EJERCICIO 12: Métodos encadenados .completadas().del_mes()
    citas_completadas_mes = CitaMedica.objects.completadas().del_mes()
    total_citas_mes = citas_completadas_mes.count()

    context = {
        'resumen_insumos': resumen_insumos,
        'monto_global_recetas': monto_global_recetas,
        'mascotas_anotadas': mascotas_anotadas,
        'citas_por_estado': citas_por_estado,
        'total_citas_mes': total_citas_mes,
    }
    return render(request, 'veterinaria/reporte.html', context)