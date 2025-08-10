from django.contrib import admin
from .models import Noticia, Categoria, Autor, ImagenNoticia, Comentario

class ImagenNoticiaInline(admin.TabularInline):
    model = ImagenNoticia
    extra = 1

class ComentarioInline(admin.TabularInline):
    model = Comentario
    extra = 0
    readonly_fields = ('fecha',)

class NoticiaAdmin(admin.ModelAdmin):
    fields = ('titulo', 'subtitulo', 'contenido', 'autor', 'categorias', 'imagen_principal', 'activa')
    
    list_display = ('titulo', 'autor', 'fecha', 'activa', 'visitas')
    list_filter = ('fecha', 'autor', 'categorias', 'activa')
    search_fields = ('titulo', 'contenido', 'autor__nombre')
    list_editable = ('activa',)
    readonly_fields = ('fecha', 'fecha_actualizacion', 'visitas')
    
    filter_horizontal = ('categorias',)
    inlines = [ImagenNoticiaInline, ComentarioInline]
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'icono')
    search_fields = ('nombre',)

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nacionalidad', 'email')
    search_fields = ('nombre', 'email')
    fields = ('nombre', 'nacionalidad', 'biografia', 'email', 'imagen')

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'noticia', 'fecha', 'activo')
    list_filter = ('fecha', 'activo')
    search_fields = ('usuario__username', 'noticia__titulo', 'contenido')
    list_editable = ('activo',)
    readonly_fields = ('fecha',)

admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Comentario, ComentarioAdmin)

# Personalización del admin
admin.site.site_header = "Portal de Noticias - Robótica | Grupo N°4"
admin.site.site_title = "Admin Portal - Grupo N°4"
admin.site.index_title = "Administración del Portal - Grupo N°4"
