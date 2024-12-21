import requests
from datetime import date

class EnergyBillModel:
    BASE_URL = "http://127.0.0.1:8000/api"

    def __init__(self, bill_id, data, consumption, value):
        """
        Inicializa a conta de energia.
        """
        self.bill_id = bill_id
        self.data = data
        self.consumption = consumption
        self.value = value

    def update(self, new_data, new_consumption, new_value):
        """
        Atualiza os dados de uma conta de energia no servidor.
        """
        data = {
            "data": new_data.isoformat(),
            "consumption": new_consumption,
            "value": new_value,
        }

        response = requests.put(f"{self.BASE_URL}/energy-bills/{self.bill_id}", json=data)
        return response

    def delete(self):
        """
        Exclui a conta de energia do servidor.
        """
        response = requests.delete(f"{self.BASE_URL}/energy-bills/{self.bill_id}")
        return response
