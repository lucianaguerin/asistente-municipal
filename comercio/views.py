import requests
from django.shortcuts import render, redirect
from .models import PermisoMunicipal, IndicadorEconomico

def index(request):
    return render(request, 'comercio/index.html')

def resultado_permisos(request):

    comuna = request.GET.get('comuna')
    actividad = request.GET.get('actividad')
    espacio = request.GET.get('espacio')

    # Sin comuna no hay consulta posible: volvemos al cuestionario
    if not comuna:
        return redirect('index')

    # Traduce las respuestas del cuestionario al rubro guardado en la base de datos
    rubro = None
    if actividad in ('Gastronomía y Alimentos', 'alimentos'):
        rubro = 'Gastronomía y Alimentos'
    elif actividad in ('Servicios Profesionales', 'servicios'):
        rubro = 'Servicios Profesionales'
    elif actividad in ('Comercio', 'productos'):
        if espacio == 'calle':
            rubro = 'Comercio en Vía Pública'
        elif espacio == 'local':
            rubro = 'Comercio Minorista (local)'

    resultados = PermisoMunicipal.objects.filter(comuna=comuna)
    if rubro:
        resultados = resultados.filter(rubro=rubro)

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