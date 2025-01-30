import requests
import streamlit as st
from datetime import date, datetime
from .energy_bills import EnergyBillsView


class EditEnergyBillView(EnergyBillsView):
    """
    Class for editing an energy bill.
    """

    @classmethod
    def show(cls):
        """
        Show the interface for editing an energy bill.
        """
        st.header("Edit Energy Bill")

        selected_bill = st.session_state.selected_bill

        if isinstance(selected_bill["data"], str):
            try:
                selected_date = datetime.strptime(
                    selected_bill["data"], "%Y-%m-%d"
                ).date()
            except ValueError:
                st.error("Invalid date format. Use format 'YYYY-MM-DD'.")
                selected_date = date.today()
        elif isinstance(selected_bill["data"], date):
            selected_date = selected_bill["data"]
        else:
            st.error("Invalid date. Using today's date with default.")
            selected_date = date.today()

        date_bill = st.date_input(
            "Date", value=selected_date, label_visibility="visible"
        )
        consumption = st.number_input(
            "Energy Consumption (kWh)",
            value=selected_bill["consumption"],
            min_value=0.0,
            format="%.2f",
            label_visibility="visible",
        )
        value = st.number_input(
            "Value",
            value=selected_bill["value"],
            min_value=0.0,
            format="%.2f",
            label_visibility="visible",
        )

        if st.button("Update"):
            if not date_bill or consumption <= 0 or value <= 0:
                st.error("All fields are required and must be valid.")
            else:
                updated_data = {
                    "data": str(date_bill),
                    "consumption": consumption,
                    "value": value,
                }
                response = requests.put(
                    f"{cls.BASE_URL}/energy-bills/{selected_bill['id']}",
                    json=updated_data,
                )

                if response.status_code == 200:
                    st.success(
                        f"Energy bill {selected_bill['id']} updated successfully."
                    )
                    st.session_state.bills = cls.fetch_bills()
                    st.session_state.page = "manager_energy_bills"
                    st.rerun()
                else:
                    st.error(f"Server error: {response.text}")
