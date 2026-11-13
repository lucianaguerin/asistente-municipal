import requests
from django.shortcuts import render
from .models import PermisoMunicipal, IndicadorEconomico

def resultado_permisos(request):
    comuna = request.GET.get('comuna', '')
    actividad = request.GET.get('actividad', '')
    espacio = request.GET.get('espacio', '')

    # Partimos consultando todos los registros de los 41 permisos
    resultados = PermisoMunicipal.objects.all()

    # Filtramos por comuna si se seleccionó
    if comuna:
        resultados = resultados.filter(comuna__icontains=comuna)

    # Filtramos según la actividad elegida en el cuestionario
    if actividad == 'Gastronomía y Alimentos':
        resultados = resultados.filter(rubro__icontains='Gastronomía')
    elif actividad == 'Servicios Profesionales':
        resultados = resultados.filter(rubro__icontains='Servicios Profesionales')
    elif actividad == 'Comercio':
        if espacio == 'local':
            resultados = resultados.filter(rubro__icontains='Comercio Minorista')
        elif espacio == 'calle':
            resultados = resultados.filter(rubro__icontains='Comercio en Vía Pública')
        else:
            resultados = resultados.filter(rubro__icontains='Comercio')

    return render(request, 'comercio/resultado.html', {'resultados': resultados})

def index(request):
    return render(request, 'comercio/index.html')

def resultado_permisos(request):

    comuna = request.GET.get('comuna')
    actividad = request.GET.get('actividad') # Ej: 'alimentos', 'servicios', 'productos'
    espacio = request.GET.get('espacio')     # Ej: 'local', 'calle'
    

    rubro = None
    if actividad == 'alimentos':
        rubro = 'Gastronomía y Alimentos'
    elif actividad == 'servicios':
        rubro = 'Servicios Profesionales'
    elif actividad == 'productos' and espacio == 'calle':
        rubro = 'Comercio en Vía Pública'
    elif actividad == 'productos' and espacio == 'local':
        rubro = 'Comercio Minorista'
    permisos = PermisoMunicipal.objects.filter(
    comuna__icontains=comuna,
    rubro__icontains=rubro
    ) if rubro else PermisoMunicipal.objects.filter(comuna__icontains=comuna)

 
    resultados = None
    if comuna and rubro:
        resultados = PermisoMunicipal.objects.filter(comuna=comuna, rubro=rubro)
    elif comuna: 
        resultados = PermisoMunicipal.objects.filter(comuna=comuna)


   # 4. CONEXIÓN A API DEFINITIVA (VALOR-UTM.CL) CON FALLBACK OFFLINE
    valor_utm = None
    conexion_online = False
    
    try:
        # Usamos valor-utm.cl que es exclusiva y NO bloquea a Python
        url = 'https://valor-utm.cl/api/v1/utm/actual.json'
        response = requests.get(url, timeout=10, verify=False)
        
        if response.status_code == 200:
            data = response.json()
            valor_utm = float(data['valor']) # Esta API entrega el valor directo
            
            # Guardamos el valor oficial en la base de datos
            IndicadorEconomico.objects.update_or_create(
                nombre='UTM',
                defaults={'valor': valor_utm}
            )
            conexion_online = True
        else:
            raise Exception(f"Error HTTP: {response.status_code}")
            
    except Exception as e:
        print(f"ATENCIÓN - Error de API: {e}") 
        indicador = IndicadorEconomico.objects.filter(nombre='UTM').first()
        if indicador:
            valor_utm = indicador.valor
        else:
            # Salvavidas con el valor oficial de Noviembre 2026
            valor_utm = 72440.0 
        conexion_online = False

    context = {
        'permisos': resultados,
        'comuna': comuna,
        'rubro_detectado': rubro,
        'valor_utm': valor_utm,
        'conexion_online': conexion_online,
    }
    return render(request, 'comercio/resultado.html', context)