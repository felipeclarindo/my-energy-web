import streamlit as st
import pandas as pd
import requests


class EnergyBillsView:
    """
    Class for viewing energy bills table.
    """

    BASE_URL = "http://127.0.0.1:8000/api"

    @classmethod
    def check_bills_and_summary(cls) -> None:
        """
        Check if the bills and summary are in the session state.
        """
        if "bills" not in st.session_state:
            st.session_state["bills"] = cls.fetch_bills()
        else:
            if st.session_state.bills != cls.fetch_bills():
                st.session_state.bills = cls.fetch_bills()

        if "bills_summary" not in st.session_state:
            st.session_state["bills_summary"] = cls.fetch_bills_summary()
        else:
            if st.session_state.bills_summary != cls.fetch_bills_summary():
                st.session_state.bills_summary = cls.fetch_bills_summary()

    @classmethod
    def fetch_bills(cls) -> list | None:
        """
        Get all energy bills from the API.

        Returns:
            list | None: List of energy bills or None if an error occurs.
        """
        try:
            response = requests.get(f"{cls.BASE_URL}/energy-bills/")
            if response.status_code == 200:
                data = response.json()
                if data:
                    return data
        except Exception:
            return None

    @classmethod
    def fetch_bills_summary(cls) -> dict | None:
        """
        Get the summary of energy bills with consumption and cost.

        Returns:
            dict | None: Summary of energy bills or None if an error occurs.
        """
        try:
            response = requests.get(f"{cls.BASE_URL}/energy-bills/summary/")
            if response.status_code == 200:
                data = response.json()
                if data:
                    return data
                else:
                    st.error("No energy bills found.")
        except Exception:
            return None

    @classmethod
    def show(cls) -> None:
        """
        Show the energy bills table.
        """
        cls.check_bills_and_summary()

        columns = st.columns([6, 2])
        with columns[0]:
            st.markdown(
                """
                <h2 style="margin: 0; padding: 0;">Energy Bills</h2>
                """,
                unsafe_allow_html=True,
            )
        with columns[1]:
            if st.button(
                "➕ Add Energy Bill", key="btn_add", help="Add a new energy bill"
            ):
                st.session_state.page = "add_energy_bill"
                st.rerun()

        st.markdown("---")

        if st.session_state.bills:
            df = pd.DataFrame(st.session_state.bills)
            st.dataframe(df, use_container_width=True)
        else:
            st.warning("No energy bills available. Click 'Add' to create a new one.")
