from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
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


