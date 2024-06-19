import os
import shutil
import datetime

# Diccionario para traducir meses al español
meses_es = {
    '01': 'ENERO', '02': 'FEBRERO', '03': 'MARZO', '04': 'ABRIL', 
    '05': 'MAYO', '06': 'JUNIO', '07': 'JULIO', '08': 'AGOSTO', 
    '09': 'SEPTIEMBRE', '10': 'OCTUBRE', '11': 'NOVIEMBRE', '12': 'DICIEMBRE'
}

# Obtener la fecha actual
hoy = datetime.datetime.today()

# Definir el año, mes y día actuales
yyyy = hoy.strftime('%Y')
mm_number = hoy.strftime('%m')
mm_palabra = meses_es[mm_number]
dd = hoy.strftime('%d')

# Formatear la fecha para los nombres de archivo
yyyymmdd = hoy.strftime('%Y%m%d')

# Ruta de origen y destino
ruta_origen = f'Controles Diarios/{yyyy}/Controles KPS/{mm_number} {mm_palabra}/{dd}/Precios/Archivos Originales'
ruta_destino = 'Controles Backup/Controles KPS/Archivos Originales'

# Crear la carpeta de destino si no existe
os.makedirs(ruta_destino, exist_ok=True)

# Diccionario para los nuevos nombres de archivo
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

# Copiar y renombrar archivos
for archivo in os.listdir(ruta_origen):
    nombre_sin_extension, extension = os.path.splitext(archivo)
    
    if extension == '.txt':
        if nombre_sin_extension in nombres_archivos:
            nuevo_nombre = nombres_archivos[nombre_sin_extension]
        else:
            continue
    elif extension == '.001':
        nuevo_nombre = cambiar_nombre_archivo_001(nombre_sin_extension + extension)
        if nuevo_nombre:
            nuevo_nombre = nuevo_nombre.replace('.001', '.txt')
        else:
            continue
    else:
        continue
    
    ruta_archivo_origen = os.path.join(ruta_origen, archivo)
    ruta_archivo_destino = os.path.join(ruta_destino, nuevo_nombre)
    
    # Copiar el archivo de origen al destino con el nuevo nombre
    shutil.copy2(ruta_archivo_origen, ruta_archivo_destino)

print("Archivos copiados y renombrados exitosamente.")
