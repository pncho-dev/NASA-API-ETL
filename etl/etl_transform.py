import pandas as pd  # Se importa pandas para manipular los datos en DataFrames
import json  # Se importa json para manejar archivos JSON

def process_project_data(raw_data):
    """
    Procesa los datos crudos del proyecto para convertirlos en DataFrames.
    """
    # Extraer la información de los proyectos y organizarla en una lista de diccionarios
    project_info = [{
        "projectId": project["projectId"],  # ID del proyecto
        "title": project["project"]["title"],  # Título del proyecto
        "startDate": project["project"]["startDate"],  # Fecha de inicio del proyecto
        "startYear": project["project"]["startYear"],  # Año de inicio
        "startMonth": project["project"]["startMonth"],  # Mes de inicio
        "endDate": project["project"]["endDate"],  # Fecha de finalización
        "endYear": project["project"]["endYear"],  # Año de finalización
        "endMonth": project["project"]["endMonth"],  # Mes de finalización
        "description": project["project"]["description"],  # Descripción del proyecto
        "benefits": project["project"]["benefits"],  # Beneficios del proyecto
        "releaseStatus": project["project"]["releaseStatus"],  # Estado de lanzamiento
        "status": project["project"]["status"],  # Estado del proyecto
        "viewCount": project["project"]["viewCount"],  # Contador de vistas del proyecto
        'destinationType': ', '.join(project["project"]['destinationType']) if 'destinationType' in project["project"].keys() else None,  # Tipo de destino del proyecto (si existe)
        "trlBegin": project["project"]["trlBegin"],  # TRL al inicio del proyecto
        "trlCurrent": project["project"]["trlCurrent"],  # TRL actual del proyecto
        "trlEnd": project["project"]["trlEnd"],  # TRL al final del proyecto
        "favorited": project["project"]["favorited"],  # Indicador de si el proyecto está marcado como favorito
        "detailedFunding": project["project"]["detailedFunding"]  # Financiamiento detallado del proyecto
    } for project in raw_data]

    # Convertir la lista de diccionarios en un DataFrame de pandas
    project_df = pd.DataFrame(project_info)

    # Extraer los contactos con el rol de "Investigator" en un DataFrame separado
    contact_info = []
    for project in raw_data:
        for contact in project["project"]["projectContacts"]:
            if "Investigator" in contact["projectContactRole"]:  # Filtrar solo los contactos con el rol de "Investigator"
                contact_info.append({
                    "contactId": contact["contactId"],  # ID de contacto
                    "firstName": contact["firstName"],  # Primer nombre del contacto
                    "lastName": contact["lastName"],  # Apellido del contacto
                    "fullName": contact["fullName"],  # Nombre completo del contacto
                    "email": contact["email"],  # Correo electrónico del contacto
                    "projectContactRole": contact["projectContactRole"],  # Rol del contacto en el proyecto
                    "projectId": project["projectId"]  # ID del proyecto asociado al contacto
                })

    # Convertir la lista de contactos en un DataFrame de pandas
    contact_df = pd.DataFrame(contact_info)
    
    return project_df, contact_df  # Devolver los DataFrames de proyectos y contactos

def transform_data(json_file_path):
    """
    Carga los datos crudos desde un archivo JSON y los procesa.
    """
    # Cargar los datos desde el archivo JSON
    with open(json_file_path, 'r') as f:
        raw_data = json.load(f)
    
    # Procesar los datos para convertirlos en DataFrames
    project_df, contact_df = process_project_data(raw_data)
    
    print("DataFrames de proyectos y contactos creados.")

    return project_df, contact_df  # Devolver los DataFrames procesados
