from django import forms

from .models import (
    CitaMedica,
    DetalleReceta,
    Especie,
    HistorialMedico,
    Insumo,
    Mascota,
    Servicio,
)


class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            widget = field.widget
            css_class = 'form-select' if isinstance(widget, forms.Select) else 'form-control'
            widget.attrs['class'] = f"{widget.attrs.get('class', '')} {css_class}".strip()


class EspecieForm(BootstrapModelForm):
    class Meta:
        model = Especie
        fields = '__all__'


class InsumoForm(BootstrapModelForm):
    class Meta:
        model = Insumo
        fields = '__all__'


class ServicioForm(BootstrapModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'


class MascotaForm(BootstrapModelForm):
    class Meta:
        model = Mascota
        fields = '__all__'


class HistorialMedicoForm(BootstrapModelForm):
    class Meta:
        model = HistorialMedico
        fields = '__all__'


class CitaMedicaForm(BootstrapModelForm):
    class Meta:
        model = CitaMedica
        fields = ('mascota', 'veterinario', 'fecha_hora', 'motivo', 'estado')


class DetalleRecetaForm(BootstrapModelForm):
    class Meta:
        model = DetalleReceta
        fields = ['cita', 'insumo', 'cantidad', 'indicaciones_uso']
