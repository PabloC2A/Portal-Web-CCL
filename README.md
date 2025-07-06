# Portal-Web-CCL

**Portal-Web-CCL** es una aplicación web desarrollada con **Django** para gestionar funcionalidades propias de la Cámara de Comercio de Loja.

---

## 📋 Contenido

- [Requisitos previos](#-requisitos-previos)
- [Instalación](#-instalación)
- [Ejecución](#-ejecución)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Contribuciones](#-contribuciones)

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
├── config/                # Configuraciones globales del proyecto Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/                  # Aplicación para la gestion de lading page
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

## 🤝 Contribuciones

1. Realiza un fork del repositorio
2. Crea una rama: `git checkout -b feature/nombre-del-feature`
3. Realiza cambios y haz commit
4. Sube tu rama: `git push origin feature/nombre-del-feature`
5. Abre un Pull Request con descripción clara

---
