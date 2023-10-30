"""This module is for services model."""
import pymongo
from utils.logger import Logger
from utils.exceptions import UserAlreadyExists, UserNotFound, UserEmptyPassword
from config.database_cursor import db
from models.user import User
import argon2

log = Logger(__name__)

COLLECTION = "users"


class UserServices:
    """This class is for user services model."""

    def __init__(self) -> None:
        """Initialize a userList object.

        Args:
            category_name (str): The name of the category.
            collection_name (str): The name of the collection to use.
        """
        self.collection = db[COLLECTION]
        self.ph = argon2.PasswordHasher()

    def add_user(self, user: User) -> User:
        """Add a user to the database.

        Args:
            user (User): The user to add.
        """
        # check if user pseudo already exists
        if user.password != "" or user.password is not None:
            try:
                existing_user = self.collection.find_one(
                    {"pseudo": user.pseudo})
                if existing_user:
                    raise UserAlreadyExists(
                        f"A user with pseudo{user.pseudo} exists."
                        )
                user.password = self.ph.hash(user.password)
                result = self.collection.insert_one(user.to_dict())
                user.id = result.inserted_id
                log.log_debug(f"user {user.pseudo} added to the database.")
                return user
            except Exception as e:
                log.log_error(f"Une erreur inattendue s'est produite: {e}")
        else:
            raise UserEmptyPassword("The password is empty.")

    def connect_user(self, pseudo: str, password: str) -> User:
        """Connect a user to the app.

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
            is_verified = self.ph.verify(user_found["password"], password)
            if not user_found or not is_verified:
                raise UserNotFound("""Aucun utilisateur trouvé avec ses crédentials.
                                   Veuillez verifier svp vos accès""")
            else:
                user = User.from_dict(user_found)
                return user
        except Exception as e:
            log.log_error(f"Une erreur inattendue s'est produite: {e}")

    def update_user(self, user: User) -> None:
        """Update the user infos.

        Args:
            user (User): the user object to update.

        Raises:
            Mongo Exception: if pymongo find exception.
        """
        if user.password != "" or user.password is not None:
            try:
                user.password = self.ph.hash(user.password)
                result = self.collection.update_one(
                    {"_id": user.id},
                    {"$set": user.to_dict()})
                if result.modified_count > 0:
                    log.log_debug(f"user {user.id} modified.")
                else:
                    log.log_debug(f"user {user.id} not found.")

                log.log_debug(f"user {user.pseudo} updated.")
            except Exception as e:
                log.log_error(f"Une erreur inattendue s'est produite: {e}")
        else:
            raise UserEmptyPassword("The password is empty.")
