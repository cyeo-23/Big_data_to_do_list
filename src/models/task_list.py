"""This module is for TaskList model."""
from src.utils.logger import Logger
from src.utils.exceptions import TaskNotFound, InvalidTask, TaskAlreadyExists
from src.config.database_cursor import db
from src.models.task import Task
from src.models.user import User

log = Logger(__name__)

# initialize the database
COLLECTION = "tasks"


class TaskList:
    """This class is for TaskList model."""

    def __init__(self, category_name: str) -> None:
        """Initialize a TaskList object.

        Args:
            category_name (str): The name of the category.
        """
        self.category_name = category_name
        self.collection = db[COLLECTION]

    def add_task(self, task: Task, user: User) -> None:
        """Add a task to the database.

        Args:
            task (Task): The task to add.
            user (User): The user to add.
        """
        try:
            task.user_id = user.id
            result = self.collection.insert_one(task.to_dict())
            task.id = result.inserted_id
            log.log_debug(f"Task {task.id} added to the list.")
        except TaskAlreadyExists as e:
            print(e)
            log.log_error(f"Failed to add task due to error: {str(e)}")

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
                    task_data["category"],
                    task_data["user_id"])
        task.id = task_data['_id']
        return task

    def get_tasks(self, user: User) -> list:
        """Get all tasks from the list.

        Args:
            user (User): The user to add.

        Returns:
            list: list of tasks.
        """
        try:
            tasks = self.collection.find({"user_id": user.id})
            list_tasks = []
            for task in tasks:
                task_object = Task(
                                    task["name"],
                                    task["description"],
                                    task["creation_date"],
                                    task["status"],
                                    task["category"],
                                    task["user_id"])
                task_object.id = task['_id']
                list_tasks.append(task_object)
            return list_tasks
        except TaskNotFound as e:
            print(e)
            log.log_error(f"Failed to get tasks due to error: {str(e)}")

    def get_ongoing_task(self) -> list:
        """Get ongoing tasks list.

        Returns:
            list: list of ongoing tasks.
        """
        try:
            list_tasks = []
            tasks = self.collection.find({"status": "ongoing"})
            for task in tasks:
                task_object = Task(
                                    task["name"],
                                    task["description"],
                                    task["creation_date"],
                                    task["status"],
                                    task["category"],
                                    task["user_id"])
                task_object.id = task['_id']
                list_tasks.append(task_object)
            return list_tasks
        except TaskNotFound as e:
            print(e)
            log.log_error(f"Failed to get tasks due to error: {str(e)}")

    def complete_task(self, task_id: str, status: str) -> None:
        """Update the status of a task.

        Args:
            task_id (str): The ID of the task to update.
            status (str): The status of the task.

        Raises:
            InvalidTaskStatus: if the status is not valid.
        """
        if status not in ["ongoing", "completed"]:
            raise InvalidTask(f"Invalid status {status}.")
        self.collection.update_one(
            {"_id": task_id},
            {"$set": {"status": status}})
        log.log_debug(f"Task {task_id} status updated to {status}.")

    def update_task(self, task_id: str, task: Task) -> None:
        """Update a task.

        Args:
            task_id (str): ID of the task to update.
            task (Task): The task to update.

        Raises:
            TaskNotFound: Exception when task not found.
        """
        result = self.collection.update_one(
            {"_id": task_id},
            {"$set": task.to_dict()})
        if result.modified_count == 0:
            raise TaskNotFound(f"Task with ID {task_id} not found.")
        log.log_debug(f"Task {task_id} updated.")

    def remove_task(self, task_id: str) -> None:
        """Delete task.

        Args:
            id (str): ID of the task to delete.

        Raises:
            TaskNotFound: Exception when task not found.
        """
        result = self.collection.delete_one({"_id": task_id})
        if result.deleted_count == 0:
            raise TaskNotFound(f"Task with ID {task_id} not found.")
        log.log_debug(f"Task {task_id} deleted.")
