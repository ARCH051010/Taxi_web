from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required  # <-- Importar decorador
from .forms import ReservacionForm
from .models import Reservacion
from .forms import ClienteForm, ConductorForm
from .models import Cliente, Conductor



def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm,
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1']
                )
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'El usuario ya existe'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'Contraseñas no coinciden'
        })






@login_required(login_url='login')
def reservas(request):
    reservas = Reservacion.objects.all()
    form = ReservacionForm()  # <-- Agregamos esto
    return render(request, 'reservas.html', {'reservas': reservas, 'form': form})

@login_required(login_url='login')
def reserva_create(request):
    if request.method == 'POST':
        form = ReservacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservas')
    else:
        form = ReservacionForm()
    return render(request, 'reservas.html', {'form': form, 'reservas': Reservacion.objects.all()})

@login_required(login_url='login')
def reserva_edit(request, pk):
    reserva = get_object_or_404(Reservacion, pk=pk)
    if request.method == 'POST':
        form = ReservacionForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('reservas')
    else:
        form = ReservacionForm(instance=reserva)
    return render(request, 'reservas.html', {'form': form, 'reservas': Reservacion.objects.all(), 'reserva_to_edit': reserva})

@login_required(login_url='login')
def reserva_delete(request,pk):
    reserva = get_object_or_404(Reservacion, pk=pk)
    reserva.delete()
    return redirect('reservas')





@login_required(login_url='login')
def clientes(request):
    clientes = Cliente.objects.all()
    form = ClienteForm()  # <-- Agregamos esto
    return render(request, 'clientes.html', {'clientes': clientes, 'form': form})

@login_required(login_url='login')
def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes.html', {'form': form, 'clientes': Cliente.objects.all()})

@login_required(login_url='login')
def cliente_edit(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes.html', {'form': form, 'clientes': Cliente.objects.all(), 'cliente_to_edit': cliente})

@login_required(login_url='login')
def cliente_delete(request,pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()
    return redirect('clientes')





@login_required(login_url='login')
def conductor(request):
    conductores = Conductor.objects.all()
    form = ConductorForm()  # <-- Agregamos esto
    return render(request, 'conductores.html', {'conductores': conductores, 'form': form})

@login_required(login_url='login')
def conductor_create(request):
    if request.method == 'POST':
        form = ConductorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('conductores')
    else:
        form = ConductorForm()
    return render(request, 'conductores.html', {'form': form, 'conductores': Conductor.objects.all()})

@login_required(login_url='login')
def conductor_edit(request, pk):
    conductor = get_object_or_404(Conductor, pk=pk)
    if request.method == 'POST':
        form = ConductorForm(request.POST, instance=conductor)
        if form.is_valid():
            form.save()
            return redirect('conductores')
    else:
        form = ConductorForm(instance=conductor)
    return render(request, 'conductores.html', {'form': form, 'conductores': Conductor.objects.all(), 'conductor_to_edit': conductor})

@login_required(login_url='login')
def conductor_delete(request,pk):
    conductor = get_object_or_404(Conductor, pk=pk)
    conductor.delete()
    return redirect('conductores')





def cerrar(request):
    logout(request)
    return redirect('home')

def entrar(request):
    if request.method == 'GET':
        return render(request, "login.html", {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is None:
            return render(request, "login.html", {
                'form': AuthenticationForm,
                'error': 'Usuario o Contraseña incorrectos'
            })
        else:
            login(request, user)
            return redirect('home')
