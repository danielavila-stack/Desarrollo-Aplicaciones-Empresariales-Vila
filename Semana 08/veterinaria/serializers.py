from rest_framework import serializers
from .models import (
    Servicio,
    CitaMedica,
    Mascota,
    PerfilVeterinario,
    Insumo,
    DetalleReceta,
)


# --- 1. Serializador de Servicio ---
class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'

    def validate_precio(self, value):
        if value <= 0:
            raise serializers.ValidationError("El precio del servicio debe ser mayor a cero.")
        return value


# --- 2. Serializadores para Relaciones (Mascota y Cita Médica) ---
class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = ['id', 'nombre', 'dueno_nombre']


class CitaMedicaSerializer(serializers.ModelSerializer):
    mascota_nombre = serializers.ReadOnlyField(source='mascota.nombre')
    veterinario_colegiatura = serializers.ReadOnlyField(source='veterinario.colegiatura')

    class Meta:
        model = CitaMedica
        fields = [
            'id', 
            'mascota', 
            'mascota_nombre', 
            'veterinario', 
            'veterinario_colegiatura', 
            'fecha_hora', 
            'motivo', 
            'estado'
        ]


# --- 3. Serializador de Insumo (con validación propia) ---
class InsumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insumo
        fields = '__all__'

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("El stock del insumo no puede ser negativo.")
        return value
    
# --- 4. Serializadores Anidados (Ejercicio 7) ---
class DetalleRecetaAnidadoSerializer(serializers.ModelSerializer):
    insumo_nombre = serializers.ReadOnlyField(source='insumo.nombre')
    insumo_precio = serializers.ReadOnlyField(source='insumo.precio')

    class Meta:
        model = DetalleReceta
        fields = ['id', 'insumo', 'insumo_nombre', 'cantidad', 'indicaciones_uso', 'insumo_precio']


class CitaMedicaAnidadaSerializer(serializers.ModelSerializer):
    mascota_nombre = serializers.ReadOnlyField(source='mascota.nombre')
    dueno_nombre = serializers.ReadOnlyField(source='mascota.dueno_nombre')
    detalles = DetalleRecetaAnidadoSerializer(many=True, read_only=True, source='detalles_receta')

    class Meta:
        model = CitaMedica
        fields = [
            'id', 
            'mascota', 
            'mascota_nombre', 
            'dueno_nombre', 
            'fecha_hora', 
            'motivo', 
            'estado', 
            'detalles'
        ]