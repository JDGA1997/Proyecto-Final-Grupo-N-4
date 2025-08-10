from django.urls import path
from .views import (
    todas_las_noticias,
    una_noticia,
    crear_noticia,
    actualizar_noticia,
    eliminar_noticia,
    acerca_de,
    contacto
)

#http://127.0.0.1:8000/noticias/

urlpatterns = [
    # Ruta principal para noticias
    path('', todas_las_noticias, name="todas_las_noticias"),
    
    # Detalle de una noticia
    path('<int:noticia_id>/', una_noticia, name='una_noticia'),
    
    # CRUD operations
    path('crear/', crear_noticia, name='crear_noticia'),
    path('actualizar/<int:noticia_id>/', actualizar_noticia, name='actualizar_noticia'),
    path('eliminar/<int:noticia_id>/', eliminar_noticia, name='eliminar_noticia'),
    
    # Páginas adicionales
    path('acerca-de/', acerca_de, name='acerca_de'),
    path('contacto/', contacto, name='contacto'),
]