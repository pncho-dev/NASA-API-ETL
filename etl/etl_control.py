import os
import datetime
import json
from etl_extract import extract_projects_data


# Definición de variables para extracción
initial_date = "2024-01-01"
NASA_API_URL = "https://techport.nasa.gov/api/projects?updatedSince="


def main():
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    bronze_file_path = f"../data/bronze/nasa_projects_{timestamp}.json"
    
    print("Extrayendo datos de todos los proyectos desde la API...")
    raw_data = extract_projects_data(NASA_API_URL, initial_date)
    if raw_data is None:
        print("Error al obtener los datos. Terminando ejecución.")
        return
    
    os.makedirs("bronze_data", exist_ok=True)
    with open(bronze_file_path, 'w') as f:
        json.dump(raw_data, f)
    print(f"Datos guardados en {bronze_file_path}.")
    

if __name__ == "__main__":
    main()
