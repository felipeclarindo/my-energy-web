import requests


class UserNotLoggedIn(Exception):
    """
    Exception raised when the user is not logged in.

    Args:
        Exception (Class): Base class for exceptions in Python.
    """

    def __init__(self, message="User is not logged in"):
        super().__init__(message)


class AuthenticateModel:
    """
    Class to connect to the API for authentication.

    Raises:
        UserNotLoggedIn: User is not logged in.

    Returns:
        JsonResponse_: Response from the API.
    """

    BASE_URL = "http://127.0.0.1:8000/api"
    logged = False

    @classmethod
    def login(cls, login: str, password: str) -> bool:
        """
        Authenticate user.

        Args:
            login (str): login to authenticate.
            password (str): password to authenticate.

        Returns:
            bool: True if authenticated or False if not.
        """
        data = {"login": login, "password": password}
        response = requests.post(f"{cls.BASE_URL}/authenticate/login", json=data)
        if response.status_code == 200:
            cls.logged = True
            return True
        return False

    @classmethod
    def logout(cls) -> None:
        """
        Logout user.

        Raises:
            UserNotLoggedIn: User is not logged in.
        """
        if cls.logged:
            cls.logged = False
        else:
            raise UserNotLoggedIn
