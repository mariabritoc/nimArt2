from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Usuario, Boleta, detalle_boleta
from .forms import ContactoForm, ProductoForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login 
from .compra import carrito
from django.views.generic import TemplateView
# Create your views here.

def home(request):
    return render(request, 'miapp/home.html')

def contacto(request):
    return render(request, 'miapp/contacto.html')

def galeria(request):
    return render(request, 'miapp/galeria.html')

def formulario(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mansaje"] = "contacto enviado"
        else:
            data["form"] = formulario

    return render(request, 'miapp/formulario.html', data)


def agregar_producto(request):
    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto agregado")
            return redirect(to="listar_productos")
        else:
            data["form"] = formulario

    return render(request, 'miapp/producto/agregar.html', data)

def listar_productos(request):
    productos = Producto.objects.all()

    data = {
        'productos': productos
    }
    return render(request, 'miapp/producto/listar.html', data)


def modificar_producto(request,id):
    producto = get_object_or_404(Producto, id=id)
    data ={
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'modificado correctamente')
            return redirect(to="listar_productos")
        else:
            data["form"] = formulario
    return render(request, 'miapp/producto/modificar.html', data)

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to="listar_productos")


def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
        data["form"] = formulario
        return redirect(to="home")
    return render(request, 'registration/registro.html', data)

def pagina1(request):
    return render(request, 'miapp/pagina1.html')

def pagina2(request):
    return render(request, 'miapp/pagina2.html')

def pagina3(request):
    return render(request, 'miapp/pagina3.html')

def pagina4(request):
    return render(request, 'miapp/pagina4.html')

def pagina5(request):
    return render(request, 'miapp/pagina5.html')

def agregar_producto_carrito(request, nombre):
    carrito_compra = carrito(request)
    producto = Producto.objects.get(nombre=nombre)
    carrito_compra.agregar_producto(producto)
    return redirect('tienda')

def eliminar_producto_carrito(request,nombre):
    carrito_compra= carrito(request)
    producto = Producto.objects.get(nombre=nombre)
    carrito_compra.eliminar(producto=producto)
    return redirect('tienda')

def restar_producto_carrito(request,nombre):
    carrito_compra= carrito(request)
    producto = Producto.objects.get(nombre=nombre)
    carrito_compra.restar(producto=producto)
    return redirect('tienda')

def limpiar_producto_carrito(request):
    carrito_compra= carrito(request)
    carrito_compra.limpiar()
    return redirect('tienda')

def tienda(request):
    productitos = Producto.objects.all()
    datos={
        'productitos': productitos
    }
    return render(request, 'miapp/tienda.html',datos)

def ver_carrito(request):
    return render(request, 'miapp/carrito.html')

def generarBoleta(request):
    carrito_compra = carrito(request)
    precio_total = 0

    for key, value in carrito_compra.carrito.items():
        if isinstance(value, dict):
            precio_total += int(value['precio']) * int(value['cantidad'])

    boleta = Boleta(total=precio_total)
    boleta.save()

    productos = []
    for key, value in carrito_compra.carrito.items():
        if isinstance(value, dict):
            producto = Producto.objects.get(nombre=value['nombre'])
            cant = int(value['cantidad'])
            subtotal = cant * int(value['precio'])
            detalle = detalle_boleta(id_boleta=boleta, id_producto=producto, cantidad=cant, subtotal=subtotal)
            productos.append(detalle)

    detalle_boleta.objects.bulk_create(productos, ignore_conflicts=True)

    datos = {
        'productos': productos,
        'fecha': boleta.fechaCompra,
        'total': boleta.total  # Asegurarse de que boleta.total esté actualizado correctamente en el modelo
    }

    request.session['boleta'] = boleta.id_boleta
    carrito_compra.limpiar()

    return render(request, 'miapp/detallecarrito.html', datos)


def detallecarrito(request):
    return render(request, 'miapp/detallecarrito.html')