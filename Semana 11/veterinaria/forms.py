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

    def clean(self):
        cleaned_data = super().clean()
        insumo = cleaned_data.get('insumo')
        cantidad = cleaned_data.get('cantidad')

        # Regla de negocio: Validar que la cantidad sea válida y no supere el stock
        if insumo and cantidad is not None:
            if cantidad <= 0:
                raise forms.ValidationError("La cantidad a recetar debe ser mayor a 0.")
            
            if cantidad > insumo.stock:
                raise forms.ValidationError(
                    f"¡Error de stock! No puedes recetar {cantidad} unidades de '{insumo.nombre}'. "
                    f"Solo hay {insumo.stock} unidades disponibles en inventario."
                )

        return cleaned_data