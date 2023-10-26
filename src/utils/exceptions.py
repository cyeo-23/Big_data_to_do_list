"""Custom exceptions for the project."""


class TaskNotFound(Exception):
    """Exception raised when a task is not found in the database.

    Attributes:
        Exception (_type_): _description_
    """

    pass


class InvalidTask(Exception):
    """Exception raised when a task attribute is invalid.

    Args:
        Exception (_type_): _description_
    """

    pass


class UserNotFound(Exception):
    """Exception raised when a user is not found in the database.

    Args:
        Exception (_type_): _description_
    """

    pass


class UserAlreadyExists(Exception):
    """Exception raised when trying to add a user that already exists.

    Args:
        Exception (_type_): _description_
    """

    pass


class InvalidUser(Exception):
    """Exception raised when a user attribute is invalid.

    Args:
        Exception (_type_): _description_
    """

    pass


class TaskAlreadyExists(Exception):
    """Exception raised when adding a task already exists.

    Args:
        Exception (_type_): _description_
    """

    pass
