import streamlit as st
from time import sleep
from models.authenticate import AuthenticateModel as Authenticate

class LoginView:
    """
    Classe para renderizar a página de login
    """
    @classmethod
    def show(cls):
        """
        Exibe a página de login
        """
        st.title("My Energy | Login")
        
        login = st.text_input("Login", label_visibility="visible")
        senha = st.text_input("Senha", type="password", label_visibility="visible")

        columns = st.columns(5, gap='large')

        if columns[0].button("Login"):
            logged = Authenticate.login(login, senha)

            if logged:
                st.session_state["logged_in"] = True
                st.session_state["user_login"] = login  
                st.success("Login successful!")
                sleep(0.5)
                st.session_state.page = "home"  
                st.rerun()
            else:
                st.error("Invalid credentials")

        if columns[4].button("Register"):
            st.session_state.page = "register"
            st.rerun()  
