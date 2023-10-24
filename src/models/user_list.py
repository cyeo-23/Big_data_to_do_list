"""This module is for userList model."""
import pymongo
from src.utils.logger import Logger
from src.utils.exceptions import UserAlreadyExists, UserNotFound
from src.config.database_cursor import db
from src.models.user import User

log = Logger(__name__)

COLLECTION = "users"


class UserList:
    """This class is for UserList model."""

    def __init__(self) -> None:
        """Initialize a userList object.

        Args:
            category_name (str): The name of the category.
            collection_name (str): The name of the collection to use.
        """
        self.collection = db[COLLECTION]

    def add_user(self, user: User) -> None:
        """Add a user to the database.

        Args:
            user (User): The user to add.
        """
        # check if user pseudo already exists
        try:
            existing_user = self.collection.find_one({"pseudo": user.pseudo})
            if existing_user:
                raise UserAlreadyExists(
                    f"A user with pseudo{user.pseudo} exists.")

            result = self.collection.insert_one(user.to_dict())
            user.id = result.inserted_id
            log.log_debug(f"user {user.pseudo} added to the database.")
        except pymongo.errors.ConnectionFailure as e:
            log.log_error(f"Erreur de connexion à la BD MongoDB: {e}")
        except pymongo.errors.PyMongoError as e:
            log.log_error(f"Une erreur PyMongo s'est produite: {e}")
        except Exception as e:
            log.log_error(f"Une erreur inattendue s'est produite: {e}")

    def get_user(self, pseudo: str) -> User:
        """Find a user from the database.

        Args:
            pseudo (str): The pseudo of the user.

        Raises:
            UserNotFound: Exception when user not found.
            Mongo Exception: if pymongo find exception.

        Returns:
            user: Return a user
        """
        try:
            user_found = self.collection.find_one({"pseudo": pseudo})
            if not user_found:
                raise UserNotFound(f"user with pseudo {pseudo} not found.")
            user = User.from_dict(user_found)
            return user
        except pymongo.errors.ConnectionFailure as e:
            log.log_error(f"Erreur de connexion à la BD MongoDB: {e}")
        except pymongo.errors.PyMongoError as e:
            log.log_error(f"Une erreur PyMongo s'est produite: {e}")
        except Exception as e:
            log.log_error(f"Une erreur inattendue s'est produite: {e}")

    def update_user(self, user: User) -> None:
        """Update the user infos.

        Args:
            user (User): the user object to update.

        Raises:
            Mongo Exception: if pymongo find exception.
        """
        try:
            result = self.collection.update_one(
                {"_id": user.id},
                {"$set": user.to_dict()})
            if result.modified_count > 0:
                raise pymongo.errors.WriteError("No document matches.")
            else:
                log.log_debug(f"user {user.id} not found.")

            log.log_debug(f"user {user.pseudo} updated.")
        except pymongo.errors.ConnectionFailure as e:
            log.log_error(f"Erreur de connexion à la BD MongoDB: {e}")
        except pymongo.errors.PyMongoError as e:
            log.log_error(f"Une erreur PyMongo s'est produite: {e}")
        except pymongo.errors.WriteError as e:
            log.log_error(f"Une erreur d'écriture s'est produite: {e}")
        except Exception as e:
            log.log_error(f"Une erreur inattendue s'est produite: {e}")

    def remove_user(self, _id: str) -> None:
        """Delete user.

        Args:
            id (str): ID of the user to delete.

        Raises:
            UserNotFound: Exception when user not found.
            Mongo Exception: if pymongo find exception.

        """
        try:
            result = self.collection.delete_one({"user_id": _id})
            if result.deleted_count == 0:
                raise UserNotFound(f"user with ID {_id} not found.")
            log.log_debug(f"user {_id} deleted.")
        except pymongo.errors.ConnectionFailure as e:
            log.log_error(f"Erreur de connexion à la BD MongoDB: {e}")
        except pymongo.errors.PyMongoError as e:
            log.log_error(f"Une erreur PyMongo s'est produite: {e}")
        except pymongo.errors.WriteError as e:
            log.log_error(f"Une erreur d'écriture s'est produite: {e}")
        except Exception as e:
            log.log_error(f"Une erreur inattendue s'est produite: {e}")
