# 🚌 GoBus - Sistema de Gestión de Transporte

![Django](https://img.shields.io/badge/Django-5.2.8-green?logo=django)
![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey?logo=sqlite)

> **Sistema moderno de gestión de transporte con autenticación segura y diseño responsivo**

## 📋 Descripción

GoBus es una aplicación web desarrollada con Django que proporciona una plataforma completa para la gestión de servicios de transporte. Cuenta con un sistema de autenticación robusto, interfaz intuitiva y arquitectura escalable.

### 🎯 Características Principales

- 🔐 **Autenticación Segura**: Sistema de login/logout integrado de Django
- 📱 **Diseño Responsivo**: Interfaz moderna adaptable a todos los dispositivos
- 🚌 **Gestión de Transporte**: Plataforma optimizada para servicios de transporte
- 🎨 **UI/UX Moderna**: Diseño limpio con Bootstrap y estilos personalizados
- 🛡️ **Protección de Rutas**: Vistas protegidas con decoradores de Django

## 🏗️ Arquitectura del Sistema

GoBus está construido siguiendo las mejores prácticas de Django con una arquitectura modular y escalable:

### **Estructura de Directorios**
```
mi_proyecto/
├── core/                    # Aplicación principal de negocio
│   ├── migrations/         # Migraciones de base de datos
│   ├── templates/core/     # Templates específicos del core
│   ├── views.py           # Vistas principales y lógica de negocio
│   ├── urls.py            # Enrutamiento de URLs del core
│   ├── models.py          # Modelos de datos (cuando se agreguen)
│   ├── forms.py           # Formularios personalizados
│   └── admin.py           # Configuración del panel de administración
├── mi_proyecto/           # Configuración principal del proyecto
│   ├── settings.py        # Configuraciones globales y de aplicación
│   ├── urls.py           # Enrutamiento principal de URLs
│   ├── wsgi.py           # Configuración para despliegue WSGI
│   └── asgi.py           # Configuración para aplicaciones asíncronas
├── templates/             # Templates globales compartidos
│   ├── base.html         # Plantilla base con estructura común
│   ├── home.html         # Página principal de la aplicación
│   └── registration/     # Templates del sistema de autenticación
├── static/               # Archivos estáticos del proyecto
│   ├── css/             # Hojas de estilo CSS
│   │   ├── base.css     # Estilos principales
│   │   ├── auth.css     # Estilos de autenticación
│   │   └── bootstrap/   # Framework CSS Bootstrap
│   └── javascript/      # Scripts JavaScript
│       └── bootstrap/   # Componentes JavaScript Bootstrap
└── db.sqlite3           # Base de datos SQLite para desarrollo
```

### **Patrones de Diseño Implementados**

#### **1. MVT (Model-View-Template)**
- **Models**: Definición de estructura de datos (extensible)
- **Views**: Lógica de negocio y procesamiento de peticiones
- **Templates**: Presentación y capa visual

#### **2. Configuración Modular**
- Separación clara entre configuración del proyecto y aplicación
- URLs organizadas jerárquicamente
- Templates estructurados por aplicación

#### **3. Sistema de Autenticación Django**
- Integración nativa con el sistema de usuarios de Django
- Middleware de autenticación y sesiones
- Decoradores de protección de vistas
- Templates personalizados para login/logout

## 🔧 Configuración del Sistema

### **Configuraciones Principales (settings.py)**

#### **Configuración de Autenticación**
```python
# URLs de autenticación
LOGIN_URL = 'login'              # Redirección para usuarios no autenticados
LOGIN_REDIRECT_URL = 'home'      # Destino después de login exitoso
LOGOUT_REDIRECT_URL = 'login'    # Destino después de logout
```

#### **Configuración de Aplicaciones**
```python
INSTALLED_APPS = [
    'django.contrib.admin',       # Panel de administración
    'django.contrib.auth',        # Sistema de autenticación
    'django.contrib.contenttypes', # Tipos de contenido
    'django.contrib.sessions',    # Manejo de sesiones
    'django.contrib.messages',     # Sistema de mensajes
    'django.contrib.staticfiles',  # Archivos estáticos
    'core',                       # Aplicación principal de negocio
]
```

#### **Middleware de Procesamiento**
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',      # Seguridad
    'django.contrib.sessions.middleware.SessionMiddleware', # Sesiones
    'django.middleware.common.CommonMiddleware',           # Utilidades comunes
    'django.middleware.csrf.CsrfViewMiddleware',         # Protección CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Autenticación
    'django.contrib.messages.middleware.MessageMiddleware', # Mensajes
    'django.middleware.clickjacking.XFrameOptionsMiddleware', # Clickjacking
]
```

#### **Configuración de Templates**
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Directorio de templates global
        'APP_DIRS': True,                  # Templates por aplicación
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

#### **Configuración de Base de Datos**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Motor SQLite
        'NAME': BASE_DIR / 'db.sqlite3',        # Archivo de base de datos
    }
}
```

