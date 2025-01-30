import streamlit as st
from app.app import App

st.set_page_config(page_title="My Energy", page_icon=":zap:")
App.show()
