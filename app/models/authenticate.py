import requests

class AuthenticateModel:
    BASE_URL = "http://127.0.0.1:8000/api"  
    logged = False

    @classmethod
    def login(cls, username: str, password: str) -> bool:
        """
        Realiza o login de um usuário com username e password.
        """
        data = {
            "login": username,
            "senha": password
        }
        response = requests.post(f"{cls.BASE_URL}/authenticate/login", json=data)
        if response.status_code == 200:
            cls.logged = True
            return True
        return False

    @classmethod
    def logout(cls) -> None:
        """
        Realiza o logout do usuário.
        """
        if cls.logged:
            cls.logged = False
        else:
            raise Exception("User is not logged in")
