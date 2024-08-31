from django.urls import path
from appmuebleria.views import *

urlpatterns = [
    
    path('vendedor/', vendedor , name= "vendedor"),
    path('cliente/', cliente, name="cliente"),
    path('producto/', producto, name="producto"),
    path("inicio/", inicio, name="inicio"),
    path("", inicio, name="inicio"),
    path("buscarProducto/", buscarProducto, name="buscarProducto"),
    path("buscar/", buscar),
    path("catalogo/", catalogo, name="catalogo"),
   
]