import streamlit as st
from ..energy_bills.energy_bills import EnergyBillsView
from .graphs.monthly_summary import MonthlySummaryGraphView
from .graphs.total_consumption_cost import TotalConsumptionAndCostGraphView
from .utils.totals_consumption import TotalConsumptionView
from .utils.insights import InsightsView


class DashboardView(EnergyBillsView):
    """
    Class for generating the energy consumption dashboard.

    Args:
        EnergyBillsView (Class): Class for extracting energy bills data.
    """

    @classmethod
    def show(cls):
        cls.check_bills_and_summary()

        cls.bills = st.session_state.bills
        cls.summary = st.session_state.bills_summary

        if cls.bills and cls.summary:
            st.title("Energy Consumption Dashboard")

            TotalConsumptionView.show()
            st.markdown(
                "<hr style='border: 1px solid #4CAF50;'>", unsafe_allow_html=True
            )

            TotalConsumptionAndCostGraphView.show()
            st.markdown("---")

            MonthlySummaryGraphView.show()
            st.markdown("---")

            InsightsView.show()

        else:
            st.info("No energy bills found to generate the dashboard.")
            if st.button("Add Energy Bill"):
                st.session_state.page = "create_energy_bill"
                st.rerun()
