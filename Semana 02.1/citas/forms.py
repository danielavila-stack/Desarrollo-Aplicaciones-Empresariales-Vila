from datetime import datetime

from django import forms
from django.utils import timezone


ESTADOS_CITA = (
    ('Pendiente', 'Pendiente'),
    ('Confirmada', 'Confirmada'),
    ('Atendida', 'Atendida'),
    ('Cancelada', 'Cancelada'),
)


class CitaForm(forms.Form):
    paciente_nombre = forms.CharField(label='Nombre completo', max_length=120, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Ana Torres'}))
    paciente_telefono = forms.CharField(label='Teléfono', max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 987 654 321'}))
    fecha_hora = forms.CharField(
        label='Fecha y hora',
        max_length=40,
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'class': 'form-control',
                'min': '2026-08-30T00:00',
            },
            format='%Y-%m-%d %H:%M',
        ),
    )
    motivo_consulta = forms.CharField(label='Motivo de consulta', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describe brevemente el motivo'}))
    estado = forms.ChoiceField(label='Estado', choices=ESTADOS_CITA, widget=forms.Select(attrs={'class': 'form-select'}))

    def clean(self):
        cleaned_data = super().clean()
        for field_name in self.fields:
            value = cleaned_data.get(field_name)
            if isinstance(value, str):
                cleaned_data[field_name] = value.strip()
                if not cleaned_data[field_name]:
                    self.add_error(field_name, 'Este campo es obligatorio.')
        return cleaned_data

    def clean_paciente_telefono(self):
        telefono = self.cleaned_data['paciente_telefono'].strip()
        digitos = ''.join(telefono.split())
        if not digitos.isdigit() or len(digitos) < 9:
            raise forms.ValidationError('Ingresa un teléfono válido con al menos 9 dígitos.')
        return telefono

    def clean_fecha_hora(self):
        fecha_hora = self.cleaned_data['fecha_hora'].strip()
        fecha_objeto = None
        for formato in ('%Y-%m-%d %H:%M', '%Y-%m-%dT%H:%M', '%Y-%m-%d'):
            try:
                fecha_objeto = datetime.strptime(fecha_hora, formato)
                break
            except ValueError:
                continue

        if fecha_objeto is None:
            raise forms.ValidationError('Ingresa una fecha y hora válida (AAAA-MM-DD HH:MM).')

        fecha_objeto = timezone.make_aware(fecha_objeto, timezone.get_current_timezone())
        if fecha_objeto < timezone.now():
            raise forms.ValidationError('No se pueden agendar citas en fechas u horas pasadas.')
        return fecha_hora