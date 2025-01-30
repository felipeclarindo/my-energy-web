import streamlit as st
import requests
from .energy_bills import EnergyBillsView

class ManagerEnergyBillsView(EnergyBillsView):
    """
    Class to manage energy bills.

    Args:
        EnergyBillsView (Class): Base class to manage energy bills.
    """

    BASE_URL = "http://127.0.0.1:8000/api"

    @classmethod
    def show(cls):
        """
        Render the main interface to manage energy bills.
        """
        cls.check_bills_and_summary()
        cls.bills = st.session_state.bills

        if not cls.bills:
            st.info("No energy bills found.")
            if st.button("Add Energy Bill"):
                st.session_state.page = "create_energy_bill"
                st.rerun()
        else:
            cls.show_bills_actions()

    @classmethod
    def show_bills_actions(cls):
        """
        Render the actions to manage the energy bills.
        """
        st.title("Manage Energy Bills")

        st.markdown("---")

        with st.expander("", expanded=True):
            st.markdown("### Select an Energy Bill")
            bill_options = [
                f"Energy Bill {bill['id']} - {bill['data']} (R${bill['value']})"
                for bill in cls.bills
            ]
            selected_bill_index = st.selectbox(
                "",
                range(len(bill_options)),
                format_func=lambda x: bill_options[x],
                label_visibility="visible",
                key="selected_bill_index",
            )
            selected_bill = cls.bills[selected_bill_index]
            st.session_state.selected_bill = selected_bill

            st.markdown("---")

            st.markdown(f"### Energy Bill {selected_bill.get("id")} Details")
            st.dataframe(selected_bill, width=500)

            col1, col2 = st.columns(2)

            with col1:
                if st.button(
                    f"✏️ Edit Bill {selected_bill['id']}",
                    key=f"edit_{selected_bill['id']}",
                ):
                    st.session_state.page = "edit_energy_bill"
                    st.rerun()

            with col2:
                clicked = False
                if st.button(
                    f"🗑️ Delete Bill {selected_bill['id']}",
                    key=f"delete_{selected_bill['id']}",
                ):
                    clicked = True

            if clicked:
                cls.delete_bill(selected_bill["id"])
                st.session_state.bills = cls.fetch_bills()
                st.rerun()
    @classmethod
    def delete_bill(cls, bill_id: id) -> None:
        """
        Delete an energy bill.

        Args:
            bill_id (id): Energy bill ID.
        """
        response = requests.delete(f"{cls.BASE_URL}/energy-bills/{bill_id}")
        if response.status_code == 200:
            st.success(f"Energy bill {bill_id} deleted successfully.")
        else:
            st.error(f"Error deleting bill {bill_id}: {response.text}")
