"""This module is for TaskList model."""
from src.utils.logger import Logger
from src.utils.exceptions import TaskNotFound, InvalidTask, TaskAlreadyExists
from src.config.database_cursor import db
from src.models.task import Task

log = Logger(__name__)


class TaskList:
    """This class is for TaskList model."""

    def __init__(self, category_name: str, collection_name: str) -> None:
        """Initialize a TaskList object.

        Args:
            category_name (str): The name of the category.
            collection (str, optional): The name of the collection to use.
        """
        self.category_name = category_name
        self.collection = db[collection_name]

    def add_task(self, task: Task) -> None:
        """Add a task to the database.

        Args:
            task (Task): The task to add.
        """
        if not isinstance(task, Task):
            raise InvalidTask("Invalid task.")

        # check if task already exists
        existing_task = self.collection.find_one({"id": task.id})
        if existing_task:
            raise TaskAlreadyExists(f"A task with ID {task.id}) exists.")

        result = self.collection.insert_one(task.to_dict())
        task.id = result.inserted_id
        log.log_debug(f"Task {task.id} added to the list.")

    def get_task(self, task_id: str) -> Task:
        """Get a task from the database.

        Args:
            task_id (str): The ID of the task.

        Raises:
            TaskNotFound: Exception when task not found.

        Returns:
            Task: Return a task
        """
        task_data = self.collection.find_one({"_id": task_id})
        if not task_data:
            raise TaskNotFound(f"Task with ID {task_id} not found.")
        task = Task(task_data["name"],
                    task_data["description"],
                    task_data["creation_date"],
                    task_data["status"],
                    task_data["category"])
        task.id = task_data['_id']
        return task

    def get_tasks(self) -> list:
        """Get all tasks from the list."""
        tasks = self.collection.find()
        return [Task(
                        task["name"],
                        task["description"],
                        task["creation_date"],
                        task["status"],
                        task["category"]) for task in tasks]

    def get_ongoing_task(self) -> list:
        """Get ongoing tasks list.

        Returns:
            list: list of ongoing tasks.
        """
        tasks = self.collection.find({"status": "ongoing"})
        return [Task(
                        task["name"],
                        task["description"],
                        task["creation_date"],
                        task["status"],
                        task["category"]) for task in tasks]

    def complete_task(self, task_id: str, status: str) -> None:
        """Update the status of a task.

        Args:
            task_id (str): _description_
            status (str): _description_

        Raises:
            InvalidTaskStatus: if the status is not valid.
        """
        if status not in ["ongoing", "completed"]:
            raise InvalidTask(f"Invalid status {status}.")
        self.collection.update_one(
            {"_id": task_id},
            {"$set": {"status": status}})
        log.log_debug(f"Task {task_id} status updated to {status}.")

    def remove_task(self, task_id: str) -> None:
        """Delete task.

        Args:
            id (str): ID of the task to delete.

        Raises:
            TaskNotFound: Exception when task not found.
        """
        result = self.collection.delete_one({"task_id": task_id})
        if result.deleted_count == 0:
            raise TaskNotFound(f"Task with ID {task_id} not found.")
        log.log_debug(f"Task {task_id} deleted.")
