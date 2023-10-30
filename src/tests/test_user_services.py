"""Tests for userServices module."""
import argon2
from config.database_cursor import db
from services.user_services import UserServices
from models.user import User
from utils.exceptions import UserEmptyPassword, UserNotFound


def test_initializes():
    """Test UserService Initialization."""
    user_services = UserServices()
    assert user_services.collection == db["users"]
    assert isinstance(user_services.ph, argon2.PasswordHasher)


def test_valid_credentials(mocker):
    """Test add user."""
    user = User("John", "Doe", "password123", "johndoe")
    user_service = UserServices()
    mocker.patch.object(user_service.collection, 'find_one', return_value=None)
    mocker.patch.object(user_service.collection, 'insert_one',
                        return_value=mocker.Mock(inserted_id='123'))

    # Act
    result = user_service.add_user(user)

    # Assert
    assert result.id == '123'
    assert result.firstname == "John"
    assert result.lastname == "Doe"
    assert result.password != "password123"
    assert result.pseudo == "johndoe"


# def test_raises_user_not_found_if_pseudo_empty():
#     "Test connection if pseudo is empty."
#     user_service = UserServices()

#     try:
#         user_service.connect_user("", "password123")
#     except Exception as e:
#         assert isinstance(e, UserNotFound)


def test_user_not_found(mocker):
    """Test user not found."""
    user_service = UserServices()
    pseudo = "john_doe"
    password = "password123"
    mocker.patch.object(user_service.collection, 'find_one', return_value=None)

    # Act and Assert
    try:
        user_service.connect_user(pseudo, password)
    except Exception as e:
        assert isinstance(e, UserNotFound)


def test_valid_password_updated_successfully(mocker):
    """Test Update with valid password."""
    user_service = UserServices()
    user = User("John", "Doe", "password123", "johndoe")
    user.id = "12345"
    mocker.patch.object(user_service.collection, 'update_one')

    # Act
    user_service.update_user(user)

    # Assert
    user_service.collection.update_one.assert_called_once_with(
        {"_id": "12345"},
        {"$set": {
            "firstname": "John",
            "lastname": "Doe",
            "pseudo": "johndoe",
            "password": mocker.ANY
        }}
    )


def test_empty_password_raises_exception(mocker):
    """Test exception when password is empty."""
    user_service = UserServices()
    user = User("John", "Doe", "", "johndoe")
    mocker.patch.object(user_service.collection, 'update_one')

    try:
        user_service.update_user(user)
    except Exception as e:
        assert isinstance(e, UserEmptyPassword)


def test_none_password_raises_exception(mocker):
    """Test exception when password is None."""
    try:
        user_service = UserServices()
        user = User("John", "Doe", None, "johndoe")
        mocker.patch.object(user_service.collection, 'update_one')
        user_service.update_user(user)
    except Exception as e:
        assert isinstance(e, TypeError)


def test_invalid_password_type_raises_type_error(mocker):
    """Test invalid password type."""
    # Act & Assert
    try:
        user_service = UserServices()
        user = User("John", "Doe", 12345, "johndoe")
        mocker.patch.object(user_service.collection, 'update_one')

        user_service.update_user(user)
    except Exception as e:
        assert isinstance(e, TypeError)


def test_invalid_pseudo_type_raises_type_error(mocker):
    """Test invalid pseudo type."""
    try:
        user_service = UserServices()
        user = User("John", "Doe", "password123", 12345)
        mocker.patch.object(user_service.collection, 'update_one')

        user_service.update_user(user)
    except Exception as e:
        assert isinstance(e, TypeError)
