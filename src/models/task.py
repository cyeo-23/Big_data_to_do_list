"""This module is for Task model."""

from datetime import datetime
from src.utils.logger import Logger
log = Logger(__name__)


class Task:
    """This class is for Task model."""

    def __init__(
                    self,
                    name: str,
                    description: str,
                    date: str,
                    status: str,
                    category: str,
                    user_id: str) -> None:
        """Initialize a Task object.

        Args:
            name (str): The name of the task.
            description (str): The description of the task.
            date (str): The creation date of the task.
            status (str): The status of the task.
            category (str): The category of the task.
            user_id (str): The user ID of the task.
        """
        # id will be set by the database mongo db
        self.id = None
        self.name = name
        self.description = description
        date = datetime.now()
        self.creation_date = date
        status = "ongoing"
        self.status = status
        self.category = category
        self.user_id = user_id

    def complete(self) -> None:
        """Mark the task as completed."""
        self.status = "completed"
        log.log_debug(f"Task {self.id} marked as completed.")

    def to_dict(self) -> dict:
        """Convert the task to a dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "creation_date": self.creation_date,
            "status": self.status,
            "category": self.category,
            "user_id": self.user_id
        }
