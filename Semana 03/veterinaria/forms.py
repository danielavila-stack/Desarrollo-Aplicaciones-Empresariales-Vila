from django import forms

from .models import Especie, HistorialMedico, Insumo, Mascota, Servicio


class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'


class EspecieForm(BootstrapModelForm):
    class Meta:
        model = Especie
        fields = ['nombre']


class InsumoForm(BootstrapModelForm):
    class Meta:
        model = Insumo
        fields = ['nombre', 'stock', 'precio']
        widgets = {
            'precio': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
            'stock': forms.NumberInput(attrs={'min': '0'}),
        }


class ServicioForm(BootstrapModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'precio']
        widgets = {
            'precio': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
        }


class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'edad', 'dueno_nombre']
        labels = {
            'nombre': 'Nombre:',
            'edad': 'Edad:',
            'dueno_nombre': 'Dueño:',  # <-- Aquí cambia el texto visible
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'dueno_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del dueño'}),
        }


class HistorialMedicoForm(BootstrapModelForm):
    class Meta:
        model = HistorialMedico
        fields = ['mascota', 'fecha', 'diagnostico', 'tratamiento']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'diagnostico': forms.Textarea(attrs={'rows': 4}),
            'tratamiento': forms.Textarea(attrs={'rows': 4}),
        }
