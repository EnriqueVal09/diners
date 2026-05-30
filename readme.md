# Diners — Sistema de Menú Digital

Aplicación web fullstack para la gestión y visualización de menús digitales en restaurantes. Permite al administrador gestionar categorías y productos de forma dinámica, con soporte para imágenes en la nube y base de datos en producción.

## Stack tecnológico

- **Backend:** Python 3 / Django 5.2
- **Base de datos:** PostgreSQL (via `dj-database-url`)
- **Almacenamiento de imágenes:** Cloudinary
- **Frontend:** Django Templates + Tailwind CSS (`django-tailwind`)
- **Servidor de producción:** Gunicorn + WhiteNoise
- **Despliegue:** Railway

## Funcionalidades

- CRUD completo de productos y categorías
- Gestión de imágenes de productos mediante Cloudinary
- Vista de menú pública para clientes
- Panel de administración para el restaurante
- Configuración lista para producción (variables de entorno, archivos estáticos, migraciones automáticas)

## Estructura del proyecto

```
diners/
├── apps/          # Aplicaciones Django (productos, categorías, etc.)
├── core/          # Configuración principal del proyecto (settings, urls, wsgi)
├── templates/     # Plantillas HTML
├── theme/         # Configuración de Tailwind CSS
├── .env.example   # Variables de entorno requeridas
├── Procfile       # Configuración de despliegue en Railway
└── requirements.txt
```

## Instalación local

### Requisitos previos

- Python 3.10+
- PostgreSQL
- Cuenta en [Cloudinary](https://cloudinary.com/) (gratuita)

### Pasos

```bash
# 1. Clona el repositorio
git clone https://github.com/EnriqueVal09/diners.git
cd diners

# 2. Crea y activa un entorno virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Instala dependencias
pip install -r requirements.txt

# 4. Configura las variables de entorno
cp .env.example .env
# Edita .env con tus credenciales (ver sección siguiente)

# 5. Aplica migraciones
python manage.py migrate

# 6. Crea un superusuario
python manage.py createsuperuser

# 7. Inicia el servidor
python manage.py runserver
```

## Variables de entorno

Copia `.env.example` a `.env` y completa los valores:

```env
SECRET_KEY=tu_clave_secreta_django
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgres://usuario:password@localhost:5432/diners
CLOUDINARY_URL=cloudinary://api_key:api_secret@cloud_name
CSRF_TRUSTED_ORIGINS=http://localhost:8000
```

## Despliegue en Railway

El proyecto incluye `Procfile` con el comando de despliegue:

```
web: python manage.py collectstatic --noinput && python manage.py migrate && gunicorn core.wsgi --log-file -
```

Para desplegar: conecta el repositorio en [Railway](https://railway.app/), configura las variables de entorno del `.env.example` y Railway ejecutará el `Procfile` automáticamente.

## Autor

**Enrique Chavez Valdez** — [github.com/EnriqueVal09](https://github.com/EnriqueVal09)
