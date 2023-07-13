from django.db import models
import datetime
# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="nombre")
    precio = models.IntegerField()
    descripcion = models.TextField()
    nuevo = models.BooleanField()
    fecha_fabricacion = models.DateField()
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre





class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    telefono = models.IntegerField(null=False)

    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido)
    
opciones_asuntos = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    telefono = models.IntegerField(null=False)
    asunto = models.IntegerField(choices=opciones_asuntos)
    mensaje = models.TextField()

    def __str__(self):
        return str(self.nombre)


class Boleta(models.Model):
    id_boleta = models.AutoField(primary_key=True)
    total = models.BigIntegerField()
    fechaCompra = models.DateTimeField(blank=False, null=False, default=datetime.datetime.now)

    def __str__(self):
        return str(self.id_boleta)
    
class detalle_boleta(models.Model):
    id_boleta = models.ForeignKey('Boleta', blank=True, on_delete=models.CASCADE)
    id_detalle_boleta = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.BigIntegerField()

    def __str__(self):
        return str(self.id_detalle_boleta)


