from django.shortcuts import render, get_object_or_404, redirect
from .models import Animes, Usuarios
from django.contrib.auth import authenticate, login
from django.contrib import messages

def webapp(request):
    messages.get_messages(request)  # Obtener mensajes almacenados
    return render(request, 'webapp/index.html')

def anime_detail(request, anime_id):
    anime = get_object_or_404(Animes, id_anime=anime_id)
    return render(request, 'webapp/anime_detail.html', {'anime': anime})

def agregar_anime(request):
    if request.method == 'POST':
        id_anime = request.POST['id_anime']
        nombre_anime = request.POST['nombre_anime']
        anime = Animes(id_anime=id_anime, nombre_anime=nombre_anime)
        anime.save()
    
    animes = Animes.objects.all()
    
    return render(request, 'webapp/agregar_anime.html', {'animes': animes})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Inicio de sesión exitoso.')
            return redirect('/')  # Cambia '/' con la URL de tu página principal
        else:
            messages.error(request, 'Credenciales inválidas. Inténtalo de nuevo.')
            return redirect('/login')  # Cambia '/login' con la URL de tu página de inicio de sesión

    return render(request, 'webapp/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        email = request.POST['email']

        try:
            Usuarios.objects.get(usuario=username)
            messages.error(request, 'El usuario ya existe. Por favor, elige otro nombre de usuario.')
        except Usuarios.DoesNotExist:
            # Realizar las acciones necesarias para registrar al usuario
            # Crea una instancia de Usuarios y guarda los datos
            user = Usuarios(usuario=username, nombre=nombre, apellido=apellido, correo=email)
            user.set_password(password)  # Establecer la contraseña utilizando el método set_password()
            user.save()
            messages.success(request, 'Registro exitoso. Inicia sesión con tu nueva cuenta.')
            return redirect('/login')  # Cambia 'login' con la URL de tu página de inicio de sesión

    return render(request, 'webapp/register.html')

