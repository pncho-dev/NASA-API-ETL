import requests


def extract_projects_investigators_data(URL: str, initial_date: str):
    try:
        
        response = requests.get(f"{URL}projects?updatedSince={initial_date}")
        response.raise_for_status()
        
        projects = response.json().get('projects', [])
        number_of_projects = response.json().get('totalCount')
        print(f"Extrayendo datos un total de {number_of_projects} proyectos...")
        # Lista para almacenar los proyectos detallados
        detailed_projects = []
        
        for project in projects:
            project_id = project.get("projectId")
            if project_id:
                detailed_project = get_project_details(URL, project_id)
                if detailed_project:
                    detailed_projects.append(detailed_project)
        
        return detailed_projects
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener datos de la API: {e}")
        return None

def get_project_details(URL: str, project_id: int):
    try:
        
        project_url = f"{URL}projects/{project_id}"
        response = requests.get(project_url)
        response.raise_for_status()
      
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener los detalles del proyecto {project_id}: {e}")
        return None
    
