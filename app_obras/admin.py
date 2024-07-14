from django.contrib import admin
from .models import Categoria, Producto,Boleta,detalle_boleta,Arriendo
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Boleta)
admin.site.register(detalle_boleta)
admin.site.register(Arriendo)