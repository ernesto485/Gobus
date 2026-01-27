# 🚌 GoBus - Panel Administrativo de Ventas de Billetes

![Django](https://img.shields.io/badge/Django-5.2.8-green?logo=django)
![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey?logo=sqlite)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?logo=bootstrap)

> **Panel administrativo moderno para la gestión y venta de billetes de transporte**

## 📋 Descripción General

GoBus es una plataforma web integral de gestión de transporte diseñada específicamente para la administración y venta de billetes de viaje. El sistema proporciona herramientas completas para la gestión de flotas, rutas, conductores y el procesamiento de ventas de billetes, todo dentro de una interfaz administrativa segura y fácil de usar.

### 🎯 Propósito Principal

Gobus sirve como el sistema backend administrativo que soporta las operaciones de una empresa de transporte, permitiendo:
- Gestión completa de la flota de autobuses
- Administración de rutas y horarios
- Gestión de personal conductor
- Procesamiento y seguimiento de ventas de billetes

## 🔧 Características Principales

### **Gestión de Recursos**
- 🚌 **Gestión de Autobuses**: Registro, edición y eliminación de unidades con matrícula, capacidad y modelo
- 👨‍✈️ **Gestión de Conductores**: Administración de personal con licencias y asignaciones
- 🛣️ **Gestión de Rutas**: Creación de rutas con origen, destino, paradas intermedias y horarios
- 🎫 **Gestión de Billetes**: Sistema completo de venta y seguimiento de billetes

### **Características Técnicas**
- 🔐 **Autenticación Segura**: Sistema de login/logout con decoradores de protección
- 📱 **Diseño Responsivo**: Interfaz adaptable a todos los dispositivos
- 🎨 **UI/UX Moderna**: Bootstrap 5 con estilos personalizados
- 📊 **Paginación**: Manejo eficiente de grandes volúmenes de datos
- 🔄 **CRUD Completo**: Operaciones completas para todos los modelos
- 📈 **Dashboard**: Vista general con estadísticas del sistema

## 📋 Requisitos Funcionales

### **RF-01 Gestión de Autobuses**
- El sistema debe permitir registrar nuevos autobuses con matrícula única
- Debe almacenar capacidad y modelo de cada unidad
- Debe permitir editar y eliminar autobuses existentes
- Debe mostrar detalles completos de cada autobús incluyendo rutas asignadas

### **RF-02 Gestión de Conductores**
- El sistema debe permitir registrar conductores con nombre y licencia única
- Debe mantener un registro actualizado de todo el personal conductor
- Debe permitir asignar conductores a rutas específicas
- Debe permitir editar y eliminar registros de conductores

### **RF-03 Gestión de Rutas**
- El sistema debe permitir crear rutas con origen, destino y paradas intermedias
- Debe almacenar distancia y frecuencia de las rutas
- Debe permitir asignar autobuses y conductores a cada ruta
- Debe gestionar horarios de salida programados

### **RF-04 Venta de Billetes**
- El sistema debe permitir la creación de billetes para usuarios registrados
- Debe asignar asientos específicos y calcular precios automáticamente
- Debe generar códigos QR para cada billete vendido
- Debe mantener un registro histórico de todas las ventas

### **RF-05 Gestión de Usuarios**
- El sistema debe proporcionar autenticación segura para administradores
- Debe proteger todas las funcionalidades administrativas
- Debe permitir cierre de sesión seguro
- Debe redirigir apropiadamente después de login/logout

### **RF-06 Reportes y Estadísticas**
- El sistema debe mostrar estadísticas en el dashboard principal
- Debe contar total de autobuses, rutas, conductores y billetes vendidos
- Debe permitir visualización detallada de cada entidad
- Debe proporcionar paginación para listas extensas

## 📋 Requisitos No Funcionales

