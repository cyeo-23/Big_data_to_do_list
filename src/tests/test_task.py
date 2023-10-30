"""Test Task model."""
from models.task import Task
import datetime


def test_task_creation():
    """Test task creation."""
    date = datetime.datetime.now().date()
    task = Task("TestTask", "A simple description", date, "ongoing",
                "Work", "user_id_123")
    assert task.name == "TestTask"
    assert task.description == "A simple description"
    assert task.status == "ongoing"
    assert task.category == "Work"
    assert task.user_id == "user_id_123"
    assert task.creation_date == date
    assert task.id is None


def test_task_to_dict():
    """Test task to dict."""
    date = datetime.datetime.now().date()
    task = Task("TestTask", "A simple description", date, "ongoing",
                "Work", "user_id_123")
    task_dict = task.to_dict()
    assert task_dict["name"] == "TestTask"
    assert task_dict["description"] == "A simple description"
    assert task_dict["creation_date"] == date
    assert task_dict["status"] == "ongoing"
    assert task_dict["category"] == "Work"
    assert task_dict["user_id"] == "user_id_123"
