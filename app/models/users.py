import requests


class UsersModel:
    """
    Class for managing users in the API.

    Returns:
        dict: Dictionary with the routers(Crud) response from the API.
    """

    BASE_URL = "http://127.0.0.1:8000/api"

    @classmethod
    def get_users(cls) -> dict:
        """
        Get all users from the API.

        Returns:
            dict: List of users or an error message.
        """
        try:
            response = requests.get(cls.BASE_URL + "/users/")
            return response.json()
        except Exception as e:
            return {"message": "Server error", "error": str(e)}

    @classmethod
    def get_user_by_id(cls, user_id: int) -> dict:
        """
        Get a specific user by ID.

        Args:
            user_id (int): User ID.

        Returns:
            dict: Dictionary with the user data where id is equal to user_cpf related or an error message.
        """
        try:
            response = requests.get(cls.BASE_URL + f"/users/{user_id}/")
            return response.json()
        except Exception as e:
            return {"message": "Server error", "error": str(e)}

    @classmethod
    def get_user_by_cpf(cls, user_cpf: int) -> dict:
        """
        Get a specific user by CPF.

        Args:
            user_cpf (int): User CPF.

        Returns:
            dict: Dictionary with the user data where cpf is equals to user_cpf related or an error message.
        """
        try:
            response = requests.get(cls.BASE_URL + f"/users/cpf/{user_cpf}/")
            return response.json()
        except Exception as e:
            return {"message": "Server error", "error": str(e)}

    @classmethod
    def get_user_by_login(cls, user_login: str) -> dict:
        """
        Get a specific user by login.

        Args:
            user_login (str): User login.

        Returns:
            dict: Dictionary with the user data where login is equals to user_login related or an error message.
        """
        try:
            response = requests.get(cls.BASE_URL + f"/users/login/{user_login}")
            return response.json()
        except Exception as e:
            return {"message": "Server error", "error": str(e)}

    @classmethod
    def create_user(cls, user: dict) -> dict:
        """
        Create a new user in the database.

        Args:
            user (dict): Dictionary with the user data to adding in the database.

        Returns:
            dict: Response from the API with the creating status.
        """
        try:
            response = requests.post(cls.BASE_URL + "/users/", json=user)
            return response
        except Exception as e:
            return {"message": "Server error", "error": str(e)}

    @classmethod
    def update_user(cls, user_id: int, user: dict) -> dict:
        """
        Update a user in the database.

        Args:
            user_id (int): user ID.
            user (dict): data to update.

        Returns:
            dict: Response from the API with the updating status.
        """
        try:
            response = requests.put(cls.BASE_URL + f"/users/{user_id}/", json=user)
            return response.json()
        except Exception as e:
            return {"message": "Server error", "error": str(e)}

    @classmethod
    def delete_user(cls, user_id: int) -> dict:
        """
        Delete a user from the database.

        Args:
            user_id (int): User ID.

        Returns:
            dict: Response from the API with the deleting status.
        """
        try:
            response = requests.delete(cls.BASE_URL + f"/users/{user_id}/")
            return response.json()
        except Exception as e:
            return {"message": "Server error", "error": str(e)}
