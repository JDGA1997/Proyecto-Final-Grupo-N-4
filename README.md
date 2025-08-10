<div align="center">
  <img src="https://github.com/user-attachments/assets/df02cfe1-dd25-41d8-9cc3-2cea31e60d1a" alt="Logo del Proyecto" width="400"/>

# 🤖 Portal de Noticias sobre Robótica
## Proyecto Final - Desarrollo Web con Django - Grupo N°4

[![Django](https://img.shields.io/badge/Django-5.2.4-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.1.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![Pillow](https://img.shields.io/badge/Pillow-11.3.0-4285F4?style=for-the-badge&logo=python&logoColor=white)](https://pillow.readthedocs.io/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
![Estado](https://img.shields.io/badge/Estado-Completado-brightgreen?style=for-the-badge)

*Portal moderno de noticias especializadas en robótica, automatización industrial y tecnología robótica del futuro*

</div>

---

## 📋 Tabla de Contenidos

- [🚀 Descripción General](#-descripción-general)
- [✨ Nuevas Funcionalidades Implementadas](#-nuevas-funcionalidades-implementadas)
- [🛠️ Stack Tecnológico](#️-stack-tecnológico)
- [📁 Estructura del Proyecto](#-estructura-del-proyecto)
- [⚙️ Instalación y Configuración](#️-instalación-y-configuración)
- [🎯 Funcionalidades Principales](#-funcionalidades-principales)
- [🌐 Navegación y Páginas](#-navegación-y-páginas)
- [📱 Diseño Responsive](#-diseño-responsive)
- [🔧 Configuración Adicional](#-configuración-adicional)
- [👥 Créditos](#-créditos)

---

## 🚀 Descripción General

El **Portal de Noticias sobre Robótica** es una aplicación web moderna desarrollada con Django que se especializa en noticias y contenido relacionado con robótica, automatización industrial y tecnología robótica del futuro. Este proyecto implementa las mejores prácticas de desarrollo web y ofrece una experiencia de usuario moderna y responsiva.

### Características Destacadas

| Característica | Descripción | Estado |
|:---------------|:------------|:------:|
| **🎨 UI Moderna** | Interfaz Bootstrap 5 con efectos visuales | ✅ |
| **📱 Responsive** | Adaptable a móviles, tablets y desktop | ✅ |
| **🔐 Autenticación** | Sistema de usuarios integrado | ✅ |
| **📸 Multimedia** | Soporte completo para imágenes | ✅ |
| **🔍 Búsqueda Avanzada** | Filtrado inteligente y ordenamiento | ✅ |
| **💬 Comentarios** | Sistema completo de comentarios | ✅ |
| **📄 Páginas Completas** | Acerca de, Contacto, Detalles | ✅ |
| **🏷️ Ordenamiento** | Por fecha y alfabético (ASC/DESC) | ✅ |
| **⚡ Performance** | Optimizado para velocidad | ✅ |
| **🛡️ Seguridad** | CSRF protection y validaciones | ✅ |

---

## ✨ Nuevas Funcionalidades Implementadas

### 🔍 **Sistema de Ordenamiento Avanzado**
- ✅ **Ordenamiento por fecha**: Ascendente (más antiguos primero) y Descendente (más recientes primero)
- ✅ **Ordenamiento alfabético**: Ascendente (A-Z) y Descendente (Z-A)
- ✅ **Interfaz intuitiva**: Dropdown con opciones claras para el usuario
- ✅ **Persistencia de filtros**: Los filtros se mantienen al navegar entre páginas
- ✅ **Combinación de filtros**: Ordenamiento + búsqueda + categoría simultáneamente

### 📄 **Página de Detalle de Noticia** (`una_noticia.html`)
- ✅ **Vista completa del artículo** con imagen destacada y contenido completo
- ✅ **Información del autor** con foto de perfil y biografía
- ✅ **Metadatos de la noticia** (fecha, categorías, número de visitas)
- ✅ **Sistema de comentarios** integrado con formulario de envío
- ✅ **Botones de compartir** en redes sociales (Facebook, Twitter, LinkedIn)
- ✅ **Sidebar con noticias relacionadas** para aumentar engagement
- ✅ **Navegación mejorada** con enlaces de regreso y acciones rápidas

### 🏢 **Página "Acerca de"**
- ✅ **Información completa del blog** con misión y visión del proyecto
- ✅ **Perfiles del equipo** con fotografías y roles de cada miembro
- ✅ **Descripción del proyecto académico** con contexto del Informatorio
- ✅ **Stack tecnológico visual** con badges y descripciones
- ✅ **Hero section moderna** con gradiente y tipografía profesional
- ✅ **Cards responsivas** para cada miembro del equipo

### 📧 **Página "Contacto"**
- ✅ **Formulario de contacto completo** con validación frontend y backend
- ✅ **Múltiples opciones de asunto** (General, Soporte Técnico, Colaboración, etc.)
- ✅ **Información de contacto** con direcciones y datos del equipo
- ✅ **Sección de FAQ** con preguntas frecuentes en formato accordion
- ✅ **Sistema de mensajes** para confirmación de envío exitoso
- ✅ **Diseño profesional** manteniendo la identidad visual del proyecto

### 🧭 **Navegación Mejorada**
- ✅ **Navbar actualizada** con enlaces a todas las nuevas páginas
- ✅ **Footer enriquecido** con enlaces rápidos y información del proyecto
- ✅ **Iconografía consistente** usando Font Awesome en toda la interfaz
- ✅ **Enlaces GitHub** para acceso directo al repositorio del proyecto
- ✅ **Breadcrumbs implícitos** en la estructura de navegación

### 🎨 **Mejoras de UI/UX**
- ✅ **Diseño coherente** en todas las páginas siguiendo el mismo patrón visual
- ✅ **Responsive design** optimizado para móviles, tablets y desktop
- ✅ **Paleta de colores robótica** con azules, grises y acentos tecnológicos
- ✅ **Efectos hover** y transiciones suaves en botones y cards
- ✅ **Typography mejorada** con jerarquía clara y legibilidad optimizada

### 🎨 **Interfaz Moderna con Bootstrap 5**
- ✅ **Template base responsivo** con navegación profesional
- ✅ **Cards interactivas** con efectos hover y animaciones suaves
- ✅ **Sistema de iconos** completo con Font Awesome 6.0.0
- ✅ **Diseño centrado** en la experiencia del usuario (UX/UI)
- ✅ **Paleta de colores** temática profesional de robótica
- ✅ **Gradientes modernos** y efectos visuales atractivos

### 📸 **Sistema de Imágenes Avanzado**
- ✅ **Imágenes principales** para noticias con redimensionado automático
- ✅ **Galería de imágenes** adicionales por noticia
- ✅ **Imágenes de perfil** para autores con biografías
- ✅ **Manejo automático** de archivos con Pillow
- ✅ **Imágenes predeterminadas** cuando no se cargan
- ✅ **Optimización** de tamaños y formatos

### 💬 **Sistema de Comentarios Completo**
- ✅ **Comentarios vinculados** a noticias específicas
- ✅ **Moderación de comentarios** (activo/inactivo)
- ✅ **Interfaz elegante** para mostrar comentarios
- ✅ **Contador de comentarios** por noticia
- ✅ **Validación de datos** y sanitización
- ✅ **Timestamps** automáticos

### 🔍 **Búsqueda y Filtrado Avanzado**
- ✅ **Búsqueda por texto** en título, subtítulo y contenido
- ✅ **Filtrado por categorías** con dropdown interactivo
- ✅ **Ordenamiento múltiple**: Por fecha (ASC/DESC) y alfabético (A-Z/Z-A)
- ✅ **Paginación avanzada** (6 noticias por página) con conservación de filtros
- ✅ **Indicadores visuales** de filtros activos con resumen inteligente
- ✅ **Función para limpiar** filtros rápidamente
- ✅ **URLs amigables** para SEO y compartir resultados
- ✅ **Interfaz intuitiva** con formularios bien organizados

### 📊 **Métricas y Analytics**
- ✅ **Contador de visualizaciones** por noticia
- ✅ **Fecha de creación** y actualización automática
- ✅ **Estado de publicación** (activa/inactiva)
- ✅ **Metadatos enriquecidos** para mejor organización
- ✅ **Estadísticas de contenido** en tiempo real

### 🎯 **Especialización en Robótica**
- ✅ **Robótica Avanzada**: Robots inteligentes y sistemas de control
- ✅ **Robótica Industrial**: Automatización y manufactura
- ✅ **Robótica del Futuro**: Tendencias e investigación avanzada

---

## 🛠️ Stack Tecnológico

### **Backend**
- **Django 5.2.4** - Framework web de Python
- **SQLite** - Base de datos integrada
- **Pillow 11.3.0** - Procesamiento de imágenes

### **Frontend**
- **Bootstrap 5.1.3** - Framework CSS responsive
- **Font Awesome 6.0.0** - Iconografía moderna
- **Google Fonts (Roboto)** - Tipografía profesional
- **HTML5 & CSS3** - Markup semántico y estilos

### **Desarrollo**
- **Python 3.12** - Lenguaje de programación
- **Virtual Environment** - Aislamiento de dependencias
- **Git** - Control de versiones

---

## 📁 Estructura del Proyecto

```
Proyecto-Final-Grupo-N-4/
├── 📁 apps/
│   └── 📁 noticias/              # App principal de noticias
│       ├── 📄 models.py          # Modelos mejorados con imágenes
│       ├── 📄 views.py           # Vistas con búsqueda y paginación
│       ├── 📄 admin.py           # Panel admin personalizado
│       ├── 📄 urls.py            # URLs organizadas
│       └── 📁 migrations/        # Migraciones de base de datos
├── 📁 grupo4/
│   ├── 📁 settings/              # Configuraciones por ambiente
│   │   ├── 📄 base.py            # Configuración base
│   │   ├── 📄 local.py           # Desarrollo local
│   │   └── 📄 production.py      # Producción
│   ├── 📄 urls.py                # URLs principales
│   └── 📄 views.py               # Vista de inicio
├── 📁 templates/                 # Templates limpios y optimizados
│   ├── 📄 base.html              # Template base responsivo
│   ├── 📄 index.html             # Página de inicio moderna
│   ├── 📄 acerca_de.html         # ✨ NUEVA: Página sobre el equipo
│   ├── 📄 contacto.html          # ✨ NUEVA: Página de contacto
│   └── 📁 noticias/              # Templates de noticias
│       ├── 📄 todas_noticias.html   # ✨ MEJORADA: Con filtros avanzados
│       ├── 📄 una_noticia.html      # ✨ NUEVA: Detalle completo
│       ├── 📄 nueva_noticia.html
│       ├── 📄 actualizar_noticia.html
│       └── 📄 eliminar_noticia.html
├── 📁 media/                     # Archivos multimedia
│   ├── 📁 noticias/              # Imágenes de noticias
│   └── 📁 autores/               # Imágenes de autores
├── 📁 static/                    # Archivos estáticos
├── 📄 requirements.txt           # Dependencias del proyecto
├── 📄 manage.py                  # Gestor de comandos Django
└── 📄 README.md                  # Documentación del proyecto
```

---

## ⚙️ Instalación y Configuración

### **1. Prerrequisitos**
```bash
Python 3.12+
Git
```

### **2. Clonar el Repositorio**
```bash
git clone https://github.com/JDGA1997/Proyecto-Final-Grupo-N-4.git
cd Proyecto-Final-Grupo-N-4
```

### **3. Crear Entorno Virtual**
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

### **4. Instalar Dependencias**
```bash
pip install -r requirements.txt
```

### **5. Configurar Base de Datos**
```bash
python manage.py makemigrations
python manage.py migrate
```

### **6. Crear Superusuario (Opcional)**
```bash
python manage.py createsuperuser
```

### **7. Ejecutar Servidor de Desarrollo**
```bash
python manage.py runserver
```

### **8. Acceder a la Aplicación**
- **Portal Principal**: http://127.0.0.1:8000/
- **Lista de Noticias**: http://127.0.0.1:8000/noticias/
- **🆕 Acerca de**: http://127.0.0.1:8000/noticias/acerca-de/
- **🆕 Contacto**: http://127.0.0.1:8000/noticias/contacto/
- **Panel de Administración**: http://127.0.0.1:8000/admin/

---

## 🎯 Funcionalidades Principales

### **🏠 Página de Inicio**
- **Hero Section** moderno con gradiente tecnológico
- **Tres áreas especializadas** en robótica claramente definidas
- **Navegación rápida** a las secciones principales
- **Diseño completamente responsive** para todos los dispositivos

### **📰 Gestión de Noticias**
- **CRUD completo**: Crear, leer, actualizar y eliminar noticias
- **Editor de contenido** con validación de campos
- **Categorización** por temas específicos de robótica
- **Sistema de imágenes** integrado con galería
- **🆕 Vista de detalle completa** con comentarios y compartir

### **🔍 Búsqueda y Filtrado Inteligente**
- **Búsqueda por texto** en título, subtítulo y contenido
- **Filtrado por categoría** con menú desplegable
- **🆕 Ordenamiento avanzado**: Por fecha (ASC/DESC) y alfabético (A-Z/Z-A)
- **Paginación inteligente** de resultados con preservación de filtros
- **URLs amigables** optimizadas para SEO

### **💬 Sistema de Comentarios**
- **Comentarios por noticia** con sistema de moderación
- **Interfaz intuitiva** para usuarios
- **Validación robusta** de datos de entrada
- **Timestamps automáticos** para seguimiento

### **� Páginas Institucionales**
- **Página "Acerca de"**: Información completa del equipo y proyecto
- **Página "Contacto"**: Formulario profesional con validación
- **FAQ integrado** con preguntas frecuentes
- **Información del equipo** con perfiles individuales

### **�🎨 Panel de Administración**
- **Interfaz personalizada** del admin de Django
- **Gestión inline** de imágenes y comentarios
- **Filtros avanzados** en los listados

---

## 🌐 Navegación y Páginas

### **Rutas Principales Disponibles**

| Ruta | Descripción | Funcionalidad |
|:-----|:------------|:--------------|
| `/` | Página de inicio | Hero section y navegación rápida |
| `/noticias/` | Lista de noticias | Búsqueda, filtros y ordenamiento |
| `/noticias/<id>/` | 🆕 Detalle de noticia | Vista completa con comentarios |
| `/noticias/crear/` | Crear noticia | Formulario de creación (autenticado) |
| `/noticias/actualizar/<id>/` | Editar noticia | Formulario de edición (autenticado) |
| `/noticias/eliminar/<id>/` | Eliminar noticia | Confirmación de eliminación |
| `/noticias/acerca-de/` | 🆕 Acerca de | Información del equipo y proyecto |
| `/noticias/contacto/` | 🆕 Contacto | Formulario de contacto y FAQ |
| `/admin/` | Panel administrativo | Gestión completa del contenido |

### **🆕 Características de Navegación**
- **Navbar responsiva** con colapso en móviles
- **Enlaces activos** con indicadores visuales
- **Breadcrumbs implícitos** en la estructura
- **Footer enriquecido** con enlaces rápidos
- **Iconografía consistente** en toda la interfaz

---

## 📱 Diseño Responsive

### **Breakpoints y Adaptaciones**

| Dispositivo | Resolución | Características |
|:------------|:-----------|:----------------|
| **📱 Móvil** | < 576px | Navegación colapsable, cards apiladas |
| **📟 Tablet** | 576px - 992px | Layout de 2 columnas, menú adaptativo |
| **💻 Desktop** | > 992px | Layout completo de 3 columnas |
| **🖥️ Wide Screen** | > 1200px | Máximo aprovechamiento del espacio |

### **Optimizaciones Móviles**
- **Navegación touch-friendly** con botones grandes
- **Imágenes optimizadas** para diferentes densidades
- **Texto legible** en pantallas pequeñas
- **Carga rápida** con assets optimizados
- **🆕 Formularios responsivos** en páginas de contacto
- **🆕 Cards adaptativas** en listados de noticias
- **🆕 Sidebar colapsable** en vista de detalle

---

## 🔧 Configuración Adicional

### **🆕 Nuevas Configuraciones de URLs**
```python
# apps/noticias/urls.py - Rutas actualizadas
urlpatterns = [
    path('', todas_las_noticias, name="todas_las_noticias"),
    path('<int:noticia_id>/', una_noticia, name='una_noticia'),  # ✨ NUEVA
    path('crear/', crear_noticia, name='crear_noticia'),
    path('actualizar/<int:noticia_id>/', actualizar_noticia, name='actualizar_noticia'),
    path('eliminar/<int:noticia_id>/', eliminar_noticia, name='eliminar_noticia'),
    path('acerca-de/', acerca_de, name='acerca_de'),             # ✨ NUEVA
    path('contacto/', contacto, name='contacto'),                # ✨ NUEVA
]
```

### **🆕 Vistas Mejoradas con Ordenamiento**
```python
# views.py - Lógica de ordenamiento implementada
def todas_las_noticias(request):
    # Parámetros de filtrado
    categoria_param = request.GET.get("categoria", "").strip()
    busqueda = request.GET.get("busqueda", "").strip()
    ordenamiento = request.GET.get("orden", "").strip()  # ✨ NUEVO
    
    # Lógica de ordenamiento avanzado
    if ordenamiento == "fecha_asc":
        noticias = noticias.order_by('fecha')
    elif ordenamiento == "fecha_desc":
        noticias = noticias.order_by('-fecha')
    elif ordenamiento == "alfabetico_asc":
        noticias = noticias.order_by('titulo')
    elif ordenamiento == "alfabetico_desc":
        noticias = noticias.order_by('-titulo')
```

### **Archivos Media**
```python
# settings/base.py
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

### **Archivos Estáticos**
```python
# settings/base.py
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
```

### **Configuración Regional**
```python
# settings/base.py
LANGUAGE_CODE = 'es-ar'
TIME_ZONE = 'America/Argentina/Buenos_Aires'
USE_I18N = True
USE_L10N = True
USE_TZ = True
```

### **Configuración de Seguridad**
```python
# settings/base.py
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
```


---

<div align="center">

### 🤖 **Portal de Noticias sobre Robótica**

*Desarrollado con ❤️ por el Grupo N°4 - Informatorio 2025*

[![Made with Django](https://img.shields.io/badge/Made%20with-Django-092E20?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![Powered by Bootstrap](https://img.shields.io/badge/Powered%20by-Bootstrap-7952B3?style=flat-square&logo=bootstrap)](https://getbootstrap.com/)
[![Built with Python](https://img.shields.io/badge/Built%20with-Python-3776AB?style=flat-square&logo=python)](https://www.python.org/)

---



**© 2025 - Informatorio Chaco | Proyecto Final de Desarrollo Web con Django**

*"Construyendo el futuro de la información robótica, una línea de código a la vez"*

</div>
