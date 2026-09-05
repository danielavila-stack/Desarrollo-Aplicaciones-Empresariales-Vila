from django.db import models

class Cita(models.Model):
    ESTADO_CHOICES = [
        ('Confirmada', 'Confirmada'),
        ('Pendiente', 'Pendiente'),
        ('Atendida', 'Atendida'),
        ('Cancelada', 'Cancelada'),
    ]

    paciente_nombre = models.CharField(max_length=150)
    paciente_telefono = models.CharField(max_length=20)
    fecha_hora = models.DateTimeField()
    motivo_consulta = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Pendiente')

    def __str__(self):
        return f"Cita de {self.paciente_nombre} - {self.fecha_hora.strftime('%Y-%m-%d %H:%M')}"