from distutils.command.upload import upload # type: ignore
from django.db import models
import datetime
from django.core.validators import MinLengthValidator

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de Categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de Categoria')

    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    idProducto = models.CharField(max_length=6, primary_key=True, verbose_name='Id de Producto')
    marca = models.CharField(max_length=20, verbose_name='Marca')
    nombre = models.CharField(max_length=40, verbose_name='Nombre de producto')
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True, verbose_name='Imagen')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")
    precio = models.IntegerField(blank=True, null=True, verbose_name="Precio")

    def __str__(self):
        return self.idProducto

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

class Arriendo(models.Model):
    idPedido = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, verbose_name="Nombre")
    apellido = models.CharField(max_length=20, verbose_name="Apellido")
    empresa = models.CharField(max_length=60, verbose_name="Empresa")
    email = models.EmailField(verbose_name="Email")
    cantidad = models.IntegerField(blank=True, null=True, verbose_name="Cantidad")
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - Pedido {self.idPedido}"

class User(models.Model):
    email = models.EmailField(unique=True, verbose_name='Correo Electrónico')
    password = models.CharField(max_length=50, validators=[MinLengthValidator(8)], verbose_name='Contraseña')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    apellido = models.CharField(max_length=50, verbose_name='Apellido')
    direccion = models.CharField(max_length=255, verbose_name='Dirección')
    rut = models.CharField(max_length=12, unique=True, verbose_name='RUT')

    def __str__(self):
        return self.email

