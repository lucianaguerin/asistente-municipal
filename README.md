# Asistente Municipal

## 1. Dependencias
- Python 3.10+ (compatible con Python 3.12)
- Django 5.1

## 2. Pasos para ejecutar Django
```bash
# Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar Django y preparar base de datos
pip install django
python manage.py makemigrations
python manage.py migrate

# Iniciar servidor
python manage.py runserver
```
Acceder desde el navegador a: `http://127.0.0.1:8000/`

## 3. Datos para probar la funcionalidad corazón
- **Caso 1 (Búsqueda específica):** Seleccionar Comuna **Viña del Mar** y Rubro **Comercio Minorista**.
- **Caso 2 (Búsqueda general por comuna):** Seleccionar Comuna **Valparaíso** y dejar el Rubro sin seleccionar.
