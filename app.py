"""Punto de entrada de ValorGol. Ejecutar con: streamlit run app.py"""
import streamlit as st

from src.estado import inicializar_estado
from src.ui import LOGO, NOMBRE_APP

st.set_page_config(page_title=NOMBRE_APP, page_icon="⚽", layout="wide")

inicializar_estado()

if LOGO.exists():
    st.logo(str(LOGO))

paginas = [
    st.Page("pages/inicio.py", title="Inicio", icon="🏠", default=True),
    st.Page("pages/explorar.py", title="Explorar", icon="🔎"),
    st.Page("pages/jugar.py", title="Jugar", icon="🎮"),
    st.Page("pages/mis_datos.py", title="Mis datos", icon="📊"),
]

st.navigation(paginas).run()
