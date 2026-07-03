import shelve
import os
from dotenv import load_dotenv

load_dotenv()  # Cargar variables de entorno desde el archivo .env

database_name = os.getenv("DATABASE_NAME", "default_db")  # Nombre del archivo de base de datos, con valor por defecto

def obtener_siguiente_codigo(archivo_db=database_name):
    # Abrimos el archivo de shelve
    with shelve.open(archivo_db) as db:
        
        if "contador_id" not in db:
            db["contador_id"] = 148
            
        id_actual = db["contador_id"]
        
        id_formateado = f"{id_actual:08d}"
        
        db["contador_id"] = id_actual + 1
        
        return id_formateado
    
def set_codigo(archivo_db=database_name, nuevo_codigo=0):
    with shelve.open(archivo_db) as db:
        db["contador_id"] = nuevo_codigo
