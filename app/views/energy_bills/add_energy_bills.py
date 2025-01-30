import requests
import streamlit as st
from datetime import date
from .energy_bills import EnergyBillsView


class AddEnergyBillsView(EnergyBillsView):
    """
    Interface to add a new energy bill.

    Args:
        EnergyBillsView (Class): Class to extends the energy bills data.
    """

    @classmethod
    def show(cls) -> None:
        """
        Render the interface to add a new energy bill.
        """
        st.title("Add New Energy Bill")

        date_bill = st.date_input("Date", label_visibility="visible")
        if date_bill:
            date_bill = str(date_bill)
            if date_bill < date.today().isoformat():
                st.error("Please select a valid date.")

        consumption = st.number_input(
            "Energy Consumption (kWh)",
            min_value=0.0,
            format="%.2f",
            label_visibility="visible",
        )
        if consumption and consumption <= 0:
            st.error("Energy consumption must be greater than 0 kWh.")

        value = st.number_input(
            "Value", min_value=0.0, format="%.2f", label_visibility="visible"
        )
        if value and value <= 0:
            st.error("Value must be greater than 0.")

        if st.button("Add"):
            if not date_bill or consumption <= 0 or value <= 0:
                st.error("All fields are required and must be valid.")
            else:
                data = {
                    "data": str(date_bill),
                    "consumption": consumption,
                    "value": value,
                }

                response = requests.post(f"{cls.BASE_URL}/energy-bills/", json=data)
                if response.status_code == 201:
                    st.success("Energy bill added successfully.")

                    cls.check_bills_and_summary()
                    st.session_state.page = "manager_energy_bills"
                    st.rerun()
                else:
                    st.error(f"Server error: {response.text}")
