from django.contrib import admin
from .models import Usuario, Contacto, Producto
# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    search_fields = ["nombre"]

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Contacto)
admin.site.register(Producto)