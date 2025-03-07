# -*- coding: utf-8 -*-
"""mANIPULACION DE DATOS.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sgAi47HWuKe4JxTpQNiQ-7Q0ahp2fKMG
"""

from google.colab import files
import pandas as pd

def procesar_archivo():
    # Paso 1: Subir archivo .txt
    print("Por favor, sube un archivo .txt")
    uploaded = files.upload()

    # Obtener el nombre del archivo subido
    for filename in uploaded.keys():
        archivo_path = filename

    try:
        # Leer el archivo
        with open(archivo_path, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
         # Paso 2: Solicitar la palabra a buscar
        palabra_buscar = input("Ingresa la palabra a buscar: ")
        veces_encontrada = contenido.lower().count(palabra_buscar.lower())
        if veces_encontrada > 0:
            print(f"La palabra '{palabra_buscar}' se encontró {veces_encontrada} veces.")
        else:
            print(f"La palabra '{palabra_buscar}' no se encontró en el archivo.")

        # Paso 3: Solicitar la palabra para reemplazar
        palabra_reemplazar = input("Ingresa la palabra para reemplazar: ")
        contenido_modificado = contenido.replace(palabra_buscar, palabra_reemplazar)

        with open(archivo_path, 'w', encoding='utf-8') as archivo:
            archivo.write(contenido_modificado)
        print(f"Se ha reemplazado '{palabra_buscar}' por '{palabra_reemplazar}' en el archivo.")
        files.download(archivo_path)
        # Mostrar contenido y permitir agregar más información
        print("Contenido actual del archivo:")
        print(contenido)
        nuevo_contenido = input("Ingresa más contenido relacionado al mismo tema:\n")

        with open(archivo_path, 'a', encoding='utf-8') as archivo:
            archivo.write("\n" + nuevo_contenido)

        print("Se ha agregado el nuevo contenido al archivo.")
        # Leer nuevamente el archivo para procesar datos
        with open(archivo_path, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()

        # Extraer tabla de datos
        datos = []
        for linea in lineas:
            if '|' in linea and not linea.startswith('| -'):
                columnas = [x.strip() for x in linea.split('|') if x.strip()]
                if len(columnas) == 4:
                    try:
                        datos.append([columnas[0], float(columnas[1]), float(columnas[2]), float(columnas[3])])
                    except ValueError:
                        continue

        # Convertir a DataFrame
        df = pd.DataFrame(datos, columns=['Lenguaje', 'Popularidad', 'Proyectos', 'Crecimiento'])
        print("Datos extraídos:")
        print(df)

        # Pedir operación matemática
        operacion = input("Elige una operación matemática (suma, resta, multiplicación): ").strip().lower()

        if operacion in ['suma', 'resta', 'multiplicacion']:
            if operacion == 'suma':
                df['Resultado'] = df['Popularidad'] + df['Crecimiento']
            elif operacion == 'resta':
                df['Resultado'] = df['Popularidad'] - df['Crecimiento']
            elif operacion == 'multiplicacion':
                df['Resultado'] = df['Popularidad'] * df['Crecimiento']

            # Guardar resultados en operaciones.txt
            with open("operaciones.txt", 'w', encoding='utf-8') as archivo:
                archivo.write(df.to_string(index=False))
            files.download("operaciones.txt")
            print("Operación realizada y guardada en operaciones.txt")
        else:
            print("Operación no válida.")

        # Copiar todo en resultado.txt
        with open("resultado.txt", 'w', encoding='utf-8') as archivo:
            archivo.write(contenido + "\n" + nuevo_contenido + "\n\nResultados de la operación:\n")
            archivo.write(df.to_string(index=False))
        files.download("resultado.txt")
        print("Todo el contenido ha sido guardado en resultado.txt")

    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejecutar la función
procesar_archivo()