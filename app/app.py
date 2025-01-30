import streamlit as st
from time import sleep
from .views.energy_bills.manager_energy_bills import ManagerEnergyBillsView
from .views.energy_bills.energy_bills import EnergyBillsView
from .views.energy_bills.add_energy_bills import AddEnergyBillsView
from .views.auth.register import RegisterView
from .views.dashboard.dashboard import DashboardView
from .views.auth.login import LoginView
from .views.energy_bills.edit_energy_bill import EditEnergyBillView


class App:
    """
    Class to render the application.
    """

    @classmethod
    def show(cls):
        """
        Render the page base in state of login and add sidebar
        """
        cls.setup_sidebar()

        if "logged_in" not in st.session_state:
            st.session_state.logged_in = False
        if "page" not in st.session_state:
            st.session_state.page = "login"

        if st.session_state.page == "login":
            cls.show_login()
        elif st.session_state.page == "register":
            cls.show_register()
        elif st.session_state.page == "dashboard":
            DashboardView.show()
        elif st.session_state.page == "energy_bills":
            EnergyBillsView.show()
        elif st.session_state.page == "add_energy_bill":
            AddEnergyBillsView.show()
        elif st.session_state.page == "create_energy_bill":
            AddEnergyBillsView.show()
        elif st.session_state.page == "manager_energy_bills":
            ManagerEnergyBillsView.show()
        elif st.session_state.page == "edit_energy_bill":
            EditEnergyBillView.show()

    @classmethod
    def setup_sidebar(cls):
        """
        Setup the sidebar
        """
        if st.session_state.get("logged_in"):
            with st.sidebar:
                st.title(":zap: My Energy")
                st.markdown("---")

                st.markdown("### **Menu**")
                if st.button(
                    "🏠 Dashboard", key="btn_dashboard", help="Control panel access"
                ):
                    st.session_state.page = "dashboard"
                    st.rerun()

                if st.button(
                    ":zap: Energy Bills", key="btn_energy_bills", help="Energy bills"
                ):
                    st.session_state.page = "energy_bills"
                    st.rerun()

                if st.button(
                    "📄 Manager Bills",
                    key="btn_manager",
                    help="View and manage your energy bills",
                ):
                    st.session_state.page = "manager_energy_bills"
                    st.rerun()

                st.markdown("---")
                if st.button("🚪 Logout", key="btn_logout", help="Logout"):
                    st.session_state.update({"logged_in": False, "page": "login"})
                    st.rerun()

    @classmethod
    def show_login(cls):
        """
        Shows the login page
        """
        if not "user_login" in st.session_state:
            st.session_state.user_login = None

        LoginView.show()

        if st.session_state.logged_in:
            sleep(0.4)
            st.session_state.page = "dashboard"
            st.rerun()

    @classmethod
    def show_register(cls):
        """
        Shows the registration page
        """
        RegisterView.show()

        if st.session_state.get("register"):
            st.session_state.page = "login"
            st.rerun()
