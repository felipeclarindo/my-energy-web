import requests

class UsersModel:
    BASE_URL = "http://127.0.0.1:8000/api"
    
    @classmethod
    def get_users(cls):
        """
        Retorna todos os usuários
        """
        return requests.get(cls.BASE_URL + "/users/")
    
    @classmethod
    def get_user_by_id(cls, user_id: int):
        """
        Retorna um usuário específico
        """
        return requests.get(cls.BASE_URL + f"/users/{user_id}/")

    @classmethod
    def get_user_by_cpf(cls, user_cpf):
        """
        Retorna um usuário específico pelo CPF
        """
        return requests.get(cls.BASE_URL + f"/users/cpf/{user_cpf}/")

    @classmethod
    def get_user_by_login(cls, user_login: str):
        """
        Retorna um usuário específico pelo login
        """
        return requests.get(cls.BASE_URL + f"/users/login/{user_login}")
    
    @classmethod
    def create_user(cls, user: dict):
        """
        Cria um novo usuário
        """
        return requests.post(cls.BASE_URL + "/users/", json=user)

    @classmethod
    def update_user(cls, user_id: int, user: dict):
        """
        Atualiza um usuário
        """
        return requests.put(cls.BASE_URL + f"/users/{user_id}/", json=user)
    
    @classmethod
    def delete_user(cls, user_id: int):
        """
        Deleta um usuário
        """
        return requests.delete(cls.BASE_URL + f"/users/{user_id}/")
    