### **RNF-01 Seguridad**
- Todas las vistas administrativas deben requerir autenticación
- El sistema debe implementar protección CSRF
- Las contraseñas deben cumplir con validadores de Django
- Las sesiones deben manejarse de forma segura

### **RNF-02 Rendimiento**
- El sistema debe responder en menos de 3 segundos para operaciones CRUD
- Debe implementar paginación para manejar grandes volúmenes de datos
- Las consultas a base de datos deben estar optimizadas
- El tiempo de carga del dashboard no debe exceder 2 segundos

### **RNF-03 Usabilidad**
- La interfaz debe ser intuitiva y fácil de navegar
- Debe ser completamente responsiva para móviles y tablets
- Debe proporcionar retroalimentación clara para todas las operaciones
- Los mensajes de éxito y error deben ser claros y específicos

### **RNF-04 Disponibilidad**
- El sistema debe estar disponible 99.5% del tiempo en producción
- Debe manejar errores gracefully sin caídas del sistema
- Debe proporcionar logging adecuado para troubleshooting
- Las operaciones críticas deben tener validación robusta

### **RNF-05 Escalabilidad**
- La arquitectura debe permitir fácil adición de nuevas funcionalidades
- El diseño de base de datos debe soportar crecimiento de datos
- El sistema debe poder manejar múltiples usuarios concurrentes
- La estructura de código debe seguir principios SOLID

## 🛠️ Tecnologías Utilizadas

### **Backend**
- **Django 5.2.8**: Framework web principal
- **Python 3.8+**: Lenguaje de programación
- **SQLite**: Base de datos para desarrollo
- **Gunicorn 21.2.0**: Servidor WSGI para producción

### **Frontend**
- **Bootstrap 5**: Framework CSS para diseño responsivo
- **HTML5**: Estructura semántica de las páginas
- **CSS3**: Estilos personalizados y animaciones
- **JavaScript**: Interactividad del lado del cliente

### **Infraestructura**
- **WhiteNoise 6.6.0**: Servidor de archivos estáticos
- **Django Templates**: Motor de plantillas
- **Django Auth**: Sistema de autenticación integrado
- **Django Messages**: Sistema de mensajes flash

### **Desarrollo y Despliegue**
- **Git**: Control de versiones
- **Railway**: Plataforma de despliegue (producción)
- **Virtual Environment**: Aislamiento de dependencias
- **pip**: Gestor de paquetes de Python

## 🏗️ Arquitectura del Sistema

GoBus está construido siguiendo las mejores prácticas de Django con una arquitectura modular y escalable:

### **Estructura de Directorios**
```
gobus/
├── core/                    # Aplicación principal de negocio
│   ├── migrations/         # Migraciones de base de datos
│   ├── templates/core/     # Templates específicos del core
│   │   ├── autobus/       # Templates de gestión de autobuses
│   │   ├── billetes/      # Templates de gestión de billetes
│   │   ├── conductores/    # Templates de gestión de conductores
│   │   └── ruta/          # Templates de gestión de rutas
│   ├── views.py           # Vistas principales y lógica de negocio
│   ├── urls.py            # Enrutamiento de URLs del core
│   ├── models.py          # Modelos de datos (Autobus, Ruta, Conductor, Billete)
│   ├── forms.py           # Formularios personalizados
│   └── admin.py           # Configuración del panel de administración
├── gobus/                 # Configuración principal del proyecto
│   ├── settings.py        # Configuraciones globales y de aplicación
│   ├── urls.py           # Enrutamiento principal de URLs
│   ├── wsgi.py           # Configuración para despliegue WSGI
│   └── asgi.py           # Configuración para aplicaciones asíncronas
├── templates/             # Templates globales compartidos
│   ├── base.html         # Plantilla base con estructura común
│   └── registration/     # Templates del sistema de autenticación
├── static/               # Archivos estáticos del proyecto
│   ├── css/             # Hojas de estilo CSS
│   │   ├── base.css     # Estilos principales
│   │   ├── auth.css     # Estilos de autenticación
│   │   ├── home-modern.css # Estilos del dashboard
│   │   └── bootstrap/   # Framework CSS Bootstrap
│   └── javascript/      # Scripts JavaScript
│       └── bootstrap/   # Componentes JavaScript Bootstrap
└── db.sqlite3           # Base de datos SQLite para desarrollo
```

