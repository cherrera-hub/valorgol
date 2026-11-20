"""Manejo del estado de sesión (st.session_state)."""
import streamlit as st

ESTADO_INICIAL = {
    "historial": [],          # lista de partidas terminadas (dicts)
    "partida": None,          # objeto Partida en curso
    "feedback": None,         # resultado de la última respuesta
    "partida_guardada": False,
    "consultados": {},        # {player_id: nombre} de registros vistos en Explorar
}


def inicializar_estado():
    """Crea las claves de session_state que aún no existan."""
    for clave, valor in ESTADO_INICIAL.items():
        if clave not in st.session_state:
            st.session_state[clave] = valor.copy() if hasattr(valor, "copy") else valor
