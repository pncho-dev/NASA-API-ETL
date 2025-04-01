from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime
from dotenv import load_dotenv
import os

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Crear una clase base
Base = declarative_base()

# Cargar las variables de entorno de la base de datos
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')

# Crea una conexión al servidor PostgreSQL
engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db_name}')

# Definir el modelo para Proyectos
class Project(Base):
    __tablename__ = 'project'
    
    project_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    start_date = Column(DateTime)
    start_year = Column(Integer)
    start_month = Column(Integer)
    end_date = Column(DateTime)
    end_year = Column(Integer)
    end_month = Column(Integer)
    description = Column(Text)
    benefits = Column(Text)
    release_status = Column(String)
    status = Column(String)
    view_count = Column(Integer)
    destination_type = Column(String)
    trl_begin = Column(Integer)
    trl_current = Column(Integer)
    trl_end = Column(Integer)
    favorited = Column(Boolean)
    detailed_funding = Column(Boolean)
    
    # Relación con la tabla de investigadores (muchos a muchos)
    investigators = relationship("Investigator", secondary="project_investigator", back_populates="projects")

# Definir el modelo para Investigadores
class Investigator(Base):
    __tablename__ = 'investigator'
    
    contact_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    full_name = Column(String)
    email = Column(String)
    project_contact_role = Column(String)
    
    # Relación con la tabla de proyectos (muchos a muchos)
    projects = relationship("Project", secondary="project_investigator", back_populates="investigators")

# Tabla intermedia para la relación muchos a muchos entre proyectos e investigadores
class ProjectInvestigator(Base):
    __tablename__ = 'project_investigator'
    
    project_id = Column(Integer, ForeignKey('project.project_id', ondelete="CASCADE"), primary_key=True)
    investigator_id = Column(Integer, ForeignKey('investigator.contact_id', ondelete="CASCADE"), primary_key=True)
    
    # Relación con las tablas de proyectos e investigadores
    project = relationship("Project", back_populates="investigators")
    investigator = relationship("Investigator", back_populates="projects")

def create_tables(user, password, host, port, db_name):
    # Conectar a la base de datos con las credenciales
    engine_db = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db_name}')
    
    # Crear las tablas definidas en Base
    Base.metadata.create_all(engine_db)  

if __name__ == '__main__':
    # Llamamos a la función para crear las tablas
    create_tables(user, password, host, port, db_name)
