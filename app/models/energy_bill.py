import requests


class EnergyBillModel:
    """
    Class to connect to the API for energy bills.

    Returns:
        JsonResponse: Response from the API.
    """

    def __init__(
        self, bill_id: int, data: str, consumption: float, value: float
    ) -> None:
        """
        Initialize the energy bill model.

        Args:
            bill_id (int): Id of the energy bill.
            data (str): Date in the format YYYY-MM-DD.
            consumption (float): Consumption in kWh.
            value (float): Value of the bill in R$.
        """
        self.BASE_URL = "http://127.0.0.1:8000/api"
        self.bill_id = bill_id
        self.data = data
        self.consumption = consumption
        self.value = value

    def update(self, new_data: str, new_consumption: float, new_value: float) -> dict:
        """
        Update an energy bill in the database.

        Args:
            new_data (str): Date in the format YYYY-MM-DD.
            new_consumption (float): Consumption in kWh.
            new_value (float):Value of the bill in R$.

        Returns:
            dict: Response from the API.
        """
        data = {
            "data": new_data.isoformat(),
            "consumption": new_consumption,
            "value": new_value,
        }
        try:
            response = requests.put(
                f"{self.BASE_URL}/energy-bills/{self.bill_id}", json=data
            )
            return response.json()
        except Exception as e:
            return {"message": "Server error", "error": str(e)}

    def delete(self) -> dict:
        """
        Delete an energy bill from the database.

        Returns:
            dict: Response from the API.
        """
        try:
            response = requests.delete(f"{self.BASE_URL}/energy-bills/{self.bill_id}")
            return response.json()
        except Exception as e:
            return {"message": "Server error", "error": str(e)}
