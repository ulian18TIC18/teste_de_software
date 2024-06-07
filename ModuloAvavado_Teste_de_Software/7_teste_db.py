import pytest
from unittest.mock import MagicMock

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Database:
    def save_user(self, user):
        pass

class UserService:
    def __init__(self, db):
        self.db = db

    def save_user(self, user: User):
        if not user.name or not user.email:
            raise ValueError("User must have a name and email")
        self.db.save_user(user)


@pytest.fixture
def user():
    return User('Ulian Almeida', 'ulian18@gmail.com')

def test_deve_salvar_usuario_com_sucesso(user):
    # Arrange
    mock_db = MagicMock(Database).return_value
    mock_db.save_user.return_value = None
    service = UserService(mock_db)

    # Act
    service.save_user(user=user)

    # Assert
    mock_db.save_user.assert_called_with(user)
