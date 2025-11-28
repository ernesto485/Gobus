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

## 🏗️ Arquitectura del Proyecto

```
mi_proyecto/
├── core/                    # Aplicación principal
│   ├── migrations/         # Migraciones de base de datos
│   ├── templates/core/     # Templates del core
│   ├── views.py           # Vistas principales
│   ├── urls.py            # URLs del core
│   └── admin.py           # Configuración de admin
├── mi_proyecto/           # Configuración del proyecto
│   ├── settings.py        # Configuraciones principales
│   ├── urls.py           # URLs globales
│   └── wsgi.py           # Configuración WSGI
├── templates/             # Templates globales
│   ├── base.html         # Plantilla base
│   ├── home.html         # Página principal
│   └── registration/     # Templates de autenticación
├── static/               # Archivos estáticos
│   ├── css/             # Hojas de estilo
│   └── javascript/      # Scripts JavaScript
└── db.sqlite3           # Base de datos SQLite
```

## 🚀 Flujo de Autenticación

### 1. **Proceso de Login**
```
Usuario → /accounts/login/ → Formulario → Validación → /home/
```

- **URL**: `/accounts/login/`
- **Template**: `registration/login.html`
- **Vista**: `django.contrib.auth.views.LoginView`
- **Redirección**: `LOGIN_REDIRECT_URL = 'home'`

### 2. **Protección de Vistas**
```python
@login_required
def home(request):
    return render(request, 'core/home.html')
```

### 3. **Proceso de Logout**
```
Usuario → POST /accounts/logout/ → Cierre de sesión → /accounts/login/
```

## 🔧 Configuración y Configuraciones Clave

### Configuraciones de Autenticación
```python
# settings.py
LOGIN_URL = 'login'              # URL para redirección de login
LOGIN_REDIRECT_URL = 'home'      # URL post-login exitoso
LOGOUT_REDIRECT_URL = 'login'    # URL post-logout
```

### Middleware de Autenticación
```python
MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # ... otros middleware
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
   pip install django==5.2.8
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
