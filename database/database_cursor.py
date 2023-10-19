import os
from dotenv import load_dotenv

# Charge les variables d'environnement à partir du fichier .env
load_dotenv()
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Replace the placeholder with your Atlas connection string
uri = os.getenv("atlas_link")

def get_db_connection():
    try:
        client = MongoClient(uri)
        db = client.get_database()
    except Exception as e:
        print(e)
    return db                          
