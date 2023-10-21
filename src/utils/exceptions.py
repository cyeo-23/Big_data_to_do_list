"""Custom exceptions for the project"""

#Exception for task not found
class TaskNotFound(Exception):
    """Exception raised when a task is not found in the database
    
    Args:
        Exception (_type_): _description_
    """
    pass

#Exception for invalid task
class InvalidTaskStatus(Exception):
    """Exception raised when a task attribute is invalid
    
    Args:
        Exception (_type_): _description_
    """
    pass


#Exception for user not found
class UserNotFound(Exception):
    """Exception raised when a user is not found in the database
    
    Args:
        Exception (_type_): _description_
    """
    pass

#Exception when adding an existing user
class UserAlreadyExists(Exception):
    """Exception raised when trying to add a user that already exists
    
    Args:
        Exception (_type_): _description_
    """
    pass

#Exception for invalid user
class InvalidUser(Exception):
    """Exception raised when a user attribute is invalid
    
    Args:
        Exception (_type_): _description_
    """
    pass


#Exception for adding a task to a category that has it already
class TaskAlreadyExists(Exception):
    """Exception raised when trying to add a task that already exists in a category
    
    Args:
        Exception (_type_): _description_
    """
    pass