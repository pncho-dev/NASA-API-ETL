import requests
import json

NASA_API_URL = "https://techport.nasa.gov/api/projects?updatedSince=2024-01-01"
API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJUZWNoUG9ydCIsImV4cCI6MTc0MzU1MjY2NywibmJmIjoxNzQzNDY2MjY3LCJTRVNTSU9OX0lEIjoiaHF6eEVJTzZWOEFqaUE4bVNMcWhucnZlMWpKcWlYMzhVbExzIiwiRklOR0VSUFJJTlRfSEFTSCI6IkU5QUEyQTJEQURCQTZFNzdDRjk5M0Y4MEFBOTlFRENBMjA1NjcwNTRCNkU2OUIzQkJFMjE1NTBCRjA4MjcwRTgifQ.VQxRxkKL_Nqb61dwCvxxo_dZeV2kr8i4E1nDkY18RoQ"  # Sustituir por tu clave API

def extract_data():
 
    try:
        response = requests.get(NASA_API_URL, params=params)
        response.raise_for_status()
        return response.json()  
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener datos de la API: {e}")
        return None



params = {
        'api_key': API_KEY
    
    }

response = requests.get(NASA_API_URL, params=params)
print (response)