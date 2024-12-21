import streamlit as st
import requests
import pandas as pd
import plotly.express as px

class DashboardView:
    BASE_URL = "http://127.0.0.1:8000/api"

    @classmethod
    def show(cls):
        """
        Exibe o Dashboard e os gráficos baseados no resumo das contas de energia
        """
        bills = st.session_state.bills if 'bills' in st.session_state else None
        if bills:
            if "bills_summary" not in st.session_state:
                response = requests.get(f"{cls.BASE_URL}/energy-bills/summary/")

                if response.status_code == 200:
                    try:
                        summary = response.json()  
                        st.session_state.bills_summary = summary  
                    except ValueError as e:
                        st.error(f"Erro ao decodificar a resposta JSON: {e}")
                        st.error(f"Resposta recebida: {response.text}")
                else:
                    st.error(f"Erro ao acessar a API. Status code: {response.status_code}")
                    st.error(f"Mensagem de erro: {response.text}")
            else:
                summary = st.session_state.bills_summary  

            if not summary:
                st.error("Resumo de contas de energia não encontrado!")

            st.title("Dashboard de Contas de Energia")

            # Caixa para o total de consumo e custo
            with st.container():
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"#### **Total de Consumo (kWh):**")
                    st.markdown(f"<h3 style='color: #4CAF50;'>{summary['total_consumption']} kWh</h3>", unsafe_allow_html=True)
                with col2:
                    st.markdown(f"#### **Total de Custo (R$):**")
                    st.markdown(f"<h3 style='color: #FF5722;'>R$ {summary['total_value']}</h3>", unsafe_allow_html=True)

            st.markdown("<hr style='border: 1px solid #4CAF50;'>", unsafe_allow_html=True) 

            cls.plot_total_value_and_consumption(summary)
            st.markdown("---")
            cls.plot_monthly_summary(summary)
            st.markdown("---")
            cls.show_insights(summary)
            st.markdown("---")
            cls.show_bills_table()
        else:
            st.info("Nenhuma conta de energia adicionada!")
            if st.button("Add Energy Bill"):
                st.session_state.page = "create_energy_bill"
                st.rerun()

    @classmethod
    def plot_monthly_summary(cls, summary):
        """
        Gera um gráfico de barras para o resumo mensal de consumo e custo
        """
        monthly_summary = summary['monthly_summary']
        
        df = pd.DataFrame(monthly_summary)
        df['month'] = pd.to_datetime(df['month'], format='%Y-%m')

        st.header("📊 Resumo Mensal de Consumo e Custo")

        fig = px.bar(
            df,
            x='month',
            y=['consumption', 'value'],
            labels={"month": "Mês", "value": "Custo (R$)", "consumption": "Consumo (kWh)"},
            barmode='group',
            height=500,
            color_discrete_sequence=["#4CAF50", "#FF5722"]  
        )

        st.plotly_chart(fig)

    @classmethod
    def plot_total_value_and_consumption(cls, summary):
        """
        Gera gráficos de pizza para o total de consumo e custo
        """
        labels = ['Consumo', 'Custo']
        values = [summary['total_consumption'], summary['total_value']] 

        st.header("💰 Total de Consumo e Custo")   

        fig = px.pie(
            values=values, 
            names=labels, 
            height=400,
            color_discrete_sequence=["#4CAF50", "#FF5722"]  
        )

        st.plotly_chart(fig)

    @classmethod
    def show_bills_table(cls):
        """
        Exibe uma tabela com as informações das contas de energia
        """
        if 'bills' not in st.session_state:
            st.session_state.bills = requests.get(f"{cls.BASE_URL}/energy-bills/").json()
            st.warning("❗ Nenhuma conta de energia carregada.")
        else:
            energy_bills = st.session_state.bills
            if energy_bills:
                df = pd.DataFrame(energy_bills)
                st.subheader("📊  Resumo das Contas de Energia")
                
                col = st.columns([1, 2, 1])[1]  
                with col:
                    st.write(df)
            else:
                st.warning("❗ Nenhuma conta de energia encontrada.")

    @classmethod
    def show_insights(cls, summary):
        """
        Gera insights a partir dos dados fornecidos
        """
        st.subheader("🔍 Análise de Consumo e Custo")

        # Verificar se as contas estão carregadas em st.session_state
        if 'bills' not in st.session_state or not st.session_state.bills:
            st.warning("❗ Não há contas de energia para gerar os insights.")
            return

        # Calcular os valores médios
        average_value_per_bill = summary['total_value'] / len(st.session_state.bills)
        average_consumption_per_bill = summary['total_consumption'] / len(st.session_state.bills)

        # Caixa de indicadores
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                st.metric(label="💲 Custo médio por fatura (R$)", value=f"R$ {average_value_per_bill:.2f}")
            with col2:
                st.metric(label="🔋 Consumo médio por fatura (kWh)", value=f"{average_consumption_per_bill:.2f} kWh")
        
        st.markdown("<hr style='border: 1px solid #4CAF50;'>", unsafe_allow_html=True)

        with st.expander("💡 Dicas e Avisos"):
            st.markdown("---")

            if average_value_per_bill < 100:
                st.info("✅ O custo médio por fatura está dentro da média. Continue acompanhando seu consumo.")
            if average_value_per_bill > 100:
                st.warning("⚠️ O custo médio por fatura está relativamente alto. Considere revisar o consumo de energia para identificar oportunidades de economia.")
            if average_consumption_per_bill > 500:
                st.warning("⚠️ O consumo médio por fatura está elevado. Tente adotar medidas para reduzir o consumo, como o uso mais eficiente de aparelhos elétricos.")

            st.markdown("---")
            
            # Sugestões adicionais
            st.info("💡 Dica: Reduzir o uso de aparelhos de alto consumo durante horários de pico pode ajudar a reduzir a fatura de energia.")
