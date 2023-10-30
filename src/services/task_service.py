"""This module contains the service layer for the task list."""
from datetime import datetime
from models.task import Task
from models.task_list import TaskList
from models.user import User


class TaskService:
    """This class is the service layer for the task list."""

    def __init__(self):
        """Initialize a TaskService object."""
        self.task_list = TaskList("A faire")

    def create_task(self, name, description, user: User, category=None):
        """Create a new task and add it to the task list."""
        date = datetime.now()
        task = Task(name, description, date, status="ongoing",
                    category=category, user_id=user.id)
        self.task_list.add_task(task, user)
        return task

    def fetch_task(self, task_id: str) -> Task:
        """Get a task from the task list."""
        return self.task_list.get_task(task_id)

    def set_task_completed(self, task_id: str) -> None:
        """Complete a task."""
        print("status:", task_id)
        self.task_list.complete_task(task_id, "completed")

    def update_existing_task(self, task_id: str, task: Task) -> None:
        """Update an existing task."""
        self.task_list.update_task(task_id, task)

    def delete_task(self, task_id: str) -> None:
        """Delete a task."""
        self.task_list.remove_task(task_id)

    def fetch_all_tasks_for_user(self, user: User) -> list:
        """Get all tasks for a user."""
        return self.task_list.get_tasks(user)

    def fetch_ongoing_tasks(self) -> list:
        """Get all ongoing tasks."""
        return self.task_list.get_ongoing_task()

    def get_tasks_by_category(self, category: str, user: User) -> list:
        """Get tasks by category for a user."""
        return self.task_list.get_tasks_by_category(category, user)

    def get_categories(self, user: User) -> list:
        """Get all categories."""
        return self.task_list.get_categories(user)
