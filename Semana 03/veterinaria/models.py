from django.db import models


class Especie(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        ordering = ['nombre']
        verbose_name = 'especie'
        verbose_name_plural = 'especies'

    def __str__(self):
        return self.nombre


class Insumo(models.Model):
    nombre = models.CharField(max_length=100)
    stock = models.IntegerField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        ordering = ['nombre']
        verbose_name = 'insumo'
        verbose_name_plural = 'insumos'

    def __str__(self):
        return self.nombre


class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        ordering = ['nombre']
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'

    def __str__(self):
        return self.nombre


class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    dueno_nombre = models.CharField(max_length=100)

    class Meta:
        ordering = ['nombre']
        verbose_name = 'mascota'
        verbose_name_plural = 'mascotas'

    def __str__(self):
        return f'{self.nombre} - {self.dueno_nombre}'


class HistorialMedico(models.Model):
    mascota = models.ForeignKey(
        Mascota,
        on_delete=models.CASCADE,
        related_name='historiales',
    )
    fecha = models.DateField()
    diagnostico = models.TextField()
    tratamiento = models.TextField()

    class Meta:
        ordering = ['-fecha', '-id']
        verbose_name = 'historial medico'
        verbose_name_plural = 'historiales medicos'

    def __str__(self):
        return f'{self.mascota.nombre} - {self.fecha:%d/%m/%Y}'
