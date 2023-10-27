"""Unit tests for TaskList class."""
import unittest
from unittest.mock import Mock
from src.models.task_list import TaskList
from src.models.task import Task
from src.models.user import User
from src.utils.exceptions import TaskNotFound
import datetime


class TestTaskList(unittest.TestCase):
    """Unit tests for TaskList class."""

    def setUp(self):
        """Initialize variables for tests."""
        self.mock_collection = Mock()
        self.task_list = TaskList("TestWork")
        self.task_list.collection = self.mock_collection
        self.sample_user = User("name user", "last name user",
                                "test_user", "password")
        self.sample_user.id = "user_id_123"
        date = datetime.datetime.now().date()
        self.sample_task = Task("TestTask", "Description", date,
                                "ongoing", "Work", self.sample_user.id)

    def test_add_task(self):
        """Test add_task method."""
        self.mock_collection.insert_one.return_value = Mock(
            inserted_id="task_id_123")
        self.task_list.add_task(self.sample_task, self.sample_user)
        self.mock_collection.insert_one.assert_called_once_with(
            self.sample_task.to_dict())

    def test_get_task(self):
        """Test get_task method."""
        self.mock_collection.find_one.return_value = {
            "_id": "task_id_123",
            "name": "TestTask",
            "description": "Description",
            "creation_date": "2023-10-26",
            "status": "ongoing",
            "category": "TestCategory",
            "user_id": "user_id_123"
        }
        task = self.task_list.get_task(task_id="task_id_123")
        self.assertEqual(task.id, "task_id_123")
        self.assertEqual(task.name, "TestTask")

    def test_get_task_not_found(self):
        """Test get_task method when task is not found."""
        self.mock_collection.find_one.return_value = None
        with self.assertRaises(TaskNotFound):
            self.task_list.get_task("task_id_1233")

    def test_get_tasks(self):
        """Test get_tasks method."""
        self.mock_collection.find.return_value = [
            {
                "_id": "task_id_123",
                "name": "TestTask",
                "description": "Description",
                "creation_date": "2023-10-26",
                "status": "ongoing",
                "category": "TestCategory",
                "user_id": "user_id_123"
            },
            {
                "_id": "task_id_456",
                "name": "TestTask2",
                "description": "Description2",
                "creation_date": "2023-10-26",
                "status": "ongoing",
                "category": "TestCategory",
                "user_id": "user_id_123"
            }
        ]
        tasks = self.task_list.get_tasks(self.sample_user)
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].id, "task_id_123")
        self.assertEqual(tasks[1].id, "task_id_456")

    def test_get_ongoing_task(self):
        """Test get_ongoing_task method."""
        self.mock_collection.find.return_value = [
            {
                "_id": "task_id_123",
                "name": "TestTask",
                "description": "Description",
                "creation_date": "2023-10-26",
                "status": "ongoing",
                "category": "TestCategory",
                "user_id": "user_id_123"
            },
            {
                "_id": "task_id_456",
                "name": "TestTask2",
                "description": "Description2",
                "creation_date": "2023-10-26",
                "status": "ongoing",
                "category": "TestCategory",
                "user_id": "user_id_123"
            }
        ]
        tasks = self.task_list.get_ongoing_task()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].id, "task_id_123")
        self.assertEqual(tasks[1].id, "task_id_456")

    def test_complete_task(self):
        """Test complete_task method."""
        self.mock_collection.update_one.return_value = Mock(
            matched_count=1)
        self.task_list.complete_task("task_id_123", "completed")
        self.mock_collection.update_one.assert_called_once_with(
            {"_id": "task_id_123"},
            {"$set": {"status": "completed"}})

    def test_complete_task_invalid_status(self):
        """Test complete_task method with invalid status."""
        with self.assertRaises(Exception):
            self.task_list.complete_task("task_id_123", "invalid_status")

    def test_update_task(self):
        """Test update_task method."""
        self.mock_collection.update_one.return_value = Mock(
            modified_count=1)
        self.task_list.update_task("task_id_123", self.sample_task)
        self.mock_collection.update_one.assert_called_once_with(
            {"_id": "task_id_123"},
            {"$set": self.sample_task.to_dict()})

    def test_remove_task(self):
        """Test remove_task method."""
        self.mock_collection.delete_one.return_value = Mock(
            deleted_count=1)
        self.task_list.remove_task("task_id_456")
        self.mock_collection.delete_one.assert_called_once_with(
            {"_id": "task_id_456"})


if __name__ == '__main__':
    unittest.main()