### **Modelo de Datos**

GoBus implementa un modelo de datos relacional con las siguientes entidades principales:

#### **Entidades Principales**
- **Autobus**: Unidades de transporte con matrícula, capacidad y modelo
- **Conductor**: Personal con licencia y asignaciones
- **Ruta**: Trayectos con origen, destino, paradas y horarios
- **Billete**: Ventas de pasajes con asignación de asientos

#### **Relaciones**
- Un **Autobus** puede tener múltiples **Rutas** (1:N)
- Un **Conductor** puede tener múltiples **Rutas** (1:N)
- Una **Ruta** puede tener múltiples **Billetes** (1:N)
- Los **Billetes** pertenecen a **Usuarios** del sistema

### **Patrones de Diseño Implementados**

#### **1. MVT (Model-View-Template)**
- **Models**: Definición de estructura de datos con relaciones complejas
- **Views**: Lógica de negocio con CRUD completo y paginación
- **Templates**: Presentación con herencia y componentes reutilizables

#### **2. Configuración Modular**
- Separación clara entre configuración del proyecto y aplicación
- URLs organizadas jerárquicamente con namespaces
- Templates estructurados por funcionalidad

#### **3. Sistema de Autenticación Django**
- Integración nativa con el sistema de usuarios de Django
- Middleware de autenticación y sesiones
- Decoradores `@login_required` para protección de vistas
- Templates personalizados para login/logout

#### **4. Gestión de Formularios**
- Formularios Django para validación automática
- Manejo de errores y retroalimentación al usuario
- Integración con modelos para operaciones CRUD

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

## 🚀 Instalación y Configuración

### Prerrequisitos
- Python 3.8+
- pip (gestor de paquetes de Python)
- Git (para clonar el repositorio)

### Pasos de Instalación

