"""This module is for User model."""

from src.utils.logger import Logger
log = Logger(__name__)


class User:
    """This class is for User model."""

    def __init__(
                    self,
                    firstname: str,
                    lastname: str,
                    password: str,
                    pseudo: str) -> None:
        """Initialize a User object.

        Args:
            firstname (str): The firstname of the user.
            lastname (str): The lastname of the user.
            password (str): The lastname of the user.
            pseudo (str): The pseudo of the user.
        """
        # id will be set by the database mongo db
        self.id = None
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.pseudo = pseudo

    def update(self, firstname, lastname, pseudo, password) -> None:
        """Updade User infos."""
        self.firstname = firstname
        self.lastname = lastname
        self.pasword = password
        self.pseudo = pseudo
        log.log_debug(f"User {self.id} is modified")

    def to_dict(self) -> dict:
        """Convert the user to a dictionary."""
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "pseudo": self.pseudo,
        }

    @classmethod
    def from_dict(cls, user_dict: dict):
        """Create a User object from a dictionary.

        Args:
            user_dict (dict): The dictionary of user information.

        Returns:
            User: The User object created from the dictionary.
        """
        user = cls(user_dict["firstname"],
                   user_dict["lastname"],
                   user_dict["pseudo"])
        user.id = user_dict["_id"]
        return user
