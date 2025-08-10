<div align="center">
  <img src="https://github.com/user-attachments/assets/df02cfe1-dd25-41d8-9cc3-2cea31e60d1a" alt="Logo del Proyecto" width="400"/>

# 🤖 Blog de Robótica
## Proyecto Final - Desarrollo Web con Django - Grupo N°4

[![Django](http#### Características Implementadas
- ✅ Filtrado por categorías mediante parámetros GET (`?categoria=nombre`)
- ✅ **Implementación con FBV**: Proyecto estandarizado usando únicamente Vistas Basadas en Funciones
- ✅ Templates dedicados para cada operación CRUD
- ✅ Redirecciones automáticas tras operaciones exitosas

#### Características Pendientes (Según Consigna)
- 🔲 Filtrado por antigüedad (ascendente y descendente)
- 🔲 Filtrado por orden alfabético (ascendente y descendente)
- 🔲 Control de permisos según tipo de usuario
- 🔲 Subida de imágenes asociadas a artículoselds.io/badge/Django-5.2.4-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://html.spec.whatwg.org/)
[![Estado](https://img.shields.io/badge/Estado-En_Desarrollo-yellow?style=for-the-badge)]()

</div>

## 📋 Descripción del Proyecto

Este proyecto es un **blog especializado en robótica** desarrollado como proyecto final del curso de Desarrollo Web del **Informatorio**. La aplicación implementa un sistema completo de gestión de artículos y comentarios sobre robótica, siguiendo las especificaciones académicas establecidas para la evaluación final.

### 🎯 Objetivo Principal

Crear una aplicación web tipo BLOG utilizando el framework Django, aplicando los conocimientos adquiridos durante el curso y cumpliendo con todos los requisitos técnicos y funcionales especificados en la consigna académica.

### 📋 Requisitos del Proyecto Final (Consigna)

#### 👥 Sistema de Perfiles (Requerido)
- **Visitante**: Navegar, filtrar publicaciones, leer artículos, registrarse y loguearse
- **Miembro/Usuario Registrado**: Comentar artículos, editar/eliminar sus propios comentarios, desloguearse
- **Colaborador**: Cargar, editar y eliminar artículos y fotos; categorizar artículos; moderar comentarios
- **Super Admin**: Control total del sistema vía Django Admin

#### 🏗️ Secciones Requeridas del Blog
- **Inicio/Portada**: Publicaciones más recientes o destacadas
- **Categorías**: Contenido dividido por categorías temáticas sobre robótica  
- **Acerca de**: Información sobre el blog y el equipo
- **Contacto**: Formulario de contacto y enlaces de comunicación

#### ⚙️ Funcionalidades Obligatorias
- **CRUD Artículos**: Crear, Leer, Editar y Eliminar artículos
- **CRUD Comentarios**: Crear, Leer, Editar y Eliminar comentarios
- **Filtros de Publicaciones**:
  - Por categoría
  - Por antigüedad (ascendente y descendente)
  - Por orden alfabético (ascendente y descendente)
- **Sistema de Autenticación**: Registro, login y logout de usuarios

## ✨ Estado Actual de Implementación

### ✅ Funcionalidades Implementadas
- **Modelos de datos**: Noticia, Autor, Categoria con relaciones apropiadas
- **CRUD completo para artículos**: Crear, leer, editar y eliminar noticias usando FBV (Vistas Basadas en Funciones)
- **Sistema de categorías**: Clasificación y filtrado por categorías
- **Panel de administración**: Gestión completa via Django Admin
- **Templates HTML**: Estructura básica para todas las operaciones CRUD
- **Configuración multi-entorno**: Settings separados (base, local, production)

### 🚧 Funcionalidades Pendientes (Según Consigna)
- **Sistema de perfiles diferenciados**: Visitante, Miembro, Colaborador
- **Sistema de autenticación**: Registro, login, logout de usuarios
- **CRUD de comentarios**: Creación, edición y eliminación de comentarios por usuarios
- **Secciones del blog**: Acerca de, Contacto
- **Filtros avanzados**: Por antigüedad y orden alfabético
- **Control de permisos**: Restricciones según tipo de usuario
- **Sistema de comentarios**: Asociación de comentarios a artículos
- **Página de inicio optimizada**: Publicaciones destacadas/recientes

### 📰 Gestión de Artículos (Implementado)
- **Página principal** con listado de artículos sobre robótica
- **Visualización** organizada y navegable
- **Filtrado básico** por categorías mediante parámetros GET
- **Detalle completo** de cada artículo con autor y fecha de publicación
- **CRUD funcional**: Crear, editar y eliminar artículos usando FBV (Vistas Basadas en Funciones)
- **Arquitectura consistente**: Implementación completamente basada en FBV para simplicidad y claridad

### 🏷️ Sistema de Categorías (Implementado)
- **Gestión de autores** con información básica (nombre, nacionalidad)
- **Categorías organizadas** para clasificar contenido sobre robótica
- **Relaciones estructuradas**: Autor → Artículos (1:N), Artículos ↔ Categorías (M:N)

## 🏗️ Arquitectura del Proyecto

### 📁 Estructura de Directorios (Actual)
```
Proyecto-Final-Grupo-N-4/
├── apps/
│   └── noticias/          # App principal para artículos del blog
│       ├── models.py      # Modelos: Noticia, Autor, Categoria
│       ├── views.py       # Vistas FBV (Vistas Basadas en Funciones)
│       ├── urls.py        # URLs de la app
│       ├── admin.py       # Configuración del admin de Django
│       └── migrations/    # Migraciones de base de datos
├── comsiete/              # Configuración principal del proyecto
│   ├── settings/          # Configuraciones separadas por entorno
│   │   ├── base.py        # Configuración base común
│   │   ├── local.py       # Desarrollo local (SQLite, DEBUG=True)
│   │   └── production.py  # Producción (para PythonAnywhere)
│   ├── urls.py            # URLs principales del proyecto
│   └── views.py           # Vista de página de inicio
├── templates/             # Templates HTML del blog
│   ├── index.html         # Página principal del blog
│   └── noticias/          # Templates para artículos
│       ├── todas_noticias.html    # Lista de artículos
│       ├── una_noticia.html       # Detalle de artículo
│       ├── nueva_noticia.html     # Crear artículo
│       ├── actualizar_noticia.html # Editar artículo
│       └── eliminar_noticia.html  # Confirmar eliminación
├── static/                # Archivos estáticos (CSS, JS, imágenes)
├── requirements.txt       # Dependencias del proyecto
└── manage.py             # Utilidad de gestión de Django
```

### 📋 Estructura Prevista (Según Consigna)
```
# Apps adicionales por implementar:
├── apps/
│   ├── noticias/          # ✅ Implementado - Artículos del blog
│   ├── usuarios/          # 🔲 Pendiente - Perfiles y autenticación
│   ├── comentarios/       # 🔲 Pendiente - Sistema de comentarios
│   └── paginas/           # 🔲 Pendiente - Acerca de, Contacto
```

### 🗄️ Modelos de Base de Datos

#### Implementados Actualmente
- **Noticia** (Artículo del Blog):
  - `titulo`: CharField(max_length=85)
  - `subtitulo`: CharField(max_length=150)  
  - `contenido`: TextField()
  - `fecha`: DateField(auto_now_add=True)
  - `autor`: ForeignKey(Autor) - Relación 1:N
  - `categorias`: ManyToManyField(Categoria) - Relación M:N

- **Autor**:
  - `nombre`: CharField(max_length=50)
  - `nacionalidad`: CharField(max_length=20)

- **Categoria**:
  - `nombre`: CharField(max_length=50)
  - `descripcion`: TextField()

#### Modelos Pendientes (Según Consigna)
- **Usuario Personalizado/Perfil**: Para gestión de perfiles diferenciados
- **Comentario**: Para sistema de comentarios en artículos
- **Contacto**: Para formulario de contacto del blog

### 🔗 Relaciones Implementadas
- **Autor → Noticias**: Relación uno a muchos (1:N)
- **Noticias ↔ Categorías**: Relación muchos a muchos (M:N)

### 🔗 Relaciones Pendientes
- **Usuario → Comentarios**: Relación uno a muchos (1:N)
- **Noticia → Comentarios**: Relación uno a muchos (1:N)
- **Usuario → Perfil**: Relación uno a uno (1:1) extendiendo User de Django

## 🚀 Instalación y Configuración

### Prerrequisitos
- Python 3.12 o superior
- pip (gestor de paquetes de Python)
- Git (para clonar el repositorio)

### Instalación Local

1. **Clonar el repositorio**
```bash
git clone https://github.com/JDGA1997/Proyecto-Final-Grupo-N-4.git
cd Proyecto-Final-Grupo-N-4
```

2. **Activar entorno virtual** (ya incluido en el proyecto)
```bash
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# Windows CMD  
.\.venv\Scripts\activate.bat

# Git Bash (Windows)
source .venv/Scripts/activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Aplicar migraciones**
```bash
python manage.py migrate
```

5. **Crear superusuario** (opcional, para Django Admin)
```bash
python manage.py createsuperuser
```

6. **Ejecutar servidor de desarrollo**
```bash
python manage.py runserver
```
   *Alternativamente, usar la tarea de VS Code: "Ejecutar Servidor Django"*

7. **Acceder al blog**
- **Página principal**: http://127.0.0.1:8000/
- **Lista de artículos**: http://127.0.0.1:8000/noticias/
- **Django Admin**: http://127.0.0.1:8000/admin/ (requiere superusuario)

### 🌐 Despliegue en Producción

**Fecha límite de entrega**: 17 de Agosto  
**Plataforma requerida**: [PythonAnywhere](https://www.pythonanywhere.com/) (gratuito)

El proyecto incluye configuración específica para producción en `comsiete/settings/production.py`

## 🛠️ Tecnologías Utilizadas

| Tecnología | Versión | Propósito | Estado |
|------------|---------|-----------|---------|
| **Django** | 5.2.4 | Framework web principal | ✅ Implementado |
| **Python** | 3.12.10 | Lenguaje de programación | ✅ Implementado |
| **SQLite** | - | Base de datos (desarrollo) | ✅ Configurado |
| **HTML5** | - | Estructura del blog | ✅ Templates básicos |
| **CSS3** | - | Estilos del blog | 🔲 Pendiente |
| **JavaScript** | - | Interactividad | 🔲 No implementado |
| **Bootstrap** | - | Framework CSS (recomendado) | 🔲 Pendiente |

### Dependencias del Proyecto
```
asgiref==3.9.1
Django==5.2.4
sqlparse==0.5.3
tzdata==2025.2
```

### Configuración Multi-Entorno
- **`base.py`**: Configuración común para todos los entornos
- **`local.py`**: Desarrollo local (DEBUG=True, SQLite)
- **`production.py`**: Producción para PythonAnywhere (DEBUG=False)

## 📱 Funcionalidades del Blog

### 🏠 Página de Inicio (Implementado)
- **Página principal** básica del blog (`templates/index.html`)
- **Acceso directo** a la sección de artículos
- 🔲 **Pendiente**: Mostrar artículos destacados/recientes según consigna

### 📰 Gestión de Artículos (Implementado)

#### Funcionalidades Actuales
- **Lista de artículos** (`/noticias/`) - Vista principal con filtrado básico por categorías
- **Detalle de artículo** (`/noticias/<id>/`) - Vista completa de cada artículo
- **Crear artículo** (`/noticias/crear/`) - Formulario de creación (FBV)
- **Editar artículo** (`/noticias/actualizar/<id>/`) - Formulario de edición (FBV)
- **Eliminar artículo** (`/noticias/eliminar/<id>/`) - Confirmación de eliminación (FBV)

#### Características Implementadas
- ✅ Filtrado por categorías mediante parámetros GET (`?categoria=nombre`)
- ✅ Implementación con FBV: Todas las vistas usando Vistas Basadas en Funciones
- ✅ Templates dedicados para cada operación CRUD
- ✅ Redirecciones automáticas tras operaciones exitosas

#### Características Pendientes (Según Consigna)
- 🔲 Filtrado por antigüedad (ascendente y descendente)
- 🔲 Filtrado por orden alfabético (ascendente y descendente)
- 🔲 Control de permisos según tipo de usuario
- � Subida de imágenes asociadas a artículos

### 💬 Sistema de Comentarios (Pendiente)
- 🔲 **CRUD de comentarios**: Crear, leer, editar y eliminar comentarios
- 🔲 **Asociación a artículos**: Comentarios vinculados a cada artículo
- 🔲 **Control de permisos**: Solo usuarios registrados pueden comentar
- 🔲 **Moderación**: Colaboradores pueden gestionar comentarios

### 👥 Sistema de Usuarios (Pendiente - Crítico)
- 🔲 **Perfiles diferenciados**: Visitante, Miembro, Colaborador
- 🔲 **Registro de usuarios**: Formulario de registro
- 🔲 **Login/Logout**: Sistema de autenticación
- 🔲 **Control de acceso**: Permisos según tipo de usuario

### 📑 Secciones del Blog (Pendientes)
- 🔲 **Categorías**: Página dedicada para navegar por categorías
- 🔲 **Acerca de**: Información sobre el blog y el equipo
- 🔲 **Contacto**: Formulario de contacto y datos de comunicación

### 🔧 Panel de Administración (Implementado)
- ✅ **Django Admin**: Gestión completa de artículos, autores y categorías
- ✅ **Configuración personalizada**: Campos, filtros y búsqueda
- ✅ **Interfaz administrativa**: Lista para gestión por administradores

## � Checklist de Cumplimiento (Consigna vs. Implementación)

### ✅ Requisitos Cumplidos
- ✅ **Framework Django**: Proyecto desarrollado con Django 5.2.4
- ✅ **Trabajo grupal**: Desarrollado por el Grupo N°4
- ✅ **Temática robótica**: Blog especializado en robótica según asignación
- ✅ **Modelos de datos**: Estructura básica de artículos, autores y categorías
- ✅ **CRUD artículos**: Crear, leer, editar y eliminar artículos usando FBV
- ✅ **Sistema de categorías**: Categorización básica implementada
- ✅ **Filtrado por categoría**: Filtros funcionales por categoría
- ✅ **Admin de Django**: Panel administrativo configurado y funcional
- ✅ **Configuración multi-entorno**: Base, local y production settings
- ✅ **Arquitectura FBV**: Implementación consistente usando Vistas Basadas en Funciones

### 🔲 Requisitos Pendientes (Críticos para Entrega)
- 🔲 **Tres perfiles de usuario**: Visitante, Miembro, Colaborador
- 🔲 **Sistema de autenticación**: Registro, login, logout
- 🔲 **CRUD comentarios**: Sistema completo de comentarios
- 🔲 **Secciones del blog**: Inicio optimizado, Acerca de, Contacto
- 🔲 **Filtros adicionales**: Por antigüedad y orden alfabético
- 🔲 **Control de permisos**: Restricciones según tipo de usuario
- 🔲 **Publicación online**: Despliegue en PythonAnywhere

### ⚠️ Fechas Importantes
- **17 de Agosto**: Fecha límite para URL en PythonAnywhere
- **Video YouTube**: Presentación de máximo 5 minutos
- **Encuesta final**: Evaluación individual del proceso de desarrollo

## 🔄 Próximos Pasos Críticos

### Prioridad Alta (Para Cumplir Consigna)
1. **Crear app `usuarios`** con perfiles diferenciados
2. **Implementar autenticación**: registro, login, logout
3. **Desarrollar sistema de comentarios** con CRUD completo
4. **Crear secciones**: Acerca de y Contacto
5. **Implementar filtros faltantes**: antigüedad y orden alfabético
6. **Configurar control de permisos** por tipo de usuario

### Prioridad Media
7. **Optimizar página de inicio** con artículos destacados
8. **Agregar estilos CSS** para mejorar presentación
9. **Implementar subida de imágenes** en artículos
10. **Desarrollar tests unitarios**

### Para Entrega Final
11. **Configurar PythonAnywhere** y publicar aplicación
12. **Grabar video de presentación** (máx. 5 minutos)
13. **Completar documentación final**

## ⚠️ Arquitectura del Proyecto: FBV (Vistas Basadas en Funciones)

### 📋 Metodología Implementada
El proyecto utiliza **exclusivamente FBV (Function-Based Views)** siguiendo las mejores prácticas de Django para proyectos académicos.

### 🎯 Ventajas de la Implementación FBV
- **Claridad**: Código más explícito y fácil de entender
- **Simplicidad**: Ideal para aprendizaje y comprensión de Django
- **Control directo**: Mayor control sobre el flujo de la vista
- **Debugging**: Más fácil de debuggear y mantener
- **Flexibilidad**: Permite personalización específica sin complejidad adicional

## 🧪 Testing

El proyecto incluye estructura básica para testing:
```bash
python manage.py test apps.noticias
```

**Estado actual**: Tests por implementar - archivo `apps/noticias/tests.py` contiene solo estructura básica.

**Tests recomendados para implementar**:
- Tests de modelos (Noticia, Autor, Categoria)
- Tests de vistas (CRUD de artículos)
- Tests de formularios y validaciones
- Tests de sistema de autenticación (cuando se implemente)
- Tests de permisos por tipo de usuario

## 👩‍💻👨‍💻 Equipo de Desarrollo

**Grupo N°4 - Informatorio 2025**  
**Proyecto Final: Blog de Robótica**

| Nombre y Apellido | Usuario en GitHub | Perfil de GitHub |
| ----------------- | ----------------- | ---------------- |
| *[Completar Nombre]* | `[usuario1]` | [![GitHub Badge](https://img.shields.io/badge/GitHub-121011?style=for-the-badge&logo=github&logoColor=white)](https://github.com/[usuario1]) |
| *[Completar Nombre]* | `[usuario2]` | [![GitHub Badge](https://img.shields.io/badge/GitHub-121011?style=for-the-badge&logo=github&logoColor=white)](https://github.com/[usuario2]) |
| *[Completar Nombre]* | `[usuario3]` | [![GitHub Badge](https://img.shields.io/badge/GitHub-121011?style=for-the-badge&logo=github&logoColor=white)](https://github.com/[usuario3]) |
| *[Completar Nombre]* | `[usuario4]` | [![GitHub Badge](https://img.shields.io/badge/GitHub-121011?style=for-the-badge&logo=github&logoColor=white)](https://github.com/[usuario4]) |
| *[Completar Nombre]* | `[usuario5]` | [![GitHub Badge](https://img.shields.io/badge/GitHub-121011?style=for-the-badge&logo=github&logoColor=white)](https://github.com/[usuario5]) |
| **Aldo Andrés Acosta** | `Andres777777` | [![GitHub Badge](https://img.shields.io/badge/GitHub-121011?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Andres777777) |
| **Juan Diego González Antoniazzi** | `JDGA1997` | [![GitHub Badge](https://img.shields.io/badge/GitHub-121011?style=for-the-badge&logo=github&logoColor=white)](https://github.com/JDGA1997) |

> **Nota**: Completar los datos de los miembros restantes del grupo según corresponda.

### 📋 Responsabilidades del Proyecto
- **Desarrollo Django**: Configuración del framework y estructura del proyecto
- **Gestión de datos**: Modelos, migraciones y admin de Django  
- **Frontend**: Templates HTML y futura implementación de CSS
- **Autenticación**: Sistema de usuarios y permisos (pendiente)
- **Comentarios**: Sistema de comentarios del blog (pendiente)
- **Despliegue**: Configuración para PythonAnywhere (pendiente)

## 🎓 Contexto Académico

### 📚 Informatorio - Desarrollo Web con Django
- **Curso**: Desarrollo Web - Etapa 2
- **Institución**: Informatorio 2025
- **Modalidad**: Proyecto final grupal
- **Temática asignada**: Blog de Robótica

### 📅 Cronograma de Entrega
- **Formación de grupos**: Semanas 10 y 11
- **Desarrollo**: Agosto 2025
- **Fecha límite URL online**: 17 de Agosto
- **Plataforma obligatoria**: [PythonAnywhere](https://www.pythonanywhere.com/) (gratuito)
- **Video presentación**: YouTube (máx. 5 minutos)
- **Encuesta final**: Evaluación individual del proceso

### � Criterios de Evaluación
- ✅ Uso correcto del framework Django
- 🔲 Implementación de los tres perfiles de usuario requeridos
- 🔲 CRUD completo para artículos y comentarios
- 🔲 Sistema de filtrado por categoría, antigüedad y orden alfabético
- 🔲 Secciones obligatorias del blog (Inicio, Categorías, Acerca de, Contacto)
- 🔲 Sistema de autenticación funcional
- 🔲 Aplicación publicada y accesible online

## 📄 Licencia

Este proyecto es desarrollado con fines educativos como parte del programa **Informatorio 2025**.  
Uso académico bajo supervisión de profesores y mentores del curso.

### ⭐ Si este proyecto te resulta útil, ¡dale una estrella en GitHub!

**Desarrollado con ❤️ por el Grupo N°4**

[![Informatorio](https://img.shields.io/badge/Informatorio-2025-blue?style=for-the-badge)](https://www.informatorio.org/)
[![Django](https://img.shields.io/badge/Django-5.2.4-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)

</div>
