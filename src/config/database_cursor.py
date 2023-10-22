import os
from dotenv import load_dotenv

# Charge les variables d'environnement à partir du fichier .env
load_dotenv()
from pymongo.mongo_client import MongoClient

# reccuperer le lien de l'URL atlas dans le fichier d'environment
uri = os.getenv("atlas_link")

def get_db_connection():
    client = MongoClient(uri)
    return client                          



client = get_db_connection()
db = client.get_database()
