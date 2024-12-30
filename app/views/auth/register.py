import streamlit as st
from email_validator import validate_email, EmailNotValidError
from validate_docbr import CPF
from time import sleep
from models.users import UsersModel


class RegisterView:
    """
    Class to render the register page.
    """

    CPF_VALIDATOR = CPF()

    @classmethod
    def show(cls) -> None:
        """
        Render the register page.
        """
        st.title("My Energy | Register")

        st.markdown("---")

        login = st.text_input("Login", label_visibility="visible")
        if login:
            if len(login) < 3:
                st.error("Login must have at least 3 characters")

        cpf = st.text_input("CPF", label_visibility="visible")
        if cpf:
            if not cls.CPF_VALIDATOR.validate(cpf):
                st.error("Invalid CPF")

        email = st.text_input("E-mail", label_visibility="visible")
        if email:
            try:
                validate_email(email)
            except EmailNotValidError as e:
                st.error(str(e))

        password = st.text_input(
            "Password", type="password", label_visibility="visible"
        )
        if password:
            if len(password) <= 8:
                st.error("Password must have at least 8 characters")

        confirm_password = st.text_input(
            "Confirm Password", type="password", label_visibility="visible"
        )

        if password != confirm_password:
            st.error("Passwords do not match")

        error = False

        columns = st.columns(7)

        button_register = columns[0].button("Register")
        button_back = columns[6].button("Back")

        if button_register:
            if (
                not login
                or not password
                or not confirm_password
                or not cpf
                or not email
            ):
                st.error("All fields are required")
                error = True
            else:
                try:
                    login_data = {
                        "login": login,
                        "cpf": cpf,
                        "email": email,
                        "password": password,
                    }
                    response = UsersModel.create_user(login_data)
                except Exception as e:
                    error = True
                    st.error(f"Server error: {str(e)}")

                if not error:
                    if response.status_code == 201:
                        st.success("User registered successfully")
                        st.session_state.page = "login"
                        st.rerun()
                    else:
                        response = response.json()
                        st.error(response["message"])

        if button_back:
            st.session_state.page = "login"
            st.rerun()
