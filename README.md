# Portal-Web-CCL

**Portal-Web-CCL** es una aplicación web desarrollada con **Django** para gestionar funcionalidades propias de una cámara de comercio. Ofrece un menú principal para navegar entre secciones clave como Inicio, Gestiones internas y otras vistas disponibles desde el portal web.

---

## 📋 Contenido

- [Requisitos previos](#-requisitos-previos)
- [Instalación](#-instalación)
- [Ejecución](#-ejecución)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Funcionalidad y menú](#-funcionalidad-y-menú)
- [Uso](#-uso)
- [Contribuciones](#-contribuciones)
- [Licencia](#-licencia)

---

## 🔍 Requisitos previos

Antes de comenzar, asegúrate de tener instalados:

- Python 3.8 o superior
- pip
- virtualenv (opcional pero recomendado)

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
├── config/                # Configuraciones globales del proyecto Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/                  # Aplicación principal del portal
│   ├── migrations/
│   ├── templates/core/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── LICENSE
├── manage.py
└── README.md
```

---

## 🔀 Funcionalidad y menú

### Menú principal

La aplicación cuenta con un menú de navegación que incluye:

- **Inicio**: página principal del sitio
- **Secciones internas**: funcionalidades gestionadas desde la app `core`
- **Contacto / Información institucional**: si está disponible

### Funciones disponibles

- Visualización de templates HTML definidos en `templates/core`
- Vistas gestionadas desde `core/views.py`
- Administración a través de `/admin`

---

## 🧑‍💻 Uso

1. Ejecuta `python manage.py runserver`
2. Abre el navegador en `http://localhost:8000/`
3. Usa el menú para navegar entre las diferentes vistas
4. Accede al panel de administración si tienes credenciales

---

## 🤝 Contribuciones

1. Realiza un fork del repositorio
2. Crea una rama: `git checkout -b feature/nombre-del-feature`
3. Realiza cambios y haz commit
4. Sube tu rama: `git push origin feature/nombre-del-feature`
5. Abre un Pull Request con descripción clara

---

## 📝 Licencia

Este proyecto está bajo la licencia [MIT](LICENSE)

---

> 💡 Este README está basado en la estructura actual del proyecto. Puedes completarlo con detalles adicionales de las vistas, modelos o funcionalidades específicas cuando el desarrollo avance.

