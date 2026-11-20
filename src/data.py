"""Carga, validación y consulta de los datos (data/datos.csv)."""
from pathlib import Path

import pandas as pd
import streamlit as st

RUTA_DATOS = Path(__file__).resolve().parent.parent / "data" / "datos.csv"
COLUMNAS_REQUERIDAS = [
    "player_id", "nombre", "posicion", "pais", "club",
    "edad", "valor_eur", "imagen_url",
]


@st.cache_data(show_spinner="Cargando datos...")
def cargar_datos(ruta=RUTA_DATOS):
    """Lee el CSV limpio y verifica que tenga las columnas necesarias."""
    df = pd.read_csv(ruta)
    faltantes = [c for c in COLUMNAS_REQUERIDAS if c not in df.columns]
    if faltantes:
        raise ValueError(f"Faltan columnas en datos.csv: {faltantes}")
    df = df.dropna(subset=["nombre", "valor_eur", "edad"]).copy()
    df["pais"] = df["pais"].fillna("Desconocido")
    df["club"] = df["club"].fillna("Sin club")
    df["edad"] = df["edad"].astype(int)
    return df.reset_index(drop=True)


def obtener_datos():
    """Devuelve el DataFrame o detiene la página con un mensaje claro."""
    try:
        return cargar_datos()
    except FileNotFoundError:
        st.error("No se encontró `data/datos.csv`. Ejecuta primero `data/limpieza.ipynb`.")
    except pd.errors.EmptyDataError:
        st.error("El archivo `data/datos.csv` está vacío.")
    except ValueError as error:
        st.error(str(error))
    st.stop()


def filtrar(df, posiciones, paises, rango_edad, rango_valor, nombre):
    """Aplica los filtros de Explorar. Listas vacías significan 'todos'."""
    resultado = df
    if posiciones:
        resultado = resultado[resultado["posicion"].isin(posiciones)]
    if paises:
        resultado = resultado[resultado["pais"].isin(paises)]
    resultado = resultado[resultado["edad"].between(*rango_edad)]
    resultado = resultado[resultado["valor_eur"].between(*rango_valor)]
    if nombre.strip():
        resultado = resultado[
            resultado["nombre"].str.contains(nombre.strip(), case=False, na=False)
        ]
    return resultado.reset_index(drop=True)


def estadisticas(df):
    """Indicadores descriptivos de un DataFrame (vacío devuelve ceros)."""
    if df.empty:
        return {"jugadores": 0, "valor_medio": 0, "valor_mediana": 0, "edad_media": 0}
    return {
        "jugadores": len(df),
        "valor_medio": df["valor_eur"].mean(),
        "valor_mediana": df["valor_eur"].median(),
        "edad_media": df["edad"].mean(),
    }
