import streamlit as st
import requests
from datetime import date, datetime
import pandas as pd

BASE_URL = "http://127.0.0.1:8000/api"

class ManagerEnergyBillsView:
    """
    Classe de gerenciamento de contas de energia.
    """
    @classmethod
    def fetch_bills(cls):
        """
        Obtém as contas de energia do usuário.
        """
        response = requests.get(f"{BASE_URL}/energy-bills/")
        if response.status_code == 200:
            st.session_state.bills = response.json() 
            return st.session_state.bills
        else:
            st.error(f"Error fetching bills: {response.text}")

    @classmethod
    def add_bill(cls):
        """
        Renderiza a interface para adicionar uma nova conta de energia.
        """
        st.header("Add New Energy Bill")

        date_bill = st.date_input("Date", label_visibility="visible")
        if date_bill:
            date_bill = str(date_bill)
            if date_bill < date.today().isoformat():
                st.error("Please select a valid date.")

        consumption = st.number_input("Energy Consumption (kWh)", min_value=0.0, format="%.2f", label_visibility="visible")
        if consumption and consumption <= 0:
            st.error("Energy consumption must be greater than 0 kWh.")

        value = st.number_input("Value", min_value=0.0, format="%.2f", label_visibility="visible")
        if value and value <= 0:
            st.error("Value must be greater than 0.")

        if st.button("Add"):
            if not date_bill or consumption <= 0 or value <= 0:
                st.error("All fields are required and must be valid.")
            else:
                data = {
                    "data": str(date_bill),
                    "consumption": consumption,
                    "value": value,
                }

                response = requests.post(f"{BASE_URL}/energy-bills/", json=data)
                if response.status_code == 201:
                    st.success("Energy bill added successfully.")
                    st.session_state.bills = cls.fetch_bills()  
                    st.session_state.page = "manage_energy_bills" 
                else:
                    st.error(f"Server error: {response.text}")

    @classmethod
    def show(cls):
        """
        Renderiza a interface principal de gerenciamento de contas de energia.
        """
        bills = cls.fetch_bills()

        if not bills:
            st.info("No energy bills found.")
            if st.button("Add Energy Bill"):
                st.session_state.page = "create_energy_bill"
                st.rerun()
        else:
            st.title("Energy Bills")

            cls.show_bills_table()
            with st.expander("Manage Energy Bills", expanded=True):
                cls.show_bills_actions(bills)
                    
    @classmethod
    def edit_bill(cls):
        """
        Renderiza a interface para editar uma conta de energia.
        """
        st.session_state.page = "edit_energy_bill"
        st.header("Edit Energy Bill")

        # Recupera a conta selecionada
        selected_bill = st.session_state.selected_bill

        # Conversão de data para o formato adequado
        if isinstance(selected_bill['data'], str):
            try:
                selected_date = datetime.strptime(selected_bill['data'], "%Y-%m-%d").date()
            except ValueError:
                st.error("Data inválida no formato de string. Use o formato 'YYYY-MM-DD'.")
                selected_date = date.today()
        elif isinstance(selected_bill['data'], date):
            selected_date = selected_bill['data']
        else:
            st.error("Data inválida. Usando a data de hoje como padrão.")
            selected_date = date.today()

        # Inputs do usuário
        date_bill = st.date_input("Date", value=selected_date, label_visibility="visible")
        consumption = st.number_input(
            "Energy Consumption (kWh)",
            value=selected_bill['consumption'],
            min_value=0.0,
            format="%.2f",
            label_visibility="visible",
        )
        value = st.number_input(
            "Value",
            value=selected_bill['value'],
            min_value=0.0,
            format="%.2f",
            label_visibility="visible",
        )

        # Botão para atualizar os dados
        if st.button("Update"):
            # Validações antes de enviar os dados
            if not date_bill or consumption <= 0 or value <= 0:
                st.error("All fields are required and must be valid.")
            else:
                # Prepara os dados para atualização
                updated_data = {
                    "data": str(date_bill),
                    "consumption": consumption,
                    "value": value,
                }

                # Envia a solicitação PUT para a API
                response = requests.put(
                    f"{BASE_URL}/energy-bills/{selected_bill['id']}",
                    json=updated_data,
                )

                if response.status_code == 200:
                    st.success(f"Energy bill {selected_bill['id']} updated successfully.")
                    st.session_state.bills = cls.fetch_bills()
                    st.session_state.page = "manager_energy_bills"
                    st.rerun()
                else:
                    st.error(f"Server error: {response.text}")

    @classmethod
    def show_bills_actions(cls, bills):
        """
        Exibe ações de edição e exclusão para as contas de energia
        """
        st.header("Manage Bills")

        bill_options = [
            f"Bill {bill['id']} - {bill['data']} (R${bill['value']})" for bill in bills
        ]
        
        selected_bill_index = st.selectbox(
            "Select a Bill to Edit or Delete",
            range(len(bill_options)),
            format_func=lambda x: bill_options[x],
            label_visibility="visible"
        )

        selected_bill = bills[selected_bill_index]
        
        st.markdown(f"### **Selected Bill**")
        st.markdown(f"**Date**: {selected_bill['data']}", unsafe_allow_html=True)
        st.markdown(f"**Consumption**: {selected_bill['consumption']} kWh", unsafe_allow_html=True)
        st.markdown(f"**Value**: R${selected_bill['value']}", unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            if st.button(f"✏️ **Edit Bill {selected_bill['id']}**", key=f"edit_{selected_bill['id']}"):
                st.session_state.selected_bill = selected_bill
                st.session_state.page = "edit_energy_bill"  
                st.rerun() 

        with col2:
            if st.button(f"🗑️ **Delete Bill {selected_bill['id']}**", key=f"delete_{selected_bill['id']}"):
                cls.delete_bill(selected_bill['id'])
                st.session_state.bills = cls.fetch_bills()
                st.rerun()

    @classmethod
    def delete_bill(cls, bill_id):
        """
        Função para excluir a conta de energia.
        """
        response = requests.delete(f"{BASE_URL}/energy-bills/{bill_id}")
        if response.status_code == 200:
            st.success(f"Energy bill {bill_id} deleted successfully.")
        else:
            st.error(f"Error deleting bill {bill_id}: {response.text}")
    
    @classmethod
    def show_bills_table(cls):  
        """
        Exibe uma tabela com as informações das contas de energia
        """
        bills = cls.fetch_bills()  
        if bills:
            df = pd.DataFrame(bills)
            st.dataframe(df)  
        else:
            st.warning("No energy bills found.")


