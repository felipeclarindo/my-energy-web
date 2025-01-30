import streamlit as st
from time import sleep
from models.authenticate import AuthenticateModel as Authenticate


class LoginView:
    """
    Class to render the login page.
    """

    @classmethod
    def show(cls):
        """
        Render the login page.
        """
        st.title("My Energy | Login")

        st.markdown("---")

        login = st.text_input("Login", label_visibility="visible")
        password = st.text_input(
            "Password", type="password", label_visibility="visible"
        )

        columns = st.columns(5, gap="large")

        if columns[0].button("Login"):
            logged = Authenticate.login(login, password)

            if logged:
                st.session_state["logged_in"] = True
                st.session_state["user_login"] = login
                st.success("Login successful!")
                sleep(1)
                st.session_state.page = "dashboard"
                st.rerun()
            else:
                st.error("Invalid credentials")

        if columns[4].button("Register"):
            st.session_state.page = "register"
            st.rerun()
