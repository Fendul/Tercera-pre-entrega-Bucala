from django.urls import path
from appmuebleria.views import *

urlpatterns = [
    
    path('vendedor/', vendedor , name= "vendedor"),
    path('cliente/', cliente, name="cliente"),
    path('producto/', producto, name="producto"),
    path("inicio/", inicio, name="inicio"),
    path("contacto/", contacto, name="contacto"),
   
]