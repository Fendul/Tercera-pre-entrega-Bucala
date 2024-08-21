from django import forms

class ClienteFormulario (forms.Form):
    nombre = forms.CharField()
    direccion = forms.CharField()
    telefono = forms.IntegerField()
    email = forms.EmailField()
    
class ProductoFormulario (forms.Form):
    codigo = forms.IntegerField()
    descripcion = forms.CharField()
    precio = forms.DecimalField()
    
class VendedorFormulario (forms.Form):
    nombre = forms.CharField()
    cbu = forms.IntegerField()