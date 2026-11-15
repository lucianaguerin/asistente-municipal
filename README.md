# Asistente Municipal

## 1. Dependencias
- Python 3.10+ (compatible con Python 3.12)
- Django 5.1

# 1. Clonar el repositorio
git clone https://github.com/lucianaguerin/asistente-municipal.git
cd asistente-municipal

# 2. Crear y activar un entorno virtual
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Instalar dependencias
pip install django requests

# 4. Iniciar el servidor
python manage.py runserver
