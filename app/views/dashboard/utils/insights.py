import streamlit as st
from ...energy_bills.energy_bills import EnergyBillsView


class InsightsView(EnergyBillsView):
    """
    Class for viewing insights.

    Args:
        EnergyBillsView (Class): Class for extracting energy bills data.
    """

    @classmethod
    def show(cls):
        """
        Show insights about energy consumption and cost.
        """
        cls.check_bills_and_summary()

        summary = st.session_state.bills_summary
        bills = st.session_state.bills

        if summary and bills:
            st.subheader("🔍 Consumption and Cost Insights")

            average_value_per_bill = summary.get("total_value") / len(
                st.session_state.bills
            )
            average_consumption_per_bill = summary.get("total_consumption") / len(
                st.session_state.bills
            )

            with st.container():
                col1, col2 = st.columns(2)
                with col1:
                    st.metric(
                        label="💲 Average cost per bill (R$)",
                        value=f"R$ {average_value_per_bill:.2f}",
                    )
                with col2:
                    st.metric(
                        label="🔋 Average consumption per (kWh)",
                        value=f"{average_consumption_per_bill:.2f} kWh",
                    )

            st.markdown(
                "<hr style='border: 1px solid #4CAF50;'>", unsafe_allow_html=True
            )

            with st.expander("💡 Warnings and Tips", expanded=True):

                st.markdown("---")

                status_average = ""
                if average_value_per_bill <= 100:
                    st.success(
                        "✅ The average cost per invoice is within the average. Keep tracking your consumption."
                    )
                    status_average = "low"
                elif (
                    average_value_per_bill > 100 and average_consumption_per_bill <= 500
                ):
                    st.warning(
                        "⚠️ The average cost per invoice is relatively high. Consider reviewing energy consumption to identify savings opportunities."
                    )
                    status_average = "medium"
                else:
                    st.error(
                        "❗️ Average consumption per invoice is high. Try to adopt measures to reduce consumption, such as more efficient use of electrical appliances."
                    )
                    status_average = "high"

                if status_average in ["medium", "high"]:
                    st.markdown("---")
                    st.info(
                        "💡 Tip: Reducing the use of high-consumption appliances during peak hours can help reduce energy bills."
                    )
