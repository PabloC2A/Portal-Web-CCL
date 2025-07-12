# Portal-Web-CCL

**Portal-Web-CCL** es una aplicación web desarrollada con **Django** para gestionar funcionalidades propias de la Cámara de Comercio de Loja.

---

## 📋 Contenido

- [Requisitos previos](#-requisitos-previos)
- [Instalación](#-instalación)
- [Ejecución](#-ejecución)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Contribuciones](#-contribuciones)
- [Licencia](#-licencia)

---

## 🔍 Requisitos previos

Antes de comenzar, asegúrate de tener instalados:

- Python 3.10 o superior
- pip
- virtualenv

---

## 🛠️ Instalación

Clona el repositorio y accede a la carpeta del proyecto:

```bash
git clone https://github.com/PabloC2A/Portal-Web-CCL.git
cd Portal-Web-CCL
```

Crea y activa un entorno virtual:

```bash
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
```

Instala las dependencias:

```bash
pip install django==5.2.4
```

---

## ▶️ Ejecución

Aplica migraciones y ejecuta el servidor:

```bash
python manage.py migrate
python manage.py runserver
```

Accede a la aplicación en tu navegador:

```
http://localhost:8000/
```

---

## 📂 Estructura del proyecto

```
Portal-Web-CCL/
├── config/                       # Configuración global del proyecto
│   ├── settings/
│   │   ├── base.py
│   │   ├── dev.py
│   │   └── prod.py
│   ├── urls.py                  # Enrutamiento principal
│   └── wsgi.py / asgi.py
│
├── core/                         # Landing page, contacto, info institucional
│   ├── views.py
│   ├── urls.py
│   └── templates/core/
│       └── landing.html
│
├── users/                        # Modelo base de usuario y su administración
│   ├── models.py                # CustomUser con roles
│   ├── admin.py
│   ├── managers.py
│   └── apps.py
│
├── accounts/                     # Login, logout, autenticación, seguridad
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/accounts/
│       └── login.html
│
├── registration/                 # Registro de socios (persona natural o jurídica)
│   ├── models.py                # Solicitud de afiliación, tipo persona, estados
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/registration/
│       ├── register_natural.html
│       └── register_juridica.html
│
├── profiles/                     # Perfiles extendidos de usuarios
│   ├── models.py                # Datos personales, empresa, contactos
│   ├── views.py
│   ├── urls.py
│   └── templates/profiles/
│       └── profile_edit.html
│
├── dashboards/                   # Vistas post-login según el rol (socio, empleado)
│   ├── views.py
│   ├── urls.py
│   └── templates/dashboards/
│       ├── dashboard_socio.html
│       └── dashboard_empleado.html
│
├── memberships/                  # Tipos de membresía, estados, renovaciones
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/memberships/
│       └── estado.html
│
├── services/                     # Catálogo y solicitudes de servicios institucionales
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/services/
│       ├── listado.html
│       └── solicitar.html
│
├── payments/                     # Recepción de pagos (tarjeta, transferencia)
│   ├── models.py
│   ├── services.py             # Integración con pasarelas
│   ├── views.py
│   ├── urls.py
│   └── templates/payments/
│       └── comprobante.html
│
├── billing/                      # Facturación y comprobantes (opcional con SRI)
│   ├── models.py
│   ├── views.py
│   ├── sri_utils.py           # Validaciones tributarias si aplica
│   └── templates/billing/
│       └── factura.html
│
├── publications/                 # Noticias, comunicados, boletines institucionales
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/publications/
│       └── noticia_detalle.html
│
├── notifications/                # Emails, alertas internas, recordatorios
│   ├── models.py
│   ├── services.py             # Envío de correos y notificaciones
│   ├── views.py
│   └── templates/notifications/
│       └── correo_base.html
│
├── documents/                    # Subida y validación de documentos (RUC, actas)
│   ├── models.py
│   ├── views.py
│   ├── validators.py
│   └── templates/documents/
│       └── subir_documento.html
│
├── templates/                    # Templates globales y layouts
│   └── base.html
├── static/                       # Archivos estáticos (CSS, JS, imágenes)
├── media/                        # Archivos subidos por los usuarios
├── requirements.txt
└── manage.py
```

---

# 🤝 Contribuciones

¡Gracias por tu interés en contribuir a este proyecto!\
Sigue los pasos a continuación para colaborar de forma ordenada y efectiva.

---

## 🚀 Cómo contribuir

### 1. Haz un fork del repositorio

Haz clic en el botón **"Fork"** (arriba a la derecha en GitHub). Esto creará una copia del proyecto en tu cuenta.

### 2. Clona tu fork

```bash
git clone https://github.com/tu-usuario/Portal-Web-CCL.git
cd Portal-Web-CCL
```

> Reemplaza `tu-usuario` con tu nombre de usuario real de GitHub.

### 3. Crea una nueva rama para tu cambio

No trabajes directamente sobre la rama `main`.

```bash
git checkout -b feature/nombre-del-cambio
```

Ejemplos:

- `feature/login-usuario`
- `fix/bug-en-menu`
- `docs/actualiza-readme`

### 4. Realiza tus cambios

Haz los cambios que deseas y asegúrate de probar que todo funcione correctamente.

### 5. Haz commit de tus cambios

```bash
git add .
git commit -m "Descripción clara y concisa del cambio"
```

> Usa mensajes de commit que expliquen **qué hiciste** y **por qué**, no solo "cambios".

### 6. Sube tus cambios a tu fork

```bash
git push origin feature/nombre-del-cambio
```

### 7. Abre un Pull Request

1. Ve a tu fork en GitHub.
2. Haz clic en **"Compare & pull request"**.
3. Asegúrate de que el PR apunte a la rama `main` del repositorio original.
4. Escribe un título y descripción clara de tus cambios.
5. Haz clic en **"Create pull request"**.

---

## 🔄 Mantén tu fork actualizado

Es recomendable mantener tu fork sincronizado con el repositorio original.

### 1. Agrega el repositorio original como remoto

```bash
git remote add upstream https://github.com/PabloC2A/Portal-Web-CCL.git
```

### 2. Trae los últimos cambios

```bash
git fetch upstream
```

### 3. Mezcla los cambios en tu rama `main`

```bash
git checkout main
git merge upstream/main
```

### 4. Sube tu rama actualizada a tu fork

```bash
git push origin main
```

---

## 🧩 ¿Cómo integrar los cambios de una rama `feature/...` al `main` de tu fork?

### Opción 1: Pull Request interno en tu fork (recomendado)

1. Ve a tu fork en GitHub.
2. Haz clic en **"Pull Requests"** > **"New Pull Request"**.
3. En el comparador selecciona:
   - `base`: tu rama `main`
   - `compare`: tu rama `feature/nombre-del-cambio`
4. Revisa los cambios y haz clic en **"Create Pull Request"**.
5. Finalmente, haz clic en **"Merge pull request"**.

### Opción 2: Fusionar manualmente con Git

Si prefieres hacerlo desde la terminal:

```bash
git checkout main
git merge feature/nombre-del-cambio
git push origin main
```

Esta opción es directa y útil si no necesitas revisión de código o estás trabajando solo.

---

## ✅ Buenas prácticas

- Usa ramas para cada funcionalidad o corrección.
- Asegúrate de que tu código compila / pasa pruebas antes de hacer PR.
- Escribe descripciones claras en tus commits y pull requests.
- Si tienes dudas, abre un *issue* o comenta en el PR.

---
config
├── __init__.py
├── __pycache__
├── asgi.py
├── settings.py
├── urls.py
└── wsgi.py
core
├── __init__.py
├── __pycache__
├── admin.py
├── apps.py
├── migrations
│   ├── __init__.py
│   └── __pycache__
├── models.py
├── static
│   └── css
│   │   └── custom.css
│   └── img
│       ├── CCL_Logo.png
│       ├── CCL_Logo1.png
│       ├── CCL_Logo2.jpg
│       ├── beneficios-socios.jpg
│       ├── hero.png
│       ├── logos
│       │   ├── banco-guayaquil.png
│       │   ├── banco-loja.jpeg
│       │   ├── banco-pichincha.jpeg
│       │   ├── cooperativa-jep.png
│       │   ├── cuxibamba.png
│       │   └── hotel-howard.png
│       ├── news-1.jpg
│       ├── news-2.jpg
│       ├── news-3.png
│       ├── news-featured.jpg
│       └── team
│           ├── team-1.jpg
│           ├── team-2.jpg
│           ├── team-3.jpg
│           └── team-4.jpg
├── templates
│   └── core
│       ├── _form_corporativo.html
│       ├── _form_emprendedor.html
│       ├── _form_empresarial.html
│       ├── afiliacion.html
│       ├── base.html
│       ├── contacto.html
│       ├── index.html
│       ├── nosotros.html
│       ├── noticias.html
│       ├── servicios.html
│       └── socios.html
├── tests.py
├── urls.py
└── views.py
static
├── css
│   ├── argon-design-system.css
│   ├── argon-design-system.css.map
│   ├── argon-design-system.min.css
│   ├── font-awesome.css
│   ├── nucleo-icons.css
│   └── nucleo-svg.css
├── fonts
│   ├── FontAwesome.otf
│   ├── fontawesome-webfont.eot
│   ├── fontawesome-webfont.svg
│   ├── fontawesome-webfont.ttf
│   ├── fontawesome-webfont.woff
│   ├── fontawesome-webfont.woff2
│   ├── nucleo-icons.eot
│   ├── nucleo-icons.svg
│   ├── nucleo-icons.ttf
│   ├── nucleo-icons.woff
│   └── nucleo-icons.woff2
└── js
users
├── __init__.py
├── __pycache__
├── admin.py
├── apps.py
├── migrations
├── models.py
├── templates
│   └── users
│       └── login.html
├── tests.py
├── urls.py
└── views.py