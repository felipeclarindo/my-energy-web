import streamlit as st
import plotly.express as px
from ...energy_bills.energy_bills import EnergyBillsView


class TotalConsumptionAndCostGraphView(EnergyBillsView):
    """
    Class for generating the total consumption and cost graph.

    Args:
        EnergyBillsView (Class): Class for extracting energy bills data.
    """

    @classmethod
    def show(cls):
        """
        Generate a pie chart for total consumption and cost
        """
        cls.check_bills_and_summary()

        summary = st.session_state.bills_summary

        if summary:

            labels = ["Consumption", "Cost"]
            values = [summary.get("total_consumption"), summary.get("total_value")]

            st.header("💰 Total Consumption and Cost")

            fig = px.pie(
                values=values,
                names=labels,
                height=400,
                color_discrete_sequence=["#4CAF50", "#FF5722"],
            )

            st.plotly_chart(fig)
