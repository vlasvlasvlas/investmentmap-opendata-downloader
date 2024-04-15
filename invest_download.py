import os
import json
import requests


def descargar_archivo(url, nombre_archivo):
    try:
        print("\n Descargando archivo...", url)

        # remove requests warning
        requests.packages.urllib3.disable_warnings(
            requests.packages.urllib3.exceptions.InsecureRequestWarning
        )

        # Realizar la solicitud de descarga
        response = requests.get(url, timeout=10, verify=False)
        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            # Escribir el contenido de la respuesta en un archivo
            with open(nombre_archivo, "wb") as archivo:
                archivo.write(response.content)
            print(f"Archivo {nombre_archivo} descargado con éxito.")
        else:
            print(
                f"No se pudo descargar el archivo {nombre_archivo}. Código de estado: {response.status_code}"
            )
    except Exception as e:
        print(f"Ocurrió un error al descargar el archivo {nombre_archivo}: {str(e)}")


def descargar_archivos_desde_json(archivo_json):
    try:
        # Cargar el archivo JSON
        with open(archivo_json, "r") as f:
            data = json.load(f)

        # Iterar sobre los datos del JSON
        for entry in data:
            iso2 = entry["iso2"]
            url_descarga = entry["url_descarga"]
            nombre_archivo = iso2 + "_" + entry["nombre_archivo"]

            # Crear la carpeta para el país si no existe
            carpeta_pais = f"./data/{iso2}"
            if not os.path.exists(carpeta_pais):
                os.makedirs(carpeta_pais)

            # Descargar el archivo y guardarlo en la carpeta correspondiente
            descargar_archivo(url_descarga, f"{carpeta_pais}/{nombre_archivo}")
    except Exception as e:
        print(f"Ocurrió un error al procesar el archivo JSON: {str(e)}")


# Ejemplo de uso
if __name__ == "__main__":
    archivo_json = (
        "invest_data.json"  # Nombre del archivo JSON con los enlaces de descarga
    )
    descargar_archivos_desde_json(archivo_json)
