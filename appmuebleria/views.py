from django.shortcuts import render
from django.http import HttpResponse
from appmuebleria.models import *
from django.template import Template, Context, loader
from appmuebleria.forms import *

# Create your views here.
def vendedor (request):  
    if request.method == "POST":
        miFormulario = VendedorFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            vendedor = Vendedor (nombre=informacion["nombre"], cbu=informacion["cbu"])
            vendedor.save()
            return render (request, "appmuebleria/inicio.html")
    else:
        miFormulario = VendedorFormulario()
           
    return render (request, "appmuebleria/vendedor.html",{"miFormulario":miFormulario})

def cliente (request):
    if request.method == "POST":
        miFormulario = ClienteFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            cliente = Cliente (nombre=informacion["nombre"], direccion=informacion["direccion"], telefono=informacion["telefono"], email=informacion["email"])
            cliente.save()
            return render (request, "appmuebleria/inicio.html")
    else:
        miFormulario = ClienteFormulario()
    
    return render (request, "appmuebleria/cliente.html", {"miFormulario":miFormulario})

def producto (request):
    
    if request.method == "POST":
        miFormulario = ProductoFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            producto = Producto (codigo=informacion["codigo"], descripcion=informacion["descripcion"], precio=informacion["precio"])
            producto.save()
            return render (request, "appmuebleria/inicio.html")
    else:
        miFormulario = ProductoFormulario()
    
    return render (request, "appmuebleria/producto.html",{"miFormulario":miFormulario})

def inicio (request):
    
    return render (request, "appmuebleria/inicio.html")

def buscarProducto (request):
    
    return render (request, "appmuebleria/buscarProducto.html")

def buscar (request):
    
    if request.GET["codigo"]:
        codigo = request.GET['codigo']
        productos = Producto.objects.filter(codigo__icontains=codigo)
        
        return render (request, "appmuebleria/resultadoBusqueda.html", {"productos":productos, "codigo":codigo})
    
    else:
        
        respuesta ="No enviaste datos"
    
    return HttpResponse (respuesta)

def catalogo (request):
    
    return render (request, "appmuebleria/catalogo.html")
