# Asistente Municipal

## 1. Dependencias
- Python 3.10+ (compatible con Python 3.12)
- Django 5.1

para abrir:

```bash
git clone https://github.com/lucianaguerin/asistente-municipal.git
cd asistente-municipal
python3 -m venv .venv
source .venv/bin/activate
pip install django requests
python manage.py runserver
```

Luego abre http://127.0.0.1:8000/ en el navegador.

Pégalos de a uno si el primero tarda, o todos juntos si prefieres. Para apagar el servidor, `Ctrl + C`.

Si `pip install django` da error de versión, usa en su lugar:

```bash
pip install "django==5.1.*" requests
```
