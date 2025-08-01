<div align="center">
  <img src="https://github.com/user-attachments/assets/df02cfe1-dd25-41d8-9cc3-2cea31e60d1a" alt="Logo del Proyecto" width="400"/>

# 🤖 Portal de Noticias sobre Robótica
## Etapa 2: Desarrollo Web - Grupo N°4

[![Django](https://img.shields.io/badge/Django-5.2.4-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://html.spec.whatwg.org/)

</div>

## 📋 Descripción del Proyecto

Este proyecto es un **portal web de noticias especializado en robótica** desarrollado como proyecto final del curso de Desarrollo Web - Etapa 2. La aplicación se centra exclusivamente en la gestión de noticias sobre robótica con un sistema completo de comentarios, implementando manejo de usuarios con roles y permisos específicos para garantizar el correcto funcionamiento del portal.

### 🎯 Objetivos del Proyecto

- Crear un portal de noticias sobre robótica funcional con página principal
- Implementar un CRUD (Create, Read, Update, Delete) completo para noticias sobre robótica
- Desarrollar un sistema integral de comentarios para las noticias sobre robótica
- Implementar gestión de usuarios con roles y permisos diferenciados
- Aplicar conceptos de programación orientada a objetos y bases de datos relacionales
- Desarrollar vistas basadas en clases (CBV) **Ó** funciones (FBV) para una arquitectura moderna (SOLO UNA SOLA)
- Crear un sistema de categorización y filtrado de contenido de noticias sobre robótica

## ✨ Características Principales

### 📰 Gestión de Noticias sobre Robótica
- **Página principal** con listado completo de todas las noticias sobre robótica
- **Visualización** organizada y navegable de noticias sobre robótica
- **Filtrado** por categorías para una mejor organización del contenido robótico
- **Detalle completo** de cada noticia sobre robótica con autor y fecha de publicación
- **CRUD completo**: Crear, editar y eliminar noticias sobre robótica según permisos de usuario
- **Sistema de categorías** para clasificar y organizar el contenido sobre robótica

### 💬 Sistema Completo de Comentarios
- **Comentarios** asociados a cada noticia sobre robótica para fomentar la interacción
- **Moderación** de comentarios según roles de usuario
- **Respuestas** a comentarios para crear hilos de discusión sobre temas de robótica
- **Gestión** completa de comentarios por usuarios registrados
- **Control de acceso** según permisos establecidos

### 👥 Sistema de Usuarios con Roles y Permisos
- **Registro e inicio de sesión** seguro de usuarios
- **Roles diferenciados**: Administrador, Editor, Usuario registrado
- **Permisos específicos** por rol para controlar acceso a funcionalidades
- **Gestión de perfiles** de usuario
- **Control de acceso** robusto para garantizar seguridad
- **Sistema de autenticación** completo

### 🏷️ Sistema de Categorías y Autores
- **Gestión de autores** especializados en robótica con información detallada
- **Categorías organizadas** para clasificar noticias sobre robótica
- **Relaciones** estructuradas entre contenido robótico y responsables

## 🏗️ Arquitectura del Proyecto

### 📁 Estructura de Directorios
```
Proyecto-Final-Grupo-N-4/
├── apps/
│   ├── noticias/          # App para gestión de noticias sobre robótica
│   │   ├── models.py      # Modelos: Noticia, Autor, Categoria, Comentario
│   │   ├── views.py       # Vistas CBV **Ó** FBV
│   │   ├── urls.py        # URLs de la app
│   │   ├── forms.py       # Formularios personalizados
│   │   └── admin.py       # Configuración del admin
│   └── usuarios/          # App para gestión de usuarios
│       ├── models.py      # Modelos: PerfilUsuario
│       ├── views.py       # Vistas CBV **Ó** FBV de autenticación
│       ├── forms.py       # Formularios de registro/login
│       └── urls.py        # URLs de autenticación
├── comsiete/              # Configuración principal del proyecto
│   ├── settings/          # Configuraciones separadas
│   │   ├── base.py        # Configuración base
│   │   ├── local.py       # Desarrollo local
│   │   └── production.py  # Producción
│   ├── urls.py            # URLs principales
│   └── views.py           # Vista principal
├── templates/             # Templates HTML
│   ├── noticias/          # Templates de noticias sobre robótica y página principal
│   ├── comentarios/       # Templates de comentarios
│   └── usuarios/          # Templates de autenticación
├── static/                # Archivos estáticos (CSS, JS, imágenes)
├── requirements.txt       # Dependencias del proyecto
└── manage.py             # Comando de gestión de Django
```

### 🗄️ Modelos de Base de Datos

#### Noticias sobre Robótica
- **Noticia**: Título, subtítulo, contenido sobre robótica, fecha, autor, categorías, imagen
- **Autor**: Nombre, nacionalidad, biografía, especialización en robótica
- **Categoria**: Nombre, descripción (ej: IA, Automatización, Robots Industriales)
- **Comentario**: Contenido, fecha, usuario, noticia, comentario padre (para respuestas)

#### Usuarios y Autenticación
- **Usuario**: Utiliza el modelo User de Django
- **PerfilUsuario**: Información adicional del usuario (avatar, biografía, etc.)
- **Rol**: Diferentes niveles de permisos (Administrador, Editor, Usuario)

### 🔗 Relaciones de Base de Datos
- **Uno a Muchos**: Autor → Noticias, Usuario → Comentarios, Noticia → Comentarios
- **Muchos a Muchos**: Noticias ↔ Categorías
- **Jerárquica**: Comentario → Comentario (para respuestas)
- **Uno a Uno**: Usuario ↔ PerfilUsuario

## 🚀 Instalación y Configuración

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Paso a paso

1. **Clonar el repositorio**
```bash
git clone https://github.com/JDGA1997/Proyecto-Final-Grupo-N-4.git
cd Proyecto-Final-Grupo-N-4
```

2. **Crear entorno virtual**
```bash
python -m venv venv
venv\Scripts\activate  # En Windows
# source venv/bin/activate  # En Linux/Mac
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Configurar base de datos**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Crear superusuario (opcional)**
```bash
python manage.py createsuperuser
```

6. **Ejecutar servidor de desarrollo**
```bash
python manage.py runserver
```

7. **Acceder a la aplicación**
- Página principal del portal: http://127.0.0.1:8000/
- Gestión de noticias: http://127.0.0.1:8000/noticias/
- Registro/Login: http://127.0.0.1:8000/usuarios/
- Admin: http://127.0.0.1:8000/admin/

## 🛠️ Tecnologías Utilizadas

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| **Django** | 5.2.4 | Framework web principal |
| **Python** | 3.x | Lenguaje de programación |
| **SQLite** | - | Base de datos |
| **HTML5** | - | Estructura de páginas |
| **CSS3** | - | Estilos (básicos) |

## 📱 Funcionalidades por Módulo

### 🏠 Página Principal
- **Listado completo** de todas las noticias sobre robótica disponibles
- **Navegación intuitiva** y organizada por temas robóticos
- **Acceso directo** a detalles de cada noticia sobre robótica
- **Filtros básicos** para mejorar la experiencia de usuario en contenido robótico

### 📰 Módulo Noticias sobre Robótica (CBV) **Ó** (FBV)

#### Vistas Disponibles
- **Lista de noticias** (`/noticias/`) - Página principal del portal de robótica
- **Detalle de noticia** (`/noticias/<id>/`) - Vista completa de cada noticia sobre robótica
- **Crear noticia** (`/noticias/crear/`) - Solo usuarios con permisos de editor/admin
- **Editar noticia** (`/noticias/editar/<id>/`) - Solo autor o administrador
- **Eliminar noticia** (`/noticias/eliminar/<id>/`) - Solo autor o administrador

#### Características Específicas
- Filtrado por categorías robóticas mediante parámetros GET
- Sistema de paginación para manejo de grandes volúmenes de noticias
- Búsqueda y organización del contenido robótico
- Control de acceso según roles de usuario

### 💬 Sistema de Comentarios

#### Funcionalidades Completas
- **Agregar comentarios** a cualquier noticia sobre robótica (usuarios registrados)
- **Responder comentarios** para crear discusiones estructuradas sobre robótica
- **Moderar comentarios** según roles de administrador
- **Eliminar comentarios** con permisos apropiados
- **Gestión completa** del sistema de comentarios en noticias robóticas

### 👥 Módulo Usuarios y Permisos

#### Gestión de Autenticación
- **Registro de usuario** (`/usuarios/registro/`)
- **Inicio de sesión** (`/usuarios/login/`)
- **Cierre de sesión** (`/usuarios/logout/`)
- **Gestión de perfil** (`/usuarios/perfil/`)

#### Control de Acceso y Roles
- **Administrador**: Control total del portal y moderación
- **Editor**: Creación y edición de noticias, moderación de comentarios  
- **Usuario registrado**: Comentarios y gestión de perfil personal
- **Usuario anónimo**: Solo lectura de noticias sobre robótica (sin comentarios)

## 🔧 Configuración de Desarrollo

### Configuraciones Separadas
El proyecto utiliza configuraciones separadas para diferentes entornos:

- **`base.py`**: Configuración común
- **`local.py`**: Desarrollo local (DEBUG=True, SQLite)
- **`production.py`**: Producción (DEBUG=False)

### Variables de Entorno
Por defecto, el proyecto usa `comsiete.settings.local` para desarrollo.

## 🧪 Testing

El proyecto incluye estructura básica para testing en cada app:
```bash
python manage.py test apps.noticias
python manage.py test apps.usuarios
```

## 👩‍💻👨‍💻 Nuestro Equipo

Este proyecto fue posible gracias al trabajo colaborativo de nuestro equipo:

| Nombre y Apellido | Usuario en GitHub | Perfil de GitHub |
| ----------------- | ----------------- | ---------------- |
| Aldo Andrés Acosta | `Andres777777` | [![GitHub Badge](https://img.shields.io/badge/GitHub-121011?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Andres777777) |
| Juan Diego González Antoniazzi | `JDGA1997` | [![GitHub Badge](https://img.shields.io/badge/GitHub-121011?style=for-the-badge&logo=github&logoColor=white)](https://github.com/JDGA1997) |

## 🤝 Contribuciones

Este proyecto es parte del curso de Programación - Etapa 2 del **Informatorio**. Las contribuciones están limitadas a los miembros del equipo durante el período académico.

## 📄 Licencia

Este proyecto es desarrollado con fines educativos como parte del programa Informatorio.

## 🏆 Logros Académicos

- ✅ Portal de noticias sobre robótica funcional con página principal completa
- ✅ Sistema integral de comentarios asociado a noticias sobre robótica
- ✅ Gestión completa de usuarios con roles y permisos diferenciados
- ✅ Implementación de CRUD completo para noticias sobre robótica
- ✅ Uso exclusivo de vistas basadas en clases (CBV) **Ó** funciones (FBV)
- ✅ Control de acceso y seguridad según roles de usuario
- ✅ Uso de Django ORM y relaciones de base de datos
- ✅ Sistema de filtrado y organización de contenido robótico
- ✅ Arquitectura modular enfocada en el portal de noticias sobre robótica

---

<div align="center">

### ⭐ Si este proyecto te fue útil, ¡no olvides darle una estrella!

**Desarrollado con ❤️ por el Grupo N°4 - Informatorio 2025**

[![Informatorio](https://img.shields.io/badge/Informatorio-2025-blue?style=for-the-badge)](https://www.informatorio.org/)

</div>
