import streamlit as st
import pandas as pd
import plotly.express as px
from ...energy_bills.energy_bills import EnergyBillsView


class MonthlySummaryGraphView(EnergyBillsView):
    """
    Generate graphs for monthly summary of energy bills.

    Args:
        EnergyBills (Class): Class for extracting energy bills data.
    """

    @classmethod
    def show(cls):
        """
        Generate bar chart for monthly consumption and cost
        """
        cls.check_bills_and_summary()

        summary = st.session_state.bills_summary

        if summary:

            monthly_summary = summary.get("monthly_summary")

            df = pd.DataFrame(monthly_summary)
            df["month"] = pd.to_datetime(df["month"], format="%Y-%m")

            st.header("📊 Resumo Mensal de Consumo e Custo")

            fig = px.bar(
                df,
                x="month",
                y=["consumption", "value"],
                labels={
                    "month": "Month",
                    "value": "Cost (R$)",
                    "consumption": "Consumption (kWh)",
                },
                barmode="group",
                height=500,
                color_discrete_sequence=["#4CAF50", "#FF5722"],
            )

            st.plotly_chart(fig)
