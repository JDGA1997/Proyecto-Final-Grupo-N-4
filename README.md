<div align="center">
  <img src="https://github.com/user-attachments/assets/df02cfe1-dd25-41d8-9cc3-2cea31e60d1a" alt="Logo del Proyecto" width="400"/>

# 🤖 Portal de Noticias sobre Robótica
## Proyecto Final - Desarrollo Web con Django - Grupo N°4

[![Django](https://img.shields.io/badge/Django-5.2.4-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.1.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![Pillow](https://img.shields.io/badge/Pillow-11.3.0-4285F4?style=for-the-badge&logo=python&logoColor=white)](https://pillow.readthedocs.io/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
![Estado](https://img.shields.io/badge/Estado-Completado-green?style=for-the-badge)

*Portal moderno de noticias especializadas en robótica, automatización industrial y tecnología robótica del futuro*

</div>

---

## 📋 Tabla de Contenidos

- [🚀 Descripción General](#-descripción-general)
- [🛠️ Stack Tecnológico](#️-stack-tecnológico)
- [📁 Estructura del Proyecto](#-estructura-del-proyecto)
- [⚙️ Instalación y Configuración](#️-instalación-y-configuración)
- [🎯 Funcionalidades Principales](#-funcionalidades-principales)
- [👤 Perfiles de Usuario y Credenciales](#-perfiles-de-usuario-y-credenciales)
- [🌐 Navegación y Páginas](#-navegación-y-páginas)
- [📱 Diseño Responsive](#-diseño-responsive)
- [👥 Equipo](#-equipo)

---

## 🚀 Descripción General

El **Portal de Noticias sobre Robótica** es una aplicación web moderna desarrollada con Django que se especializa en noticias y contenido relacionado con robótica, automatización industrial y tecnología robótica del futuro. Este proyecto implementa las mejores prácticas de desarrollo web y ofrece una experiencia de usuario moderna y responsiva.

### Características Destacadas

| Característica | Descripción | Estado |
|:---------------|:------------|:------:|
| **🎨 UI Moderna** | Interfaz Bootstrap 5 con efectos visuales | ✅ |
| **📱 Responsive** | Adaptable a móviles, tablets y desktop | ✅ |
| **🔐 Autenticación** | Sistema de usuarios completo | ✅ |
| **🔑 Perfiles de Usuario** | Visitante, Miembro, Colaborador | ✅ |
| **📸 Multimedia** | Soporte completo para imágenes | ✅ |
| **🔍 Búsqueda Avanzada** | Filtrado inteligente y ordenamiento | ✅ |
| **💬 Comentarios** | Sistema completo de comentarios | ✅ |
| **📄 Páginas Completas** | Acerca de, Contacto, Detalles | ✅ |
| **🏷️ Ordenamiento** | Por fecha y alfabético (ASC/DESC) | ✅ |
| **⚡ Performance** | Optimizado para velocidad | ✅ |
| **🛡️ Seguridad** | CSRF protection y validaciones | ✅ |

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
│   ├── 📁 noticias/              # App principal de noticias
│   │   ├── 📄 models.py          # Modelos mejorados con imágenes
│   │   ├── 📄 views.py           # Vistas con búsqueda y paginación
│   │   ├── 📄 admin.py           # Panel admin personalizado
│   │   ├── 📄 urls.py            # URLs organizadas
│   │   └── 📁 migrations/        # Migraciones de base de datos
│   └── 📁 authentication/        # App de autenticación
│       ├── 📄 models.py          # Modelos de perfil de usuario
│       ├── 📄 views.py           # Vistas de login/registro
│       ├── 📄 forms.py           # Formularios de autenticación
│       ├── 📄 urls.py            # URLs de auth (/auth/)
│       └── 📁 migrations/        # Migraciones de autenticación
├── 📁 grupo4/
│   ├── 📁 settings/              # Configuraciones por ambiente
│   │   ├── 📄 base.py            # Configuración base + nueva app
│   │   ├── 📄 local.py           # Desarrollo local
│   │   └── 📄 production.py      # Producción
│   ├── 📄 urls.py                # URLs principales + auth
│   └── 📄 views.py               # Vista de inicio
├── 📁 templates/                 # Templates limpios y optimizados
│   ├── 📄 base.html              # Template base responsivo
│   ├── 📄 index.html             # Página de inicio moderna
│   ├── 📄 acerca_de.html         # Página sobre el equipo
│   ├── 📄 contacto.html          # Página de contacto
│   ├── 📁 auth/                  # Templates de autenticación
│   │   ├── 📄 login.html         # Página de inicio de sesión
│   │   └── 📄 register.html      # Página de registro
│   └── 📁 noticias/              # Templates de noticias
│       ├── 📄 todas_noticias.html   # Con filtros avanzados
│       ├── 📄 una_noticia.html      # Detalle completo
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
python -m venv .venv
```

### **4. Activar Entorno Virtual**
```bash
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### **5. Instalar Dependencias**
```bash
pip install -r requirements.txt
```

### **6. Configurar Base de Datos**
```bash
python manage.py makemigrations
python manage.py migrate
```

### **7. Crear Superusuario (Opcional)**
```bash
python manage.py createsuperuser
```

### **8. Ejecutar Servidor de Desarrollo**
```bash
python manage.py runserver
```

### **9. Acceder a la Aplicación**
- **Portal Principal**: http://127.0.0.1:8000/
- **Lista de Noticias**: http://127.0.0.1:8000/noticias/
- **Login**: http://127.0.0.1:8000/auth/login/
- **Registro**: http://127.0.0.1:8000/auth/register/
- **Logout**: http://127.0.0.1:8000/auth/logout/
- **Acerca de**: http://127.0.0.1:8000/noticias/acerca-de/
- **Contacto**: http://127.0.0.1:8000/noticias/contacto/
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
- **Vista de detalle completa** con comentarios y compartir

### **🔍 Búsqueda y Filtrado Inteligente**
- **Búsqueda por texto** en título, subtítulo y contenido
- **Filtrado por categoría** con menú desplegable
- **Ordenamiento avanzado**: Por fecha (ASC/DESC) y alfabético (A-Z/Z-A)
- **Paginación inteligente** de resultados con preservación de filtros
- **URLs amigables** optimizadas para SEO

### **🔐 Sistema de Autenticación**
- **Registro de usuarios**: Formulario completo con validaciones Django
- **Login/Logout**: Sistema funcional implementado con redirecciones correctas
- **Estructura modular**: App independiente para escalabilidad
- **Perfiles de usuario**: Tres tipos implementados (Visitante, Miembro, Colaborador)
- **Control de permisos**: Restricciones implementadas por tipo de perfil
- **Templates responsivos**: Páginas de autenticación integradas al diseño

### **💬 Sistema de Comentarios**
- **Comentarios por noticia** con sistema de moderación
- **Interfaz intuitiva** para usuarios
- **Validación robusta** de datos de entrada
- **Timestamps automáticos** para seguimiento

### **📄 Páginas Institucionales**
- **Página "Acerca de"**: Información completa del equipo y proyecto
- **Página "Contacto"**: Formulario profesional con validación
- **FAQ integrado** con preguntas frecuentes

---

## 👤 Perfiles de Usuario y Credenciales

### **🔑 Tipos de Perfiles Disponibles**

#### **👀 Visitante**
- **Permisos**: Solo lectura de noticias públicas
- **Acceso**: Navegación por todas las páginas sin autenticación
- **Funcionalidades**: Ver noticias, usar filtros, acceder a páginas institucionales

#### **👤 Miembro**
- **Permisos**: Lectura completa + comentarios
- **Registro**: Cualquier usuario puede registrarse como Miembro
- **Funcionalidades adicionales**: 
  - Comentar en noticias
  - Acceso a secciones exclusivas para miembros
  - Perfil personalizado

#### **✍️ Colaborador**
- **Permisos**: Gestión completa de contenido
- **Funcionalidades administrativas**:
  - Crear, editar y eliminar noticias
  - Moderar comentarios
  - Gestionar categorías y autores
  - Acceso a herramientas avanzadas

### **🎫 Credenciales de Prueba**

#### **Administrador del Sistema**
```
Usuario: admin
Contraseña: admin123
Tipo: Superusuario
URL: http://127.0.0.1:8000/admin/
```

#### **Usuario Colaborador**
```
Usuario: colaborador1
Contraseña: test123456
Tipo: Colaborador
Funciones: Gestión completa de noticias
```

#### **Usuario Miembro**
```
Usuario: miembro1
Contraseña: test123456
Tipo: Miembro
Funciones: Comentarios y lectura
```

#### **Usuario Visitante**
```
Usuario: visitante1
Contraseña: test123456
Tipo: Visitante
Funciones: Solo lectura
```

### **🔧 Crear Nuevos Usuarios**

Para crear usuarios adicionales, puedes:

1. **Registro público**: Usar el formulario en `/auth/register/`
2. **Panel admin**: Acceder como administrador a `/admin/`
3. **Comando terminal**:
```bash
python manage.py createsuperuser
```

### **🛡️ Sistema de Permisos**

| Acción | Visitante | Miembro | Colaborador |
|:-------|:---------:|:-------:|:-----------:|
| Ver noticias | ✅ | ✅ | ✅ |
| Usar filtros | ✅ | ✅ | ✅ |
| Comentar | ❌ | ✅ | ✅ |
| Crear noticias | ❌ | ❌ | ✅ |
| Editar noticias | ❌ | ❌ | ✅ |
| Eliminar noticias | ❌ | ❌ | ✅ |
| Moderar comentarios | ❌ | ❌ | ✅ |
| Acceso admin | ❌ | ❌ | Parcial |

---

## 🌐 Navegación y Páginas

### **📱 Navbar Dinámico**
- **Usuario no autenticado**: Enlaces a Login y Registro
- **Usuario autenticado**: Muestra nombre de usuario, tipo de perfil y opciones de logout
- **Responsive**: Colapsa en móviles con hamburger menu
- **Indicadores visuales**: Badge con tipo de perfil actual

### **🗺️ Mapa del Sitio**
```
Inicio (/)
├── Noticias (/noticias/)
│   ├── Detalle de noticia (/noticias/<id>/)
│   ├── Nueva noticia (/noticias/crear/) [Solo Colaboradores]
│   ├── Editar noticia (/noticias/actualizar/<id>/) [Solo Colaboradores]
│   └── Eliminar noticia (/noticias/eliminar/<id>/) [Solo Colaboradores]
├── Autenticación (/auth/)
│   ├── Login (/auth/login/)
│   ├── Registro (/auth/register/)
│   └── Logout (/auth/logout/)
├── Acerca de (/noticias/acerca-de/)
├── Contacto (/noticias/contacto/)
└── Administración (/admin/) [Solo Administradores]
```

---

## 📱 Diseño Responsive

### **🎨 Características del Diseño**
- **Mobile First**: Optimizado primero para dispositivos móviles
- **Bootstrap 5**: Framework responsive con grid system
- **Breakpoints**: sm (576px), md (768px), lg (992px), xl (1200px)
- **Typography**: Escala responsiva con Google Fonts (Roboto)
- **Imágenes**: Redimensionado automático con clases responsive

### **📺 Compatibilidad de Dispositivos**
- **📱 Móviles**: 320px - 767px
- **📟 Tablets**: 768px - 991px  
- **💻 Desktop**: 992px - 1199px
- **🖥️ Large Desktop**: 1200px+

### **🌈 Paleta de Colores**
- **Primario**: #007bff (Azul tecnológico)
- **Secundario**: #6c757d (Gris moderno)
- **Éxito**: #28a745 (Verde confirmación)
- **Advertencia**: #ffc107 (Amarillo alerta)
- **Peligro**: #dc3545 (Rojo error)
=======
## 📝 **Últimas Actualizaciones**

### **🔄 Cambios Recientes (Enero 2025)**
- ✅ **Sistema de autenticación completado**: App `authentication` funcional
  - ✅ Registro de usuarios con validaciones
  - ✅ Login/logout con redirecciones correctas
  - ✅ URLs integradas en `/auth/`
  - ✅ Templates responsivos implementados
- ✅ **Correcciones críticas**: Errores de sintaxis y configuración resueltos
  - ✅ Fix indentación en `views.py` de authentication
  - ✅ Fix imports en `urls.py` de authentication
  - ✅ Configuración de admin corregida
- ✅ **Servidor completamente funcional**: Todas las rutas operativas
- ✅ **Documentación actualizada**: README reflejando estado actual

### **🎯 Próximos Objetivos**
- 🔄 **Modelo Profile**: Implementar tipos de usuario (Visitante, Miembro, Colaborador)
- 🔄 **Integración de permisos**: Restricciones por tipo de perfil
- 🔄 **Navbar dinámico**: Mostrar estado de autenticación del usuario

---

## 👥 Equipo

Este proyecto fue posible gracias al trabajo colaborativo de nuestro equipo:

| Nombre y Apellido | Usuario en GitHub | Perfil de GitHub |
| ----------------- | ----------------- | ---------------- |
| Aldo Andrés Acosta | `Andres777777` | [![GitHub Badge](https://img.shields.io/badge/GitHub-121011?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Andres777777) |
| Valentino André Cabás | `Valen-cbs` | [![GitHub Badge](https://img.shields.io/badge/GitHub-121011?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Valen-cbs) |
| Vallejos Nahuel | `Nahuel151` | [![GitHub Badge](https://img.shields.io/badge/GitHub-121011?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Nahuel151) |
| Juan Diego González Antoniazzi | `JDGA1997` | [![GitHub Badge](https://img.shields.io/badge/GitHub-121011?style=for-the-badge&logo=github&logoColor=white)](https://github.com/JDGA1997) |

---

<div align="center">

### 🤖 **Portal de Noticias sobre Robótica**

*Desarrollado con ❤️ por el Grupo N°4 - Informatorio 2025*
*Fecha de última actualización: Agosto 16, 2025*

[![Made with Django](https://img.shields.io/badge/Made%20with-Django-092E20?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![Powered by Bootstrap](https://img.shields.io/badge/Powered%20by-Bootstrap-7952B3?style=flat-square&logo=bootstrap)](https://getbootstrap.com/)
[![Built with Python](https://img.shields.io/badge/Built%20with-Python-3776AB?style=flat-square&logo=python)](https://www.python.org/)

---

**© 2025 - Informatorio Chaco | Proyecto Final de Desarrollo Web con Django**

*"Construyendo el futuro de la información robótica, una línea de código a la vez"*

</div>
