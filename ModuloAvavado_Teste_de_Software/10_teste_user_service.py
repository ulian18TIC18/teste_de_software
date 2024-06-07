import pytest

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

class UserService:
    def get_user_info(self, user_id):
        if user_id == 1:
            return {'user_id': 1, 'name': 'Jose Ulian'}
        else:
            return None

class UserManager:
    def __init__(self, user_service):
        self.user_service = user_service

    def fetch_user_info(self, user_id):
        user_info = self.user_service.get_user_info(user_id)
        if not user_info:
            raise ValueError("User not found")
        return user_info
    
def teste_localizar_user_info():
    usuario_service = UserService()
    usuario_manager = UserManager(usuario_service)
    usuario_info = usuario_manager.fetch_user_info(1)
    assert usuario_info == {'user_id': 1, 'name': 'Jose Ulian'}

def teste_user_inexistente():
    usuario_service = UserService()
    usuario_manager = UserManager(usuario_service)
    with pytest.raises(ValueError):
        usuario_manager.fetch_user_info(2)
