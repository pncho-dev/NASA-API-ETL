import os  # Se importa os para interactuar con el sistema de archivos
import datetime  # Se importa datetime para trabajar con fechas y horas
from dotenv import load_dotenv  # Se importa load_dotenv para cargar variables de entorno desde un archivo .env
import json  # Se importa json para manipular archivos JSON
from etl_extract import extract_projects_investigators_data  # Se importa la función para extraer datos de la API
from etl_transform import transform_data  # Se importa la función para transformar los datos crudos en DataFrames

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Definición de variables para la extracción de datos
initial_date = "2025-03-28"  # Fecha inicial para filtrar proyectos actualizados desde esta fecha
API_URL = os.getenv('API_URL')  # Cargar la URL de la API desde las variables de entorno

def main():
    # Definir la ruta donde se guardarán los datos crudos extraídos
    projects_raw_file_path = f"../data/nasa_projects.json"
    
    # Crear el directorio para guardar los datos si no existe
    os.makedirs("../data/", exist_ok=True)
    
    # Llamar a la función de extracción de datos desde la API
    raw_data = extract_projects_investigators_data(API_URL, initial_date)
    
    # Verificar si los datos se obtuvieron correctamente
    if raw_data is None:
        print("Error al obtener los datos. Terminando ejecución.")
        return  # Finaliza la ejecución si no se obtuvieron datos
    
    # Guardar los datos crudos en un archivo JSON
    with open(projects_raw_file_path, 'w') as f:
        json.dump(raw_data, f)  # Escribir los datos crudos en el archivo
    print(f"Datos guardados en {projects_raw_file_path}.")
    
    # Llamar a la función de transformación para convertir los datos en DataFrames
    project_df, contact_df = transform_data(projects_raw_file_path)


# Si el script se ejecuta directamente, llamar a la función main
if __name__ == "__main__":
    main()
