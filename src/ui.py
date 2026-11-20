"""Elementos visuales compartidos: identidad de ValorGol."""
from pathlib import Path

import pandas as pd
import streamlit as st

RAIZ = Path(__file__).resolve().parent.parent
LOGO = RAIZ / "assets" / "logo.png"
NOMBRE_APP = "ValorGol"
COLORES = ["#1B7F3B", "#F2C230", "#0B2E1A", "#6FBF8B", "#C9A227"]
FOTOS_EQUIPO = [
    RAIZ / "assets" / "foto_estudiante_1.jpg",
    RAIZ / "assets" / "foto_estudiante_2.jpg",
]


def formato_eur(valor):
    """Convierte un número a texto legible: 1500000 -> '€1.5 M'."""
    if pd.isna(valor):
        return "N/D"
    if valor >= 1_000_000:
        return f"€{valor / 1_000_000:.1f} M"
    return f"€{valor / 1_000:.0f} K"


def encabezado(titulo, subtitulo=""):
    """Título uniforme para todas las páginas."""
    st.title(f"⚽ {titulo}")
    if subtitulo:
        st.caption(subtitulo)


def mostrar_foto(url, ancho=150):
    """Muestra la foto del jugador o un aviso si no existe."""
    if isinstance(url, str) and url.startswith("http"):
        st.image(url, width=ancho)
    else:
        st.markdown("🧑 *Sin foto disponible*")


def icono_posicion(posicion):
    """Devuelve un emoji según la posición del jugador (usa match-case)."""
    match posicion:
        case "Portero":
            return "🧤"
        case "Defensa":
            return "🛡️"
        case "Mediocampista":
            return "🎯"
        case "Delantero":
            return "⚽"
        case _:
            return "👤"
