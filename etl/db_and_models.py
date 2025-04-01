from sqlalchemy import create_engine, Column, Integer, String, ForeignKey,DateTime,text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime
from dotenv import load_dotenv
import os

# Carga las variables de entorno desde el archivo .env
load_dotenv()
# Crear una clase base
Base = declarative_base()

user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')


# Crea una conexión al servidor PostgreSQL
engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/')


