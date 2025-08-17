from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from functools import wraps

def perfil_requerido(*perfiles_permitidos):
    def decorator(view_func):
        @wraps(view_func)
        @login_required
        def _wrapped_view(request, *args, **kwargs):
            if request.user.tipo_perfil in perfiles_permitidos:
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("No tienes permiso para acceder aquí.")
        return _wrapped_view
    return decorator
