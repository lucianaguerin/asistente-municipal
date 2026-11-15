# Asistente Municipal

## Requisitos
- Python 3.10 o superior (https://www.python.org/downloads/)
- Git

## Cómo ejecutarla

**1. Descargar el proyecto**
```bash
git clone https://github.com/lucianaguerin/asistente-municipal.git
cd asistente-municipal
```

**2. Crear y activar un entorno virtual** (créalo tú; no uses la carpeta `venv` si aparece en el repositorio)

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows (PowerShell):
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Windows (CMD):
```bat
python -m venv .venv
.venv\Scripts\activate.bat
```
Si PowerShell bloquea el script, ejecuta una vez: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.

**3. Instalar dependencias**
```bash
pip install -r requirements.txt
```

**4. Iniciar el servidor**
```bash
python manage.py runserver
```
(En macOS/Linux, si `python` no existe, usa `python3`.)

Abre http://127.0.0.1:8000/ en el navegador. Para detener el servidor: `Ctrl + C`.

La base de datos (`db.sqlite3`) ya incluye los 41 permisos, así que no hace falta migrar ni cargar datos. Necesitas conexión a internet para el diseño (Bootstrap) y el valor de la UTM; sin internet la app sigue funcionando con el último valor guardado.

## Panel de administración (opcional)
```bash
python manage.py createsuperuser
```
Luego entra a http://127.0.0.1:8000/admin/ para crear o editar permisos.

## Solución de problemas
- `command not found: python` → usa `python3`.
- `No module named django` → el entorno virtual no está activado o falta el paso 3.
- Error al activar `venv/bin/activate` → esa carpeta venía de otro computador; usa `.venv` como en el paso 2.
