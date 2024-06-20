import os
import shutil
import datetime

# Diccionario para traducir meses al español
meses_es = {
    '01': 'ENERO', '02': 'FEBRERO', '03': 'MARZO', '04': 'ABRIL', 
    '05': 'MAYO', '06': 'JUNIO', '07': 'JULIO', '08': 'AGOSTO', 
    '09': 'SEPTIEMBRE', '10': 'OCTUBRE', '11': 'NOVIEMBRE', '12': 'DICIEMBRE'
}

# Función para procesar archivos de viernes, incluyendo sábado y domingo (y lunes si es festivo)
def procesar_archivos_vienes(fecha):
    yyyy = fecha.strftime('%Y')
    mm_number = fecha.strftime('%m')
    mm_palabra = meses_es[mm_number]
    dd = fecha.strftime('%d')
    yyyymmdd = fecha.strftime('%Y%m%d')

    ruta_precios = f'Controles Diarios/{yyyy}/Controles KPS/{mm_number} {mm_palabra}/{dd}/Precios'
    subcarpetas = sorted([d for d in os.listdir(ruta_precios) if os.path.isdir(os.path.join(ruta_precios, d)) and len(d) == 4 and d.isdigit()])

    for subcarpeta in subcarpetas:
        ruta_origen = os.path.join(ruta_precios, subcarpeta, 'Archivos Originales')
        procesar_archivos_genericos(ruta_origen, yyyymmdd, subcarpeta == subcarpetas[-1])

# Función para procesar archivos de lunes a jueves
def procesar_archivos_semana(fecha):
    yyyy = fecha.strftime('%Y')
    mm_number = fecha.strftime('%m')
    mm_palabra = meses_es[mm_number]
    dd = fecha.strftime('%d')
    yyyymmdd = fecha.strftime('%Y%m%d')
    ruta_origen = f'Controles Diarios/{yyyy}/Controles KPS/{mm_number} {mm_palabra}/{dd}/Precios/Archivos Originales'

    procesar_archivos_genericos(ruta_origen, yyyymmdd,True)

# Función genérica para copiar y renombrar archivos
def procesar_archivos_genericos(ruta_origen, yyyymmdd, es_ultimo_dia=False):
    ruta_destino = 'Controles Backup/Controles KPS/Archivos Originales'
    os.makedirs(ruta_destino, exist_ok=True)

    nombres_archivos = {
        '900408537_cva_alloc': f'{yyyymmdd}_cvadva.txt',
        'Fwd_USDCOP_Diaria': f'{yyyymmdd}_Fwd_USDCOP.txt',
        'Matriz_TC': f'{yyyymmdd}_Mat_Monedas.txt',
        'SwapCC_IBR_Diaria': f'{yyyymmdd}_LIBORCOP.txt',
        'SB': f'{yyyymmdd}_Betas.txt',
        'SP': f'{yyyymmdd}_Precios.txt',
        'SV': f'{yyyymmdd}_Tasas.txt'
    }

    for archivo in os.listdir(ruta_origen):
        nombre_base, extension = os.path.splitext(archivo)
        nombre_base = '_'.join(nombre_base.split('_')[:-1])
        if nombre_base in nombres_archivos:
            nuevo_nombre = nombres_archivos[nombre_base]
            ruta_archivo_origen = os.path.join(ruta_origen, archivo)
            ruta_archivo_destino = os.path.join(ruta_destino, nuevo_nombre)
            shutil.copy2(ruta_archivo_origen, ruta_archivo_destino)
            if nombre_base == 'Matriz_TC' and es_ultimo_dia:
                ruta_extra = os.path.join(ruta_destino, 'Mat_Monedas.txt')
                shutil.copy2(ruta_archivo_origen, ruta_extra)

# Obtener la fecha actual y determinar el día de la semana
hoy = datetime.datetime.today()
if hoy.weekday() == 4:  # Viernes
    procesar_archivos_vienes(hoy)
else:
    procesar_archivos_semana(hoy)
