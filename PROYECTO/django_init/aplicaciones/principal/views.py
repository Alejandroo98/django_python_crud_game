from django.shortcuts import render , redirect
from .forms import PersonaForm
from .models import Persona

def inicio( request ):
    if request.method == 'GET' :
        personas = Persona.objects.all().order_by('-puntaje')
        contexto = {
            'personas' : personas[:10]
        }
        return render( request , 'index.html' , contexto  )
    else : 
        form = PersonaForm(request.POST)
        contexto = {
            'form' : form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render( request , 'index.html' , contexto  )

