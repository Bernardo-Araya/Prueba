from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
from django.contrib import messages
=======
from app_obras.compra import Carrito
>>>>>>> 85851ffd8f8e41941781c2d283594a5209847f8b
from django.http import HttpResponse
import random
from transbank.error.transbank_error import TransbankError
from transbank.webpay.webpay_plus.transaction import Transaction
from rest_framework import generics
<<<<<<< HEAD
from app_obras.compra import Carrito
from app_obras.forms import ProductoForm, ArriendoForm, RegistroUserForm
from .models import Categoria, Producto, Boleta, detalle_boleta
from .serializers import CategoriaSerializer, ProductoSerializer, BoletaSerializer, DetalleBoletaSerializer
import requests
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login


def registro(request):
    if request.method == 'POST':
        form = RegistroUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegistroUserForm()
    
    return render(request, 'registro.html', {'form': form})

def register(request):
    return render(request, 'registro.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('correo')  # El usuario es el email
            password = form.cleaned_data.get('contrasenia')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                auth_login(request, user)
                # Redirigir a la página deseada después del inicio de sesión
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def index(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', context={'datos': productos})


def nosotros(request):
    productos = Producto.objects.all()
    return render(request, 'nosotros.html', context={'datos': productos})


def administracion(request):
    productos = Producto.objects.all()
    return render(request, 'administracion.html', context={'datos': productos})


@login_required
def crear(request):
    if request.method == "POST":
        productoform = ProductoForm(request.POST, request.FILES)
        if productoform.is_valid():
            productoform.save()  # similar al insert en función
            return redirect('administracion')
    else:
        productoform = ProductoForm()
    return render(request, 'crear.html', {'productoform': productoform})


@login_required
def eliminar(request, producto_id):
    productoEliminada = Producto.objects.get(idProducto=producto_id)  # similar a select * from... where...
    productoEliminada.delete()
    return redirect('administracion')


@login_required
def modificar(request, producto_id):
    productoModificada = Producto.objects.get(idProducto=producto_id)  # Buscamos el objeto
=======
from django.contrib import messages

from app_obras.forms import ProductoForm, ArriendoForm
from .models import Categoria, Producto, Boleta, detalle_boleta
from .serializers import CategoriaSerializer, ProductoSerializer, BoletaSerializer, DetalleBoletaSerializer
from django.http import HttpResponseBadRequest
import requests


def index(request):
	productos= Producto.objects.all()
	
	return render(request, 'index.html',context={'datos':productos})


def nosotros(request):
	productos= Producto.objects.all()
	
	return render(request, 'nosotros.html',context={'datos':productos})

def administracion(request):
	productos= Producto.objects.all()
	
	return render(request, 'administracion.html',context={'datos':productos})

@login_required
def crear(request):
    if request.method=="POST":
        productoform=ProductoForm(request.POST,request.FILES)
        if productoform.is_valid():
            productoform.save()     #similar al insert en función
            return redirect ('administracion')
    else:
        productoform=ProductoForm()
    return render (request, 'crear.html', {'productoform': productoform})



@login_required
def eliminar(request, producto_id): 
    productoEliminada = Producto.objects.get(idProducto=producto_id) #similar a select * from... where...
    productoEliminada.delete()
    return redirect ('administracion')

@login_required
def modificar(request, producto_id): 
    productoModificada = Producto.objects.get(idProducto=producto_id) # Buscamos el objeto
>>>>>>> 85851ffd8f8e41941781c2d283594a5209847f8b
    
    if request.method == "POST":
        formulario = ProductoForm(data=request.POST, instance=productoModificada)
        if formulario.is_valid():
            formulario.save()
            return redirect('administracion')
    else:
        # Crear el formulario con el atributo readonly
        form = ProductoForm(instance=productoModificada)
        form.fields['idProducto'].widget.attrs['readonly'] = 'readonly'

    datos = {
        'form': form
    }
    
    return render(request, 'modificar.html', datos)


def obtener_tasa_de_cambio():
    try:
        response = requests.get('https://api.exchangerate-api.com/v4/latest/CLP')
        response.raise_for_status()
        datos = response.json()
        return datos['rates']['USD']
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener la tasa de cambio: {e}")
        return None

<<<<<<< HEAD

=======
>>>>>>> 85851ffd8f8e41941781c2d283594a5209847f8b
def mostrar(request):
    try:
        response = requests.get('http://127.0.0.1:8000/api/productos/')
        response.raise_for_status()
        productos = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener productos de la API: {e}")
        productos = []

    tasa_de_cambio = obtener_tasa_de_cambio()
<<<<<<< HEAD
    if (tasa_de_cambio is not None):
=======
    if tasa_de_cambio is not None:
>>>>>>> 85851ffd8f8e41941781c2d283594a5209847f8b
        for producto in productos:
            producto['precio_usd'] = round(producto['precio'] * tasa_de_cambio, 2)
    else:
        for producto in productos:
            producto['precio_usd'] = 'N/A'

    datos = {
        'productos': productos
    }
    return render(request, 'mostrar.html', datos)


<<<<<<< HEAD
def agregar_producto(request, id):
    carrito_compra = Carrito(request)
=======

def agregar_producto(request,id):
    carrito_compra= Carrito(request)
>>>>>>> 85851ffd8f8e41941781c2d283594a5209847f8b
    producto = Producto.objects.get(idProducto=id)
    carrito_compra.agregar(producto=producto)
    return redirect('mostrar')

<<<<<<< HEAD

def eliminar_producto(request, id):
    carrito_compra = Carrito(request)
=======
def eliminar_producto(request, id):
    carrito_compra= Carrito(request)
>>>>>>> 85851ffd8f8e41941781c2d283594a5209847f8b
    producto = Producto.objects.get(idProducto=id)
    carrito_compra.eliminar(producto=producto)
    return redirect('mostrar')

<<<<<<< HEAD

def restar_producto(request, id):
    carrito_compra = Carrito(request)
=======
def restar_producto(request, id):
    carrito_compra= Carrito(request)
>>>>>>> 85851ffd8f8e41941781c2d283594a5209847f8b
    producto = Producto.objects.get(idProducto=id)
    carrito_compra.restar(producto=producto)
    return redirect('mostrar')

<<<<<<< HEAD

def limpiar_carrito(request):
    carrito_compra = Carrito(request)
    carrito_compra.limpiar()
    return redirect('mostrar')
=======
def limpiar_carrito(request):
    carrito_compra= Carrito(request)
    carrito_compra.limpiar()
    return redirect('mostrar')    
>>>>>>> 85851ffd8f8e41941781c2d283594a5209847f8b


def procesar_pago(request):
    if request.method == 'GET':
        if not request.session.get('carrito'):
            return render(request, 'webpay/plus/error.html', {'error': 'El carrito está vacío'})
        
        precio_total = 0
        for key, value in request.session['carrito'].items():
            precio_total += int(value['precio']) * int(value['cantidad'])
        buy_order = str(random.randrange(1000000, 99999999))
        session_id = str(random.randrange(1000000, 99999999))
        return_url = request.build_absolute_uri('/webpay-plus/commit')

        create_request = {
            "buy_order": buy_order,
            "session_id": session_id,
            "amount": precio_total,
            "return_url": return_url
        }

        try:
            response = Transaction().create(buy_order, session_id, precio_total, return_url)
            return render(request, 'webpay/plus/create.html', {'request': create_request, 'response': response})
        except Exception as e:
            return render(request, 'webpay/plus/error.html', {'error': str(e)})
    else:
        return render(request, 'webpay/plus/error.html', {'error': 'Método HTTP no permitido'})


def arriendo(request):
    if request.method == 'POST':
        form = ArriendoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Su solicitud fue enviado correctamente.')
            return redirect('arriendo')
        else:
            messages.error(request, 'Datos inválidos, por favor ingreselos nuevamente.')
    else:
        form = ArriendoForm()

<<<<<<< HEAD
    return render(request, 'arriendo.html', {'form': form})


## API
=======
    return  render(request, 'arriendo.html', {'form': form})
     
            

##API

>>>>>>> 85851ffd8f8e41941781c2d283594a5209847f8b

class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class BoletaList(generics.ListCreateAPIView):
    queryset = Boleta.objects.all()
    serializer_class = BoletaSerializer

class BoletaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Boleta.objects.all()
    serializer_class = BoletaSerializer

class DetalleBoletaList(generics.ListCreateAPIView):
    queryset = detalle_boleta.objects.all()
    serializer_class = DetalleBoletaSerializer

class DetalleBoletaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = detalle_boleta.objects.all()
    serializer_class = DetalleBoletaSerializer
<<<<<<< HEAD
=======

>>>>>>> 85851ffd8f8e41941781c2d283594a5209847f8b
