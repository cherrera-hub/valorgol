"""Página Mis datos: actividad del usuario durante la sesión."""
import pandas as pd
import plotly.express as px
import streamlit as st

from src.ui import COLORES, encabezado

encabezado("Mis datos", "Resumen de tu actividad en ValorGol durante esta sesión.")

historial = st.session_state["historial"]
consultados = st.session_state["consultados"]

if not historial and not consultados:
    st.info("Todavía no tienes actividad. Juega una partida o selecciona jugadores en Explorar.")
    st.stop()

# ---------- Resumen ----------
partidas = pd.DataFrame(historial)
c1, c2, c3, c4 = st.columns(4)
c1.metric("Partidas jugadas", len(partidas))
c2.metric("Puntaje acumulado", int(partidas["puntaje"].sum()) if not partidas.empty else 0)
c3.metric("Mejor resultado", int(partidas["puntaje"].max()) if not partidas.empty else 0)
c4.metric("Jugadores consultados", len(consultados))

# ---------- Juego ----------
st.subheader("🎮 Estadísticas de juego")
if partidas.empty:
    st.info("Aún no has terminado ninguna partida.")
else:
    total_aciertos = partidas["aciertos"].sum()
    total_rondas = partidas["rondas"].sum()
    st.write(f"**Precisión global:** {total_aciertos / total_rondas:.0%} ({total_aciertos} de {total_rondas} rondas)")
    fig = px.line(
        partidas, x="partida", y="puntaje", markers=True,
        title="Evolución de tu puntaje",
        labels={"partida": "Partida", "puntaje": "Puntaje"},
        color_discrete_sequence=COLORES,
    )
    st.plotly_chart(fig)
    st.subheader("🕒 Historial")
    st.dataframe(
        partidas[["partida", "fecha", "puntaje", "aciertos", "mejor_racha", "duracion_s"]],
        hide_index=True,
    )
    st.download_button(
        "⬇️ Descargar mi historial (CSV)",
        partidas.to_csv(index=False).encode("utf-8"),
        file_name="mi_historial_valorgol.csv",
        mime="text/csv",
    )

# ---------- Explorar ----------
st.subheader("🔎 Jugadores consultados")
if consultados:
    st.write(", ".join(consultados.values()))
else:
    st.info("Aún no has seleccionado jugadores en Explorar.")
