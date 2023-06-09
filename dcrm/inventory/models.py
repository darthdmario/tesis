from django.db import models

class Record(models.Model):
    codigo_institucion_externa = models.CharField(max_length=100)
    codigo_senecyt = models.CharField(max_length=100)
    codigo_toma_fisica = models.CharField(max_length=100)
    codigo_anterior = models.CharField(max_length=100)
    bien = models.CharField(max_length=50)
    clase_bien = models.CharField(max_length=100)
    serie  = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    usuario_final = models.CharField(max_length=50)
    nro_cedula = models.CharField(max_length=10)
    ubicacion = models.CharField(max_length=100)
    edificio = models.CharField(max_length=100)
    custodio_administrativo = models.CharField(max_length=50)
    delegado_1 = models.CharField(max_length=50)
    delegado_2 = models.CharField(max_length=50)
    delegado_3 = models.CharField(max_length=50)
    tipo_novedad = models.CharField(max_length=500)
    observaciones = models.CharField(max_length=500)
    nro_acta_entrega_recepcion = models.CharField(max_length=50)
    nro_acta_donacion_factura = models.CharField(max_length=50)
    valor_monetario = models.CharField(max_length=50)
    fecha_entrega_recepcion = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return(f"{self.codigo_institucion_externa}")