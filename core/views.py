from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.


def index (request):
    mecanicos = Empleado.objects.all()
    aux = {
        'lista' : mecanicos
    }
    return render(request, 'core/index.html', aux)

def vehiculos (request):

    return render(request, 'core/vehiculos.html')

def about (request):
    return render(request, 'core/about.html')

def contact (request):
    return render(request, 'core/contact.html')


def mecanicos (request):
    mecanicos = Empleado.objects.all()
    aux = {
        'lista' : mecanicos
    }
    return render(request, 'core/mecanicos.html', aux)


def services (request):
    return render(request, 'core/services.html')

def listarmecanicos (request,):
    mecanicos = Empleado.objects.all()
    aux = {
        'lista' : mecanicos
    }
    return render(request, 'core/listarmecanicos.html', aux )



def administrador(request):
    mecanicos = Empleado.objects.all()
    aux = {
        'lista': mecanicos
    }
    return render(request, 'core/indexadmin.html', aux)

def empleadosadd (request):
    aux = {
        'forms' : empleadoform()
    }
    if request.method == 'POST':
        formulario = empleadoform(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "EMPLEADO GUARDADO CORRECTAMENTE")
        else:
            aux['forms'] = formulario
            messages.error(request, "NO SE PUDO GUARDAR EL EMPELADO")
    return render(request, 'core/crud/add.html',aux)


def empleadosupdate(request, id):
    empleado = get_object_or_404(Empleado, pk=id)
    if request.method == 'POST':
        formulario = empleadoform(request.POST, request.FILES, instance=empleado)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "EMPLEADO ACTUALIZADO CORRECTAMENTE")
            return redirect('listarmecanicos')  # Redirigir a la lista de mecánicos después de actualizar
    else:
        formulario = empleadoform(instance=empleado)
    
    aux = {'forms': formulario}
    return render(request, 'core/crud/update.html', aux)


def empleadosdelete(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    empleado.delete()
    messages.success(request, "ELIMINADO CORRECTAMENTE")
    return redirect('listarmecanicos')



def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            user = formulario.save()
            user = authenticate(username=user.username, password=request.POST['password1'])
            if user is not None:
                login(request, user)
                messages.success(request, "Te has registrado correctamente")
                if user.is_superuser or user.is_staff:
                    return redirect('admin:index')
                else:
                    return redirect('login')
            else:
                messages.error(request, "Error en la autenticación. Por favor, verifica tus credenciales.")
        else:
            data['form'] = formulario
            messages.error(request, "Formulario no válido. Por favor, corrige los errores.")
    
    return render(request, 'registration/register.html', data)