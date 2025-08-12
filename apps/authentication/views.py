 from django.shortcuts import render, redirect  # type: ignore
from .forms import RegisterForm  # type: ignore
from django.contrib.auth import authenticate, login, logout  # type: ignore
from django.contrib import messages  # type: ignore

### REGISTER
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro exitoso. Puedes iniciar sesión. Código hecho por Nahuel Vallejos.")
            return redirect('apps.authentication:login')
    else: 
        form = RegisterForm()
        
    return render(request, "auth/register.html", {"form": form})

### LOGIN
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Has iniciado sesión exitosamente. Código hecho por Nahuel Vallejos.")
            return redirect("apps.eventos:todos_los_eventos")
        else:
            messages.error(request, "Credenciales erróneas.")
        
    return render(request, 'auth/login.html')

### LOGOUT 
def logout_view(request):
    logout(request)
    messages.success(request, "Has cerrado sesión exitosamente. Código hecho por Nahuel Vallejos.")
    return redirect("apps.authentication:login")