#### **Configuración de Archivos Estáticos**
```python
STATIC_URL = 'static/'                    # URL para archivos estáticos
STATICFILES_DIRS = [BASE_DIR / 'static']   # Directorios de archivos estáticos
```

### **Configuración de URLs**

#### **URLs Principales (mi_proyecto/urls.py)**
```python
urlpatterns = [
    path('admin/', admin.site.urls),                                    # Panel admin
    path('', include('core.urls')),                                     # URLs del core
    path('accounts/login/', auth_views.LoginView.as_view(
        template_name='registration/login.html'), name='login'),        # Login
    path('accounts/logout/', logout_view, name='logout'),              # Logout
]
```

#### **URLs del Core (core/urls.py)**
```python
urlpatterns = [
    path('', views.home, name='home'),  # Página principal protegida
]
```

## 🛠️ Instalación y Configuración

### Prerrequisitos
- Python 3.8+
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar el repositorio**
   ```bash
   git clone <repository-url>
   cd mi_proyecto
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Migraciones de base de datos**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crear superusuario**
   ```bash
   python manage.py createsuperuser
   ```

6. **Iniciar servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```

7. **Acceder a la aplicación**
   - **Aplicación**: http://127.0.0.1:8000/
   - **Admin**: http://127.0.0.1:8000/admin/

## 🎨 Diseño y Estilos

### Estructura de Templates
- **Base Template**: `templates/base.html`
- **Auth Templates**: `templates/registration/`
- **Core Templates**: `core/templates/core/`

### Estilos CSS
- **Framework**: Bootstrap
- **Personalización**: `static/css/base.css`, `static/css/auth.css`
- **Iconos**: SVG integrados y Bootstrap Icons

### Componentes UI
- **Auth Card**: Diseño moderno para login
- **Brand Badge**: Logo personalizado de GoBus
- **Responsive Design**: Mobile-first approach

## 🔒 Seguridad

### Características de Seguridad
- ✅ CSRF protection habilitado
- ✅ Autenticación de usuarios Django
- ✅ Middleware de seguridad
- ✅ Validación de contraseñas
- ✅ Protección contra ataques comunes

### Validadores de Contraseña
```python
AUTH_PASSWORD_VALIDATORS = [
    'UserAttributeSimilarityValidator',
    'MinimumLengthValidator',
    'CommonPasswordValidator',
    'NumericPasswordValidator',
]
```

## 📊 Base de Datos

### Modelo de Usuario
Django utiliza el modelo `User` estándar con:
- Credenciales de autenticación
- Permisos y grupos
- Campos personalizados posibles

### Tablas Principales
- `auth_user`: Datos de usuarios
- `auth_group`: Grupos de usuarios
- `auth_permission`: Permisos del sistema

## 🚀 Despliegue

### Consideraciones de Producción
- Cambiar `DEBUG = False`
- Configurar `ALLOWED_HOSTS`
- Usar base de datos PostgreSQL/MySQL
- Configurar archivos estáticos
- Implementar HTTPS

### Variables de Entorno
```python
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
```

## 🤝 Contribución

1. Fork del proyecto
2. Crear feature branch: `git checkout -feature/nueva-funcionalidad`
3. Commit de cambios: `git commit -m 'Agrega nueva funcionalidad'`
4. Push al branch: `git push origin feature/nueva-funcionalidad`
5. Abrir Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT.

## 📞 Contacto

- **Proyecto**: GoBus - Gestión de Transporte
- **Tecnología**: Django 5.2.8
- **Base de Datos**: SQLite (desarrollo)

---

> **Nota**: Este proyecto utiliza el sistema de autenticación integrado de Django para garantizar la seguridad y fiabilidad del sistema de gestión de transporte.
