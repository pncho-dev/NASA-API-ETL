import requests  # Se importa la librería requests para hacer solicitudes HTTP

def extract_projects_investigators_data(URL: str, initial_date: str):
    try:
        # Se hace una solicitud GET para obtener los proyectos actualizados desde la fecha dada
        response = requests.get(f"{URL}projects?updatedSince={initial_date}")
        response.raise_for_status()  # Se verifica si la respuesta tiene errores
        
        # Se obtiene la lista de proyectos y el número total de proyectos desde la respuesta JSON
        projects = response.json().get('projects', [])
        number_of_projects = response.json().get('totalCount')
        print(f"Extrayendo datos para un total de {number_of_projects} proyectos...")
        
        # Se crea una lista vacía para almacenar los proyectos detallados
        detailed_projects = []
        
        # Se recorre cada proyecto y se obtiene su información detallada
        for project in projects:
            project_id = project.get("projectId")  # Se obtiene el ID del proyecto
            if project_id:
                # Se obtiene los detalles del proyecto usando su ID
                detailed_project = get_project_details(URL, project_id)
                if detailed_project:
                    # Si se obtienen detalles, se agregan a la lista
                    detailed_projects.append(detailed_project)
        
        return detailed_projects  # Se devuelve la lista con los proyectos detallados
    except requests.exceptions.RequestException as e:
        # Se captura cualquier excepción de solicitud y se imprime el error
        print(f"Error al obtener datos de la API: {e}")
        return None  # En caso de error, se retorna None

def get_project_details(URL: str, project_id: int):
    try:
        # Se construye la URL para obtener los detalles de un proyecto específico
        project_url = f"{URL}projects/{project_id}"
        response = requests.get(project_url)  # Se realiza la solicitud GET
        response.raise_for_status()  # Se verifica si la respuesta tiene errores
        
        return response.json()  # Se retorna la respuesta en formato JSON con los detalles del proyecto
    except requests.exceptions.RequestException as e:
        # Se captura cualquier excepción de solicitud y se imprime el error
        print(f"Error al obtener los detalles del proyecto {project_id}: {e}")
        return None  # En caso de error, se retorna None
