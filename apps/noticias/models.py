from django.db import models
from django.conf import settings

class Categoria(models.Model):
    categoria_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    icono = models.CharField(max_length=50, default='fas fa-tag', help_text="Clase de icono Font Awesome")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Categorías"

class Autor(models.Model):
    autor_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=20)
    biografia = models.TextField(blank=True, null=True, help_text="Biografía del autor")
    email = models.EmailField(blank=True, null=True)
    imagen = models.ImageField(upload_to='autores/', blank=True, null=True, default='autores/default-author.png')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Autores"

class Noticia(models.Model):
    noticia_id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=85)
    subtitulo = models.CharField(max_length=150)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    categorias = models.ManyToManyField(Categoria) #Relacion n:m (muchos a muchos)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE) #Relación 1:n (uno a muchos)
    imagen_principal = models.ImageField(upload_to='noticias/', blank=True, null=True, help_text="Imagen principal de la noticia")
    activa = models.BooleanField(default=True, help_text="Noticia visible en el sitio")
    visitas = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.titulo

    def incrementar_visitas(self):
        self.visitas += 1
        self.save(update_fields=['visitas'])

    class Meta:
        verbose_name_plural = "Noticias"
        ordering = ['-fecha']

class ImagenNoticia(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name='imagenes_adicionales')
    imagen = models.ImageField(upload_to='noticias/galeria/')
    descripcion = models.CharField(max_length=200, blank=True)
    orden = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Imagen de {self.noticia.titulo}"

    class Meta:
        ordering = ['orden']

class Comentario(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.usuario.username} - {self.noticia.titulo[:30]}'

    class Meta:
        ordering = ['-fecha']  

# class Persona(models.Model):
#     id_persona = models.AutoField(primary_key=True)
#     nombre = models.CharField(max_length=100)
#     apellido = models.CharField(max_length=100)

# class Perfil(models.Model):
#     id_perfil = models.AutoField(primary_key=True)
#     biografia = models.TextField()
#     persona = models.OneToOneField(Persona, on_delete=models.CASCADE)

