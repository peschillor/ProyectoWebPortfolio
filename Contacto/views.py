from django.shortcuts import render,redirect
from .forms import FormularioContacto

# Create your views here.
def contacto(request):
    data={
        'form': FormularioContacto()
    }
    
    if request.method == 'POST':
        formulario = FormularioContacto(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]= "Se ha enviado correctamente"
        else:
            data["form"] = formulario    
       
    return render(request,"Contacto/contacto.html",data)

