from django import forms
from .models import Producto, Arriendo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto 
        fields = ['idProducto', 'marca', 'nombre', 'categoria', 'imagen', 'precio']
        labels ={
            'idProducto':'IdProducto',
            'marca' : 'Marca',
            'nombre': 'Nombre',
            'categoria':'Categoria',
            'imagen':'Imagen',
            'precio':'Precio'
        }
        widgets={

            'idProducto':forms.TextInput(
                attrs={
                    'placeholder':'Ingrese el Id..',
                    'id': 'id',
                    'class': 'form-control',
                }
            ),
            'marca': forms.TextInput(
                attrs={
                    'placeholder':'Ingrese marca..',
                    'id':'marca',
                    'class':'form-control',
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'placeholder':'Ingrese nombre..',
                    'id':'nombre',
                    'class':'form-control',
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'id':'categoria',
                    'class':'form-control',
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class':'form-control',
                    'id': 'imagen',
                }
            ),

            'precio': forms.NumberInput(
                attrs={
                    'placeholder': 'Ingrese el precio..',
                    'id': 'precio',
                    'class': 'form-control',
                    'step': '0.01',
                    'min': '0',
                }
            ),
        }
class ArriendoForm(forms.ModelForm):
    class Meta:
        model = Arriendo
        fields = ['nombre', 'apellido', 'empresa' , 'email', 'cantidad']
        labels ={
            'nombre' : 'Nombre',
            'apellido' : 'Apellido',
            'empresa' : 'Empresa',
            'email' : 'Email',
            'cantidad' : 'Cantidad'
        }
        widgets={
            'nombre': forms.TextInput(
                attrs={
                'placerholder': 'Ingrese su nombre',
                'id' : 'nombre',
                'class' : 'form-control',
                }
            ),

            'apellido': forms.TextInput(
                attrs={
                'placerholder': 'Ingrese su apellido',
                'id' : 'apellido',
                'class' : 'form-control',
                }
            ),
            'empresa': forms.TextInput(
                attrs={
                'placerholder': 'Ingrese el nombre de la empresa',
                'id' : 'empresa',
                'class' : 'form-control',
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'placerholder': 'Ingrese su correo',
                    'id' : 'email',
                    'class' : 'form-control',
                }
            ),

            'cantidad': forms.NumberInput(
                attrs={
                'placerholder': 'Ingrese la cantidad que necesita',
                'id' : 'cantidad',
                'class' : 'form-control',
                'step': '0',
                'min': '0',                
                }
            )                                    
        }