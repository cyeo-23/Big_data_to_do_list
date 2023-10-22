"""Module for connection to the MongoDB database.

The module take the mongoDB uri in the .env file
and create a client to the mongoDB database.
"""
import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient

# Charge les variables d'environnement à partir du fichier .env
load_dotenv()

# reccuperer le lien de l'URL atlas dans le fichier d'environment
atlas = os.getenv("atlas_link")


def get_db_connection(uri):
    """Create connection to the database."""
    client = MongoClient(uri)
    return client


client = get_db_connection(atlas)
db = client.get_database()
