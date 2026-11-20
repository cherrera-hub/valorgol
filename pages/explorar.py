"""Página Explorar: tabla, filtros, detalle, estadísticas y gráficos."""
import plotly.express as px
import streamlit as st

from src.data import estadisticas, filtrar, obtener_datos
from src.ui import COLORES, encabezado, formato_eur, icono_posicion, mostrar_foto

encabezado("Explorar", "Filtra la base de jugadores y analiza patrones.")
df = obtener_datos()

# ---------- Filtros (barra lateral) ----------
st.sidebar.header("Filtros")
posiciones = st.sidebar.multiselect("Posición", sorted(df["posicion"].dropna().unique()))
paises = st.sidebar.multiselect("País", sorted(df["pais"].unique()))
edad_min, edad_max = int(df["edad"].min()), int(df["edad"].max())
rango_edad = st.sidebar.slider("Edad", edad_min, edad_max, (edad_min, edad_max))
valor_max = float(df["valor_eur"].max()) / 1e6
rango_valor_m = st.sidebar.slider("Valor de mercado (millones €)", 0.0, valor_max, (0.0, valor_max))
nombre = st.sidebar.text_input("Nombre contiene")

rango_valor = (rango_valor_m[0] * 1e6, rango_valor_m[1] * 1e6)
filtrado = filtrar(df, posiciones, paises, rango_edad, rango_valor, nombre)

if filtrado.empty:
    st.warning("Ningún jugador cumple con los filtros. Prueba ampliarlos.")
    st.stop()

# ---------- Estadísticas ----------
stats = estadisticas(filtrado)
c1, c2, c3, c4 = st.columns(4)
c1.metric("Jugadores", f"{stats['jugadores']:,}")
c2.metric("Valor medio", formato_eur(stats["valor_medio"]))
c3.metric("Valor mediano", formato_eur(stats["valor_mediana"]))
c4.metric("Edad promedio", f"{stats['edad_media']:.1f}")

# ---------- Tabla interactiva ----------
st.subheader("Registros")
st.caption("Selecciona una fila para ver el detalle del jugador.")
columnas = ["nombre", "posicion", "pais", "club", "edad", "valor_eur"]
evento = st.dataframe(
    filtrado[columnas],
    on_select="rerun",
    selection_mode="single-row",
    hide_index=True,
)

# ---------- Detalle del registro ----------
filas = evento.selection.rows
if filas:
    jugador = filtrado.iloc[filas[0]]
    st.session_state["consultados"][int(jugador["player_id"])] = jugador["nombre"]
    st.subheader(f"Detalle: {jugador['nombre']}")
    col_foto, col_info = st.columns([1, 3])
    with col_foto:
        mostrar_foto(jugador["imagen_url"])
    with col_info:
        st.write(f"**Posición:** {icono_posicion(jugador['posicion'])} {jugador['posicion']}")
        st.write(f"**País:** {jugador['pais']}")
        st.write(f"**Club:** {jugador['club']}")
        st.write(f"**Edad:** {jugador['edad']} años")
        st.write(f"**Valor de mercado:** {formato_eur(jugador['valor_eur'])}")
else:
    st.info("Aún no has seleccionado ningún jugador.")

# ---------- Gráficos ----------
st.subheader("Visualizaciones")
g1, g2 = st.columns(2)
with g1:
    por_posicion = filtrado.groupby("posicion", as_index=False)["valor_eur"].mean()
    fig1 = px.bar(
        por_posicion, x="posicion", y="valor_eur",
        title="Valor medio por posición",
        labels={"posicion": "Posición", "valor_eur": "Valor medio (€)"},
        color_discrete_sequence=COLORES,
    )
    st.plotly_chart(fig1)
with g2:
    muestra = filtrado.sample(min(len(filtrado), 2000), random_state=1)
    fig2 = px.scatter(
        muestra, x="edad", y="valor_eur", color="posicion", hover_name="nombre",
        title="Edad vs. valor de mercado",
        labels={"edad": "Edad", "valor_eur": "Valor (€)", "posicion": "Posición"},
        color_discrete_sequence=COLORES,
    )
    st.plotly_chart(fig2)
