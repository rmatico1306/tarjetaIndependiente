

# Create your views here.
from django.shortcuts import render
#instacioamos la vista generica de django
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.messages import*
from django.forms.forms import Form
from django import forms
from django.shortcuts import redirect, render
from .models import*
from .form import UserRegisterForm
from django.urls import reverse


def search_beneficery(request, persona_id):
    beneficiary=Persona.objects.get(id= persona_id)
    return render(request,"create.html",{"beneficiary":beneficiary})

def tarjeta(request):
    tarjetas=Tarjeta.objects.all()  
    def hello():
        return "hola"

    return render(request,"principal.html",{"tarjeta":tarjetas, "hello":hello})
    
def login_usuario(request):
    return render(request,"index.html")

def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            
            username=form.cleaned_data['username']
            messages.success(request,f'Usuario{username} creado')
            form.save()
            # REdirect para redireccionar a la pagina de inicio 
            return redirect('Home')
    else:
        form= UserRegisterForm()
    context={'form':form}
    return render(request,'register.html', context)
def getOut(request):
    logout(request)
    messages.success(request, F"Tu session Se ha Cerrado Correctamente")
    return redirect("/")
#CRUD  tomado de la pagina https://blog.nubecolectiva.com/como-crear-un-crud-con-django-2-y-bootstrap-4-parte-3-python-3-7/
#cramos la Tarjeta
class ListCard(ListView):
    model=Tarjeta
class CreateCard(SuccessMessageMixin, CreateView):
    model= Tarjeta
    form=  Tarjeta
    fields = "__all__" 
    success_message='  Creado exitosamente'
    def get_success_url(self):        
        return reverse('Home')
class DetailCard(DetailView):
    model=Tarjeta
    form= Tarjeta
    fields= "__all__"
class  UpdateCard(SuccessMessageMixin, UpdateView):
    model=Tarjeta
    form= Tarjeta
    fields= "__all__"
    success_message='Tarjeta Actualizada'
    def get_success_url(self):
        return reverse('Home') #Redirecccinamos a la pagina principal 

class DeleteCard(SuccessMessageMixin, DeleteView):
    model= Tarjeta
    form=  Tarjeta
    fields = "__all__" 
    success_message=' Tarjeta Eliminada '  
    def get_success_url(self):  
        success_message=' Tarjeta Eliminada '    
        messages.success(self.request,(success_message))  
        return reverse('Home')
class CreateBeneficery(SuccessMessageMixin, CreateView):
    model= Persona
    form=  Persona
    fields = "__all__" 
    success_message='  Creado exitosamente'
    def get_success_url(self):        
        return reverse('Home')

  

   