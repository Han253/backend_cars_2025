# 🚗 Tienda de Carros Usados - Aplicación Web (SPA)

Este proyecto es una aplicación web de una sola página (SPA) para la venta y compra de carros usados. Utiliza Django REST Framework como backend (API RESTful) y React para la interfaz de usuario.

## 🔧 Tecnologías utilizadas

### Backend
- [Python 3.11+](https://www.python.org/)
- [Django 5.2](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [django-cors-headers](https://pypi.org/project/django-cors-headers/)
- [django-filter](https://pypi.org/project/django-filter/)
- [drf-yasg (Swagger)](https://github.com/axnsan12/drf-yasg)
- [Pillow](https://pypi.org/project/Pillow/)
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/)

---

## 🚀 Cómo clonar y ejecutar el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/tienda-carros-usados.git
cd tienda-carros-usados 
```

### 2. Crear y Activar el Entorno Virtual
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias del backend
```bash
pip install -r requirements.txt
```

## 🗂️ Estructura del Proyecto
```bash
backend/
│
├── cars/                  # App principal
├── backend/               # Configuración de Django
├── manage.py              # Comando principal de Django
└── requirements.txt       # Dependencias
```