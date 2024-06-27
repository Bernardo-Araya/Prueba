from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app_obras.compra import Carrito
from django.http import HttpResponse
import random
from transbank.error.transbank_error import TransbankError
from transbank.webpay.webpay_plus.transaction import Transaction
from rest_framework import generics

from app_obras.forms import ProductoForm
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

def arriendo(request):
	productos= Producto.objects.all()
	
	return render(request, 'arriendo.html',context={'datos':productos})

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

def mostrar(request):
    try:
        response = requests.get('http://127.0.0.1:8000/api/productos/')
        response.raise_for_status()
        productos = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener productos de la API: {e}")
        productos = []

    tasa_de_cambio = obtener_tasa_de_cambio()
    if tasa_de_cambio is not None:
        for producto in productos:
            producto['precio_usd'] = round(producto['precio'] * tasa_de_cambio, 2)
    else:
        for producto in productos:
            producto['precio_usd'] = 'N/A'

    datos = {
        'productos': productos
    }
    return render(request, 'mostrar.html', datos)



def agregar_producto(request,id):
    carrito_compra= Carrito(request)
    producto = Producto.objects.get(idProducto=id)
    carrito_compra.agregar(producto=producto)
    return redirect('mostrar')

def eliminar_producto(request, id):
    carrito_compra= Carrito(request)
    producto = Producto.objects.get(idProducto=id)
    carrito_compra.eliminar(producto=producto)
    return redirect('mostrar')

def restar_producto(request, id):
    carrito_compra= Carrito(request)
    producto = Producto.objects.get(idProducto=id)
    carrito_compra.restar(producto=producto)
    return redirect('mostrar')

def limpiar_carrito(request):
    carrito_compra= Carrito(request)
    carrito_compra.limpiar()
    return redirect('mostrar')    


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


##API


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


