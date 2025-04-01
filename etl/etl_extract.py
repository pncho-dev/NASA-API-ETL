import requests


def extract_projects_data(URL:str,initial_date:str):
 
    try:
        response = requests.get(f"{URL}{initial_date}")
        response.raise_for_status()
        return response.json()  
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener datos de la API: {e}")
        return None




