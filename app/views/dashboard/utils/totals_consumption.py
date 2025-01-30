import streamlit as st
from ...energy_bills.energy_bills import EnergyBillsView


class TotalConsumptionView(EnergyBillsView):
    """
    Class for viewing total consumption and cost.

    Args:
        EnergyBillsView (Class): Class for extracting energy bills data.
    """

    @classmethod
    def show(cls):
        """
        Render the total consumption and cost to view.
        """
        cls.check_bills_and_summary()

        cls.bills = st.session_state.bills
        cls.summary = st.session_state.bills_summary

        if cls.bills and cls.summary:
            with st.container():
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"#### **Total Consumption (kWh):**")
                    st.markdown(
                        f"<h3 style='color: #4CAF50;'>{cls.summary.get('total_consumption')} kWh</h3>",
                        unsafe_allow_html=True,
                    )
                with col2:
                    st.markdown(f"#### **Total Cost (R$):**")
                    st.markdown(
                        f"<h3 style='color: #FF5722;'>R$ {cls.summary.get('total_value')}</h3>",
                        unsafe_allow_html=True,
                    )
