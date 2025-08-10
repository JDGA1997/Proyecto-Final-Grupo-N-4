from django.shortcuts import render, redirect, get_object_or_404
from .models import Noticia, Autor, Categoria


# VISTA BASADA EN FUNCIONES (FBV) - LISTAR TODAS LAS NOTICIAS
def todas_las_noticias(request):
    categoria_param = request.GET.get("categoria", "").strip()

    # Buscar todas las noticias desde la base de datos.
    noticias = Noticia.objects.all()

    if categoria_param:
        noticias = noticias.filter(categorias__nombre__icontains=categoria_param)

    # Meterlas en un contexto.
    context = {"noticias": noticias, "categoria_seleccionada": categoria_param}

    # Renderizar el html con el contexto.
    return render(request, "noticias/todas_noticias.html", context)


# VISTA BASADA EN FUNCIONES (FBV) - DETALLE DE UNA NOTICIA
def una_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, noticia_id=noticia_id)
    context = {"noticia": noticia}
    return render(request, "noticias/una_noticia.html", context)


# VISTA BASADA EN FUNCIONES (FBV) - CREAR NUEVA NOTICIA
def crear_noticia(request):
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        subtitulo = request.POST.get('subtitulo')
        contenido = request.POST.get('contenido')
        autor_id = request.POST.get('autor')
        categorias_ids = request.POST.getlist('categorias')

        # Crear la noticia
        noticia = Noticia.objects.create(
            titulo=titulo,
            subtitulo=subtitulo,
            contenido=contenido,
            autor_id=autor_id
        )
        
        # Asignar categorías
        if categorias_ids:
            noticia.categorias.set(categorias_ids)

        return redirect("todas_las_noticias")

    # Si es GET, mostrar el formulario
    autores = Autor.objects.all()
    categorias = Categoria.objects.all()
    context = {
        'autores': autores,
        'categorias': categorias
    }
    return render(request, "noticias/nueva_noticia.html", context)


# VISTA BASADA EN FUNCIONES (FBV) - ACTUALIZAR NOTICIA
def actualizar_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, noticia_id=noticia_id)
    
    if request.method == "POST":
        noticia.titulo = request.POST.get('titulo')
        noticia.subtitulo = request.POST.get('subtitulo')
        noticia.contenido = request.POST.get('contenido')
        autor_id = request.POST.get('autor')
        if autor_id:
            noticia.autor_id = autor_id
        
        categorias_ids = request.POST.getlist('categorias')
        
        noticia.save()
        
        # Actualizar categorías
        if categorias_ids:
            noticia.categorias.set(categorias_ids)

        return redirect("todas_las_noticias")

    # Si es GET, mostrar el formulario con datos actuales
    autores = Autor.objects.all()
    categorias = Categoria.objects.all()
    context = {
        'noticia': noticia,
        'autores': autores,
        'categorias': categorias
    }
    return render(request, "noticias/actualizar_noticia.html", context)


# VISTA BASADA EN FUNCIONES (FBV) - ELIMINAR NOTICIA
def eliminar_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, noticia_id=noticia_id)

    if request.method == "POST":
        noticia.delete()
        return redirect("todas_las_noticias")

    return render(request, "noticias/eliminar_noticia.html", {"noticia": noticia})