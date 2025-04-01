import pandas as pd
import json

def process_project_data(raw_data):
    """
    Procesa los datos crudos del proyecto para convertirlos en DataFrames.
    """
    # Extraer la información de los proyectos en un DataFrame
    project_info = [{
        "projectId": project["projectId"],
        "title": project["project"]["title"],
        "startDate": project["project"]["startDate"],
        "startYear": project["project"]["startYear"],
        "startMonth": project["project"]["startMonth"],
        "endDate": project["project"]["endDate"],
        "endYear": project["project"]["endYear"],
        "endMonth": project["project"]["endMonth"],
        "description": project["project"]["description"],
        "benefits": project["project"]["benefits"],
        "releaseStatus": project["project"]["releaseStatus"],
        "status": project["project"]["status"],
        "viewCount": project["project"]["viewCount"],
        'destinationType': ', '.join(project["project"]['destinationType']) if 'destinationType' in project["project"].keys() else None,
        "trlBegin": project["project"]["trlBegin"],
        "trlCurrent": project["project"]["trlCurrent"],
        "trlEnd": project["project"]["trlEnd"],
        "favorited": project["project"]["favorited"],
        "detailedFunding": project["project"]["detailedFunding"]
    } for project in raw_data]

    project_df = pd.DataFrame(project_info)

    # Extraer los contactos con "Investigator" en el rol en un DataFrame separado
    contact_info = []
    for project in raw_data:
        for contact in project["project"]["projectContacts"]:
            if "Investigator" in contact["projectContactRole"]:
                contact_info.append({
                    "contactId": contact["contactId"],
                    "firstName": contact["firstName"],
                    "lastName": contact["lastName"],
                    "fullName": contact["fullName"],
                    "email": contact["email"],
                    "projectContactRole": contact["projectContactRole"],
                    "projectId": project["projectId"]
                })

    contact_df = pd.DataFrame(contact_info)
    
    return project_df, contact_df

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

    return  project_df, contact_df
    
    
