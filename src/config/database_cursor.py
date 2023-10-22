"""This module start a connection to the MongoDB
database and instantiate the client and db object"""
import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient

# Charge les variables d'environnement à partir du fichier .env
load_dotenv()

# reccuperer le lien de l'URL atlas dans le fichier d'environment
atlas = os.getenv("atlas_link")


def get_db_connection(uri):
    """This fuction create connection to the MongoDB database"""
    client = MongoClient(uri)
    return client


client = get_db_connection(atlas)
db = client.get_database()
