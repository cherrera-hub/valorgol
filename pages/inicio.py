"""Página de inicio: presentación, datos, funcionalidades e indicadores."""
import streamlit as st

from src.data import obtener_datos
from src.ui import FOTOS_EQUIPO, LOGO, NOMBRE_APP, encabezado, formato_eur

df = obtener_datos()

col_logo, col_texto = st.columns([1, 4])
with col_logo:
    if LOGO.exists():
        st.image(str(LOGO), width=140)
with col_texto:
    encabezado(NOMBRE_APP, "Explora el mercado del fútbol y pon a prueba tu ojo para el valor de los jugadores.")

st.header("📚 Sobre los datos")
st.write(
    "Trabajamos con información real de jugadores de fútbol profesional: posición, país, "
    "club, edad y valor de mercado. Sirve para entender cómo se valoran los futbolistas y "
    "qué factores influyen en su precio."
)
st.caption(
    "Fuente: Transfermarkt datasets (Kaggle: davidcariboo/player-scores; GitHub: "
    "dcaribou/transfermarkt-datasets). Licencia CC0 1.0."
)

st.header("📈 Indicadores generales")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Jugadores", f"{len(df):,}")
c2.metric("Países", df["pais"].nunique())
c3.metric("Valor medio", formato_eur(df["valor_eur"].mean()))
c4.metric("Partidas jugadas", len(st.session_state["historial"]))

st.header("🧭 Funcionalidades")
f1, f2, f3 = st.columns(3)
with f1:
    st.subheader("🔎 Explorar")
    st.write("Filtra jugadores, consulta su detalle y analiza gráficos.")
    st.page_link("pages/explorar.py", label="Ir a Explorar", icon="🔎")
with f2:
    st.subheader("🎮 Jugar")
    st.write("Adivina qué jugador vale más y acumula puntos.")
    st.page_link("pages/jugar.py", label="Ir a Jugar", icon="🎮")
with f3:
    st.subheader("📊 Mis datos")
    st.write("Revisa tu historial, tu progreso y los jugadores consultados.")
    st.page_link("pages/mis_datos.py", label="Ir a Mis datos", icon="📊")

st.header("👥 Acerca de")
st.write("Proyecto final de Algoritmos y Programación, Universidad de Antioquia, 2026-2.")
equipo = [
    ("Carlos Andrés Herrera Benavides", "Ingeniería Industrial, UdeA. Líder: repositorio, datos y página Explorar."),
    ("Cristian Daniel Ramos Rivas", "Ingeniería Industrial, UdeA. Juego, Mis datos, Inicio e identidad visual."),
]
columnas_equipo = st.columns(len(equipo))
for columna, foto, (nombre, rol) in zip(columnas_equipo, FOTOS_EQUIPO, equipo):
    with columna:
        if foto.exists():
            st.image(str(foto), width=130)
        st.markdown(f"**{nombre}**")
        st.caption(rol)

st.header("📝 Créditos y licencias")
st.markdown(
    "- Datos: Transfermarkt datasets, licencia CC0 1.0 (los datos originales provienen de Transfermarkt).\n"
    "- Fotos de jugadores: enlaces de Transfermarkt incluidos en el dataset.\n"
    "- Librerías: Streamlit, pandas y Plotly.\n"
    "- Logo y paleta: Cristian Daniel Ramos Rivas, con apoyo de herramientas de inteligencia artificial.\n"
    "- Software: licencia CC BY-NC 4.0 (ver `docs/LICENSE.md`)."
)
