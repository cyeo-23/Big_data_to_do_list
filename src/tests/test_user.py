"""Unit tests for user class."""
from models.user import User


def test_valid_input():
    """Test initialization."""
    user = User("John", "Doe", "password123", "johndoe")
    assert user.firstname == "John"
    assert user.lastname == "Doe"
    assert user.password == "password123"
    assert user.pseudo == "johndoe"


def test_update_updates_user_info():
    """Test updating user info."""
    user = User(firstname="John", lastname="Doe",
                password="password", pseudo="johndoe")
    user.update(firstname="Jane", lastname="Smith",
                pseudo="janesmith", password="newpassword")

    assert user.firstname == "Jane"
    assert user.lastname == "Smith"
    assert user.pseudo == "janesmith"
    assert user.password == "newpassword"


def test_valid_attributes():
    """Test of serialization."""
    user = User(firstname="John", lastname="Doe",
                password="password", pseudo="johndoe")
    expected_dict = {
        "firstname": "John",
        "lastname": "Doe",
        "pseudo": "johndoe",
        "password": "password"
    }
    assert user.to_dict() == expected_dict


def test_create_user_from_dict_with_required_fields():
    """Test of load from dict."""
    user_dict = {
        "firstname": "John",
        "lastname": "Doe",
        "pseudo": "johndoe",
        "password": "password123",
        "_id": "65ze65fe5zf655"
    }
    user = User.from_dict(user_dict)
    assert isinstance(user, User)
    assert user.firstname == "John"
    assert user.lastname == "Doe"
    assert user.pseudo == "johndoe"
    assert user.password == "password123"
