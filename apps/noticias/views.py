from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Noticia, Autor, Categoria, Comentario


# VISTA BASADA EN FUNCIONES (FBV) - LISTAR TODAS LAS NOTICIAS
def todas_las_noticias(request):
    categoria_param = request.GET.get("categoria", "").strip()
    busqueda = request.GET.get("busqueda", "").strip()
    ordenamiento = request.GET.get("orden", "").strip()

    # Buscar todas las noticias activas desde la base de datos.
    noticias = Noticia.objects.filter(activa=True).select_related('autor').prefetch_related('categorias')

    # Filtrar por categoría
    if categoria_param:
        noticias = noticias.filter(categorias__nombre__icontains=categoria_param)

    # Filtrar por búsqueda
    if busqueda:
        noticias = noticias.filter(
            Q(titulo__icontains=busqueda) |
            Q(subtitulo__icontains=busqueda) |
            Q(contenido__icontains=busqueda)
        )

    # Aplicar ordenamiento
    if ordenamiento == 'fecha_asc':
        noticias = noticias.order_by('fecha')
    elif ordenamiento == 'fecha_desc':
        noticias = noticias.order_by('-fecha')
    elif ordenamiento == 'titulo_asc':
        noticias = noticias.order_by('titulo')
    elif ordenamiento == 'titulo_desc':
        noticias = noticias.order_by('-titulo')
    else:
        noticias = noticias.order_by('-fecha')  # Por defecto más recientes primero

    # Paginación
    paginator = Paginator(noticias, 6)  # 6 noticias por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Obtener todas las categorías para el filtro
    categorias = Categoria.objects.all()

    # Meterlas en un contexto.
    context = {
        "noticias": page_obj,
        "categorias": categorias,
        "categoria_seleccionada": categoria_param,
        "busqueda": busqueda,
        "ordenamiento": ordenamiento
    }

    # Renderizar el html con el contexto.
    return render(request, "noticias/todas_noticias.html", context)


# VISTA BASADA EN FUNCIONES (FBV) - DETALLE DE UNA NOTICIA
def una_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, noticia_id=noticia_id, activa=True)
    
    # Incrementar visitas
    noticia.incrementar_visitas()
    
    # Obtener comentarios activos
    comentarios = noticia.comentarios.filter(activo=True).select_related('usuario')
    
    # Procesar formulario de comentario
    if request.method == "POST" and request.user.is_authenticated:
        contenido = request.POST.get('contenido', '').strip()
        if contenido:
            Comentario.objects.create(
                noticia=noticia,
                usuario=request.user,
                contenido=contenido
            )
            messages.success(request, 'Comentario agregado exitosamente.')
            return redirect('una_noticia', noticia_id=noticia_id)
    
    # Noticias relacionadas (misma categoría)
    noticias_relacionadas = Noticia.objects.filter(
        categorias__in=noticia.categorias.all(),
        activa=True
    ).exclude(noticia_id=noticia_id).distinct()[:3]
    
    context = {
        "noticia": noticia,
        "comentarios": comentarios,
        "noticias_relacionadas": noticias_relacionadas
    }
    return render(request, "noticias/una_noticia.html", context)


# VISTA BASADA EN FUNCIONES (FBV) - CREAR NUEVA NOTICIA
@login_required
def crear_noticia(request):
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        subtitulo = request.POST.get('subtitulo')
        contenido = request.POST.get('contenido')
        autor_id = request.POST.get('autor')
        categorias_ids = request.POST.getlist('categorias')
        imagen_principal = request.FILES.get('imagen_principal')

        # Validaciones básicas
        if not all([titulo, subtitulo, contenido, autor_id]):
            messages.error(request, 'Todos los campos son obligatorios.')
            return render(request, "noticias/nueva_noticia.html", {
                'autores': Autor.objects.all(),
                'categorias': Categoria.objects.all()
            })

        # Crear la noticia
        noticia = Noticia.objects.create(
            titulo=titulo,
            subtitulo=subtitulo,
            contenido=contenido,
            autor_id=autor_id,
            imagen_principal=imagen_principal
        )
        
        # Asignar categorías
        if categorias_ids:
            noticia.categorias.set(categorias_ids)

        messages.success(request, 'Noticia creada exitosamente.')
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
@login_required
def actualizar_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, noticia_id=noticia_id)
    
    if request.method == "POST":
        noticia.titulo = request.POST.get('titulo')
        noticia.subtitulo = request.POST.get('subtitulo')
        noticia.contenido = request.POST.get('contenido')
        autor_id = request.POST.get('autor')
        if autor_id:
            noticia.autor_id = autor_id
        
        # Manejar imagen
        if 'imagen_principal' in request.FILES:
            noticia.imagen_principal = request.FILES['imagen_principal']
        
        categorias_ids = request.POST.getlist('categorias')
        
        noticia.save()
        
        # Actualizar categorías
        if categorias_ids:
            noticia.categorias.set(categorias_ids)

        messages.success(request, 'Noticia actualizada exitosamente.')
        return redirect("una_noticia", noticia_id=noticia_id)

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
@login_required
def eliminar_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, noticia_id=noticia_id)

    if request.method == "POST":
        noticia.delete()
        messages.success(request, 'Noticia eliminada exitosamente.')
        return redirect("todas_las_noticias")

    context = {"noticia": noticia}
    return render(request, "noticias/eliminar_noticia.html", context)


# VISTA BASADA EN FUNCIONES (FBV) - PÁGINA ACERCA DE
def acerca_de(request):
    context = {
        'equipo': [
            {
                'nombre': 'Aldo Andrés Acosta', 
                'rol': '',
                'descripcion': '',
                'github': 'Andres777777'
            },
            {
                'nombre': 'Valentino André Cabás',
                'rol': '',
                'descripcion': '',
                'github': 'Valen-cbs'
            },
                        {
                'nombre': 'Nahuel Vallejos',
                'rol': '',
                'descripcion': '',
                'github': 'Nahuel151'
            },
            {
                'nombre': 'Integrante4',
                'rol': '',
                'descripcion': '',
                'github': ''
            },
            {
                'nombre': 'Integrante5',
                'rol': '',
                'descripcion': '',
                'github': ''
            },
            {
                'nombre': 'Integrante6',
                'rol': '',
                'descripcion': '',
                'github': ''
            },
            {
                'nombre': 'Juan Diego González Antoniazzi',
                'rol': 'Desarrollador Full Stack',
                'descripcion': 'Scrum Master y Tester QA',
                'github': 'JDGA1997'
            }
        ]
    }
    return render(request, 'acerca_de.html', context)


# VISTA BASADA EN FUNCIONES (FBV) - PÁGINA CONTACTO
def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')
        
        # Aquí podrías agregar lógica para enviar email o guardar en BD
        # Por ahora solo mostramos mensaje de éxito
        messages.success(request, f'¡Gracias {nombre}! Tu mensaje ha sido enviado correctamente. Te responderemos pronto.')
        return redirect('contacto')
    
    return render(request, 'contacto.html')
    return render(request, "noticias/eliminar_noticia.html", context)