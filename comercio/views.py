from django.shortcuts import render
from .models import PermisoMunicipal

def index(request):
    return render(request, 'comercio/index.html')

def resultado_permisos(request):
    # 1. Obtenemos lo que el usuario seleccionó en el formulario
    comuna = request.GET.get('comuna')
    rubro = request.GET.get('rubro')

    # 2. Partimos cargando todos los permisos de la base de datos
    permisos = PermisoMunicipal.objects.all()

    # 3. Si el usuario eligió una comuna, filtramos la lista
    if comuna:
        permisos = permisos.filter(comuna=comuna)

    # 4. Si el usuario eligió un rubro, filtramos la lista también
    if rubro:
        permisos = permisos.filter(rubro=rubro)

    # 5. Creamos una bolsita simple con los datos para mandarlos al HTML
    datos = {
        'permisos': permisos
    }

    # 6. Devolvemos la página con los resultados
    return render(request, 'comercio/resultado.html', datos)

    # 6. Devolvemos la página con los resultados
    return render(request, 'comercio/resultado.html', datos)