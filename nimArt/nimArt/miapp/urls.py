from django.urls import path
from .views import home, contacto, galeria, formulario, agregar_producto, listar_productos, modificar_producto, eliminar_producto, pagina1, pagina2, pagina3, pagina4, pagina5
from miapp.views import registro

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('galeria/', galeria, name="galeria"),
    path('formulario/', formulario, name="formulario"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('listar-productos/', listar_productos, name="listar_productos"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('registro/', registro, name='registro'),
    path('pagina1/', pagina1, name="pagina1"),
    path('pagina2/', pagina2, name="pagina2"),
    path('pagina3/', pagina3, name="pagina3"),
    path('pagina4/', pagina4, name="pagina4"),
    path('pagina5/', pagina5, name="pagina5"),
]
