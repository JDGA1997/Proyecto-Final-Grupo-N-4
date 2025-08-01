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

Este proyecto es un **portal web de noticias especializado en robótica** desarrollado como proyecto final del curso de Desarrollo Web - Etapa 2. La aplicación permite gestionar noticias y comentarios relacionados con el mundo de la robótica, ofreciendo funcionalidades de visualización, administración de contenido y sistema de usuarios con roles y permisos.

### 🎯 Objetivos del Proyecto

- Crear un sistema web completo para la gestión de noticias sobre robótica
- Implementar un CRUD (Create, Read, Update, Delete) funcional usando Django
- Desarrollar un sistema de comentarios interactivo para las noticias
- Implementar manejo de usuarios, permisos y roles
- Aplicar conceptos de programación orientada a objetos y bases de datos relacionales
- Desarrollar vistas basadas en clases (CBV) **Ó** funciones (FBV) para una arquitectura moderna (SOLO UNA SOLA)
- Crear un sistema de categorización y filtrado de contenido

## ✨ Características Principales

### 📰 Gestión de Noticias
- **Visualización** de todas las noticias del portal
- **Filtrado** por categorías (Tecnología, Investigación, Innovación, etc.)
- **Detalle completo** de cada noticia con autor y fecha
- **CRUD completo**: Crear, editar y eliminar noticias
- **Sistema de categorías** múltiples por noticia

### 💬 Sistema de Comentarios
- **Comentarios** en cada noticia para fomentar la interacción
- **Moderación** de comentarios por parte de los administradores
- **Respuestas** a comentarios para crear discusiones
- **Gestión** de comentarios por usuarios registrados

### 👥 Sistema de Usuarios y Permisos
- **Registro e inicio de sesión** de usuarios
- **Roles diferenciados**: Administrador, Editor, Usuario registrado
- **Permisos específicos** por rol para diferentes acciones
- **Gestión de perfiles** de usuario
- **Sistema de autenticación** robusto

### 🏷️ Sistema de Categorías y Autores
- **Gestión de autores** con información detallada
- **Categorías organizadas** para clasificar noticias
- **Relaciones** entre contenido y responsables

## 🏗️ Arquitectura del Proyecto

### 📁 Estructura de Directorios
```
Proyecto-Final-Grupo-N-4/
├── apps/
│   ├── noticias/          # App para gestión de noticias
│   │   ├── models.py      # Modelos: Noticia, Autor, Categoria, Comentario
│   │   ├── views.py       # Vistas CBV
│   │   ├── urls.py        # URLs de la app
│   │   ├── forms.py       # Formularios personalizados
│   │   └── admin.py       # Configuración del admin
│   └── usuarios/          # App para gestión de usuarios
│       ├── models.py      # Modelos: PerfilUsuario
│       ├── views.py       # Vistas CBV de autenticación
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
│   ├── noticias/          # Templates de noticias
│   ├── comentarios/       # Templates de comentarios
│   └── usuarios/          # Templates de autenticación
├── static/                # Archivos estáticos (CSS, JS, imágenes)
├── requirements.txt       # Dependencias del proyecto
└── manage.py             # Comando de gestión de Django
```

### 🗄️ Modelos de Base de Datos

#### Noticias
- **Noticia**: Título, subtítulo, contenido, fecha, autor, categorías, imagen
- **Autor**: Nombre, nacionalidad, biografía
- **Categoria**: Nombre, descripción
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
- Portal principal: http://127.0.0.1:8000/
- Noticias: http://127.0.0.1:8000/noticias/
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

### 📰 Módulo Noticias

#### Vistas Disponibles (CBV)
- **Lista de noticias** (`/noticias/`)
- **Detalle de noticia** (`/noticias/<id>/`)
- **Crear noticia** (`/noticias/crear/`) - Solo usuarios autenticados con permisos
- **Editar noticia** (`/noticias/editar/<id>/`) - Solo autor o administrador
- **Eliminar noticia** (`/noticias/eliminar/<id>/`) - Solo autor o administrador

#### Características Especiales
- Filtrado por categorías mediante parámetros GET
- Búsqueda en títulos y contenido
- Sistema de paginación para listas extensas
- Carga de imágenes para ilustrar noticias

### 💬 Módulo Comentarios

#### Funcionalidades
- **Agregar comentarios** a noticias (usuarios registrados)
- **Responder comentarios** para crear hilos de discusión
- **Moderar comentarios** (administradores)
- **Eliminar comentarios propios** (usuarios registrados)

### 👥 Módulo Usuarios

#### Vistas de Autenticación
- **Registro de usuario** (`/usuarios/registro/`)
- **Inicio de sesión** (`/usuarios/login/`)
- **Cierre de sesión** (`/usuarios/logout/`)
- **Perfil de usuario** (`/usuarios/perfil/`)

#### Sistema de Permisos
- **Administrador**: Acceso completo a todas las funciones
- **Editor**: Puede crear, editar noticias y moderar comentarios  
- **Usuario registrado**: Puede comentar y gestionar su perfil
- **Usuario anónimo**: Solo lectura de noticias

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
|  | `` | [![GitHub Badge](https://img.shields.io/badge/GitHub-121011?style=for-the-badge&logo=github&logoColor=white)](https://github.com/) |
|  | `` | [![GitHub Badge](https://img.shields.io/badge/GitHub-121011?style=for-the-badge&logo=github&logoColor=white)](https://github.com/) |
|  | `` | [![GitHub Badge](https://img.shields.io/badge/GitHub-121011?style=for-the-badge&logo=github&logoColor=white)](https://github.com/) |
|  | `` | [![GitHub Badge](https://img.shields.io/badge/GitHub-121011?style=for-the-badge&logo=github&logoColor=white)](https://github.com/) |
|  | `` | [![GitHub Badge](https://img.shields.io/badge/GitHub-121011?style=for-the-badge&logo=github&logoColor=white)](https://github.com/) |
| Aldo Andrés Acosta | `Andres777777` | [![GitHub Badge](https://img.shields.io/badge/GitHub-121011?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Andres777777) |
| Juan Diego González Antoniazzi | `JDGA1997` | [![GitHub Badge](https://img.shields.io/badge/GitHub-121011?style=for-the-badge&logo=github&logoColor=white)](https://github.com/JDGA1997) |

## 🤝 Contribuciones

Este proyecto es parte del curso de Programación - Etapa 2 del **Informatorio**. Las contribuciones están limitadas a los miembros del equipo durante el período académico.

## 📄 Licencia

Este proyecto es desarrollado con fines educativos como parte del programa Informatorio.

## 🏆 Logros Académicos

- ✅ Implementación completa de CRUD para noticias
- ✅ Sistema de comentarios interactivo con respuestas
- ✅ Manejo de usuarios, permisos y roles
- ✅ Uso de Django ORM y relaciones de base de datos
- ✅ Desarrollo con vistas basadas en clases (CBV)
- ✅ Sistema de filtrado y búsqueda avanzado
- ✅ Gestión de archivos multimedia
- ✅ Arquitectura modular con apps separadas
- ✅ Portal especializado en robótica

---

<div align="center">

### ⭐ Si este proyecto te fue útil, ¡no olvides darle una estrella!

**Desarrollado con 🤖❤️ por el Grupo N°4 - Informatorio 2025**

[![Informatorio](https://img.shields.io/badge/Informatorio-2025-blue?style=for-the-badge)](https://www.informatorio.org/)

</div>
