import os
import shutil
import datetime
import time
inicio = time.time()
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

    ruta_precios = f'C:\\Temp\\Punto B\\Controles\\{yyyy}\\{mm_number} {mm_palabra}\\{dd}\\Precios'
    subcarpetas = sorted([d for d in os.listdir(ruta_precios) if os.path.isdir(os.path.join(ruta_precios, d)) and len(d) == 4 and d.isdigit()])

    for subcarpeta in subcarpetas:
        # Calcular la fecha yyyymmdd para cada subcarpeta
        dia_subcarpeta = datetime.datetime.strptime(f"{yyyy}{subcarpeta}", '%Y%d%m')
        yyyymmdd_subcarpeta = dia_subcarpeta.strftime('%Y%m%d')

        ruta_origen = os.path.join(ruta_precios, subcarpeta, 'Archivos Originales')
        procesar_archivos_genericos(ruta_origen, yyyymmdd_subcarpeta, subcarpeta == subcarpetas[-1])

# Función para procesar archivos de lunes a jueves
def procesar_archivos_semana(fecha):
    yyyy = fecha.strftime('%Y')
    mm_number = fecha.strftime('%m')
    mm_palabra = meses_es[mm_number]
    dd = fecha.strftime('%d')
    yyyymmdd = fecha.strftime('%Y%m%d')
    ruta_origen = f'C:\Temp\Punto B\Controles\{yyyy}\{mm_number} {mm_palabra}\{dd}\Precios\Archivos Originales'

    procesar_archivos_genericos(ruta_origen, yyyymmdd,True)

# Función genérica para copiar y renombrar archivos
def procesar_archivos_genericos(ruta_origen, yyyymmdd, es_ultimo_dia=False):
    ruta_destino = r'C:\Users\USER\Desktop\Punto A'

    nombres_archivos = {
        '900408537_cva_alloc': f'{yyyymmdd}_cvadva.txt',
        'Fwd_USDCOP_Diaria': f'{yyyymmdd}_Fwd_USDCOP.txt',
        'Matriz_TC': f'{yyyymmdd}_Mat_Monedas.txt',
        'SwapCC_IBR_Diaria': f'{yyyymmdd}_LIBORCOP.txt',
        'SB': f'{yyyymmdd}_Betas.txt',
        'SP': f'{yyyymmdd}_Precios.txt',
        'SV': f'{yyyymmdd}_Tasas.txt'
    }

    # Función para cambiar el nombre de los archivos .001
    def cambiar_nombre_archivo_001(nombre_original):
        tipo = nombre_original[:2]
        if tipo in ['SB', 'SP', 'SV']:
            nuevo_nombre = nombres_archivos[tipo]
            return nuevo_nombre
        return None


    for archivo in os.listdir(ruta_origen):
            nombre_sin_extension, extension = os.path.splitext(archivo)
            
            if extension == '.txt':
                # Extraer la parte del nombre sin la fecha
                nombre_base = '_'.join(nombre_sin_extension.split('_')[:-1])
                if nombre_base in nombres_archivos:
                    nuevo_nombre = nombres_archivos[nombre_base]
                    ruta_archivo_origen = os.path.join(ruta_origen, archivo)
                    ruta_archivo_destino = os.path.join(ruta_destino, nuevo_nombre)
                    # Copiar el archivo de origen al destino con el nuevo nombre
                    shutil.copy2(ruta_archivo_origen, ruta_archivo_destino)
                    print(f"{archivo} --> {nuevo_nombre}")
                    print()
                    # Si es Matriz_TC y es el último día, hacer una copia adicional
                    if nombre_base == 'Matriz_TC' and es_ultimo_dia:
                        ruta_archivo_destino_adicional = os.path.join(ruta_destino, 'Mat_Monedas.txt')
                        shutil.copy2(ruta_archivo_origen, ruta_archivo_destino_adicional)
                        print(f"{archivo} --> Mat_Monedas.txt")
                        print()
                else:
                    continue
            elif extension == '.001':
                nuevo_nombre = cambiar_nombre_archivo_001(nombre_sin_extension + extension)
                if nuevo_nombre:
                    nuevo_nombre = nuevo_nombre.replace('.001', '.txt')
                    ruta_archivo_origen = os.path.join(ruta_origen, archivo)
                    ruta_archivo_destino = os.path.join(ruta_destino, nuevo_nombre)
                    # Copiar el archivo de origen al destino con el nuevo nombre
                    shutil.copy2(ruta_archivo_origen, ruta_archivo_destino)
                    print(f"{archivo} --> {nuevo_nombre}")
                    print()
                else:
                    continue
            else:
                continue

# Obtener la fecha actual y determinar el día de la semana
#hoy = datetime.datetime.today()
#print(hoy)

hoy = datetime.datetime(2024, 6, 14)  # Año, Mes, Día
if hoy.weekday() == 4:  # Viernes
    procesar_archivos_vienes(hoy)
    print()
    print("Proceso finalzado, archivos copiados con exito")
    print()
    fin = time.time()
    tiempo_total= (fin-inicio)/60
    print(f"Tiempo total proceso {tiempo_total}")
else:
    procesar_archivos_semana(hoy)
    print()
    print("Proceso finalzado, archivos copiados con exito")
    print()
    fin = time.time()
    tiempo_total= (fin-inicio)/60
    print(f"Tiempo total proceso {tiempo_total}")
