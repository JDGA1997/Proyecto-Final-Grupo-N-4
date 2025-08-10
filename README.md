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
- [✨ Mejoras Implementadas](#-mejoras-implementadas)
- [🛠️ Stack Tecnológico](#️-stack-tecnológico)
- [📁 Estructura del Proyecto](#-estructura-del-proyecto)
- [⚙️ Instalación y Configuración](#️-instalación-y-configuración)
- [🎯 Funcionalidades](#-funcionalidades)
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
| **🔍 Búsqueda** | Filtrado avanzado y paginación | ✅ |
| **💬 Comentarios** | Sistema completo de comentarios | ✅ |
| **⚡ Performance** | Optimizado para velocidad | ✅ |
| **🛡️ Seguridad** | CSRF protection y validaciones | ✅ |

---

## ✨ Mejoras Implementadas

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
- ✅ **Paginación avanzada** (6 noticias por página)
- ✅ **Indicadores visuales** de filtros activos
- ✅ **Función para limpiar** filtros rápidamente
- ✅ **URLs amigables** para SEO

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
│   └── 📁 noticias/              # Templates de noticias
│       ├── 📄 todas_noticias.html
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
- **Panel de Administración**: http://127.0.0.1:8000/admin/

---

## 🎯 Funcionalidades

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

### **🔍 Búsqueda y Filtrado**
- **Búsqueda por texto** en título, subtítulo y contenido
- **Filtrado por categoría** con menú desplegable
- **Paginación inteligente** de resultados
- **URLs amigables** optimizadas para SEO

### **💬 Sistema de Comentarios**
- **Comentarios por noticia** con sistema de moderación
- **Interfaz intuitiva** para usuarios
- **Validación robusta** de datos de entrada
- **Timestamps automáticos** para seguimiento

### **🎨 Panel de Administración**
- **Interfaz personalizada** del admin de Django
- **Gestión inline** de imágenes y comentarios
- **Filtros avanzados** en los listados
- **Branding específico** del Grupo N°4

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

---

## 🔧 Configuración Adicional

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
