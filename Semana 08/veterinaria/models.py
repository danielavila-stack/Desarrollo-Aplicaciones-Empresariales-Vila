from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone  # Importante para manejar la fecha actual en del_mes()


# ==========================================
# QUERYSET PERSONALIZADO (EJERCICIO 7)
# ==========================================
class CitaMedicaQuerySet(models.QuerySet):

    def completadas(self):
        """Regla de negocio 1: Filtra las citas en estado completado o atendida"""
        return self.filter(
            models.Q(estado__iexact='Completado')
            | models.Q(estado__iexact='Atendida')
        )

    def del_mes(self):
        """Regla de negocio 2: Filtra las citas registradas en el mes y año actual"""
        ahora = timezone.now()
        return self.filter(
            fecha_hora__year=ahora.year, fecha_hora__month=ahora.month
        )


# ==========================================
# ENTIDADES DEL SISTEMA
# ==========================================
class Especie(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Insumo(models.Model):
    nombre = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nombre


class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nombre


class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    dueno_nombre = models.CharField(max_length=100, verbose_name="Dueño")

    def __str__(self):
        return self.nombre


class HistorialMedico(models.Model):
    mascota = models.ForeignKey(
        Mascota,
        on_delete=models.CASCADE,
        related_name='historiales',
    )
    fecha = models.DateField()
    diagnostico = models.TextField()
    tratamiento = models.TextField()

    def __str__(self):
        return f'{self.mascota} - {self.fecha}'


class PerfilVeterinario(models.Model):
    # Cada usuario puede tener un único perfil profesional de veterinario.
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='perfil_veterinario',
    )
    colegiatura = models.CharField(max_length=20, unique=True)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f'Vet. {self.colegiatura} - {self.especialidad}'


class FichaMedica(models.Model):
    # Cada mascota tiene una única ficha médica asociada.
    mascota = models.OneToOneField(
        Mascota,
        on_delete=models.CASCADE,
        related_name='ficha_medica',
    )
    codigo_chip = models.CharField(max_length=50, unique=True)
    alergias = models.TextField(blank=True, null=True)
    grupo_sanguineo = models.CharField(max_length=10)

    def __str__(self):
        return f'Ficha de {self.mascota.nombre}'


class CitaMedica(models.Model):
    # Una mascota puede tener múltiples citas médicas.
    mascota = models.ForeignKey(
        Mascota,
        on_delete=models.CASCADE,
        related_name='citas',
    )
    # No se puede eliminar un veterinario que tenga citas registradas.
    veterinario = models.ForeignKey(
        PerfilVeterinario,
        on_delete=models.PROTECT,
        related_name='citas',
    )
    fecha_hora = models.DateTimeField()
    motivo = models.CharField(max_length=200)
    estado = models.CharField(max_length=20, default='Pendiente')
    insumos_recetados = models.ManyToManyField(
        Insumo,
        through='DetalleReceta',
        related_name='citas_asociadas',
    )

    # Asignamos el QuerySet personalizado con as_manager() (Ejercicio 7)
    objects = CitaMedicaQuerySet.as_manager()

    def __str__(self):
        return f"Cita de {self.mascota.nombre} el {self.fecha_hora.strftime('%Y-%m-%d %H:%M')}"


class DetalleReceta(models.Model):
    # Este modelo intermedio permite guardar datos propios de cada insumo recetado.
    cita = models.ForeignKey(
        CitaMedica,
        on_delete=models.CASCADE,
        related_name='detalles_receta',
    )
    insumo = models.ForeignKey(
        Insumo,
        on_delete=models.PROTECT,
        related_name='detalles_receta',
    )
    cantidad = models.PositiveIntegerField(default=1)
    indicaciones_uso = models.TextField()

    def __str__(self):
        return f'{self.cantidad}x {self.insumo.nombre} para cita #{self.cita.id}'


class Factura(models.Model):
    historial = models.ForeignKey(
        HistorialMedico,
        on_delete=models.CASCADE,
        related_name='facturas',
    )
    fecha_emision = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return f'Factura #{self.id} - S/ {self.total}'