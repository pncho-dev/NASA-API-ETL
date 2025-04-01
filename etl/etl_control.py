import os
import datetime
from dotenv import load_dotenv
import json
from etl_extract import extract_projects_investigators_data
from etl_transform import transform_data 

# Cargar variables de entorno desde .env
load_dotenv()

# Definición de variables para extracción
initial_date = "2025-03-28"
API_URL = os.getenv('API_URL')

def main():
    
    #timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    projects_raw_file_path = f"../data/nasa_projects.json"
    
    raw_data = extract_projects_investigators_data(API_URL, initial_date)
    if raw_data is None:
        print("Error al obtener los datos. Terminando ejecución.")
        return
    
    os.makedirs("bronze_data", exist_ok=True)
    with open(projects_raw_file_path, 'w') as f:
        json.dump(raw_data, f)
    print(f"Datos guardados en {projects_raw_file_path}.")
    
    project_df, contact_df = transform_data(projects_raw_file_path)

if __name__ == "__main__":
    main()