1. **Clonar el repositorio**
   ```bash
   git clone <repository-url>
   cd gobus
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
   - **Panel Administrativo**: http://127.0.0.1:8000/
   - **Admin Django**: http://127.0.0.1:8000/admin/

### **Configuración Inicial**

Después de la instalación, se recomienda:

1. **Crear datos de prueba** desde el panel de administración
2. **Configurar autobuses** con matrícula, capacidad y modelo
3. **Registrar conductores** con sus licencias correspondientes
4. **Crear rutas** asignando autobuses y conductores
5. **Probar la venta de billetes** desde el panel principal

## 🎨 Interfaz de Usuario

### **Dashboard Principal**
- **Estadísticas en tiempo real**: Total de autobuses, rutas, conductores y billetes
- **Navegación intuitiva**: Acceso rápido a todas las funcionalidades
- **Diseño moderno**: Interfaz limpia con Bootstrap 5
- **Totalmente responsivo**: Funciona en móviles, tablets y desktop

### **Gestión de Entidades**
Cada entidad (Autobuses, Conductores, Rutas, Billetes) incluye:
- **Lista paginada** con búsqueda y ordenamiento
- **Formularios de creación/edición** con validación
- **Vista de detalles** con información completa
- **Confirmación de eliminación** para evitar errores
- **Mensajes de éxito/error** para retroalimentación

### **Componentes UI**
- **Tarjetas informativas**: Para mostrar estadísticas y datos importantes
- **Tablas responsivas**: Para listas de datos con paginación
- **Modales y formularios**: Para operaciones CRUD
- **Alertas y notificaciones**: Sistema de mensajes de Django
- **Navegación consistente**: Menú principal y breadcrumbs

## 🔒 Seguridad Implementada

### **Autenticación y Autorización**
- ✅ Sistema de autenticación de Django
- ✅ Decoradores `@login_required` en todas las vistas
- ✅ Redirecciones automáticas para usuarios no autenticados
- ✅ Manejo seguro de sesiones
- ✅ Protección CSRF en todos los formularios

### **Validación de Datos**
- ✅ Validadores de contraseñas de Django
- ✅ Validación de formularios en backend
- ✅ Restricciones de unicidad en modelos
- ✅ Campos obligatorios y validaciones personalizadas

### **Seguridad en Producción**
- ✅ Variables de entorno para configuración sensible
- ✅ Configuración de ALLOWED_HOSTS
- ✅ Middleware de seguridad de Django
- ✅ Headers de seguridad HTTP

## 📊 Flujo de Trabajo del Sistema

### **1. Configuración Inicial**
1. Administrador accede al sistema
2. Configura autobuses disponibles
3. Registra conductores con sus licencias
4. Define rutas y horarios

### **2. Operación Diaria**
1. Asignación de autobuses y conductores a rutas
2. Venta de billetes a usuarios
3. Generación de códigos QR
4. Seguimiento de ventas y estadísticas

### **3. Gestión y Reportes**
1. Monitoreo desde el dashboard
2. Consulta de ventas y estadísticas
3. Gestión de incidencias
4. Actualización de datos

## 🌐 Despliegue en Producción

### **Configuración de Producción**
El proyecto está configurado para despliegue en Railway con:

- **Gunicorn**: Servidor WSGI para producción
- **WhiteNoise**: Servidor de archivos estáticos
- **Variables de entorno**: Para configuración segura
- **Base de datos**: Configurable para PostgreSQL/MySQL

### **Variables de Entorno Requeridas**
```python
SECRET_KEY=os.environ.get('SECRET_KEY')
DEBUG=os.environ.get('DEBUG', 'False') == 'True'
ALLOWED_HOSTS=['your-domain.com']
```

### **Consideraciones de Producción**
- Cambiar `DEBUG = False`
- Configurar `ALLOWED_HOSTS` apropiadamente
- Usar base de datos PostgreSQL para mejor rendimiento
- Configurar serving de archivos estáticos
- Implementar monitoring y logging

## 🔄 Mantenimiento y Actualizaciones

### **Tareas Regulares**
- **Backups de base de datos**: Diarios para producción
- **Actualización de dependencias**: Mensual
- **Revisión de logs**: Semanal
- **Optimización de consultas**: Trimestral

### **Escalabilidad**
- **Base de datos**: Migración a PostgreSQL/MySQL
- **Caching**: Implementación de Redis
- **CDN**: Para archivos estáticos
- **Load Balancing**: Para alta disponibilidad

## 🤝 Contribución

1. Fork del proyecto
2. Crear feature branch: `git checkout -b feature/nueva-funcionalidad`
3. Commit de cambios: `git commit -m 'Agrega nueva funcionalidad'`
4. Push al branch: `git push origin feature/nueva-funcionalidad`
5. Abrir Pull Request

### **Estándares de Código**
- Seguir PEP 8 para Python
- Usar nombres descriptivos para variables y funciones
- Documentar funciones complejas
- Mantener la estructura de directorios existente

## 📝 Licencia

Este proyecto está bajo la Licencia MIT.

## 📞 Contacto y Soporte

- **Proyecto**: GoBus - Panel Administrativo de Ventas de Billetes
- **Tecnología Principal**: Django 5.2.8
- **Base de Datos**: SQLite (desarrollo) / PostgreSQL (producción)
- **Despliegue**: Railway (producción)

---

> **Nota**: GoBus es un sistema administrativo completo diseñado para empresas de transporte que necesitan gestionar eficientemente sus operaciones de venta de billetes, flota de vehículos y personal conductor. La arquitectura modular permite fácil expansión y personalización según las necesidades específicas de cada negocio.
