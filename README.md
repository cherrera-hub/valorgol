# ValorGol ⚽

<p align="center">
  <img src="assets/logo.png" alt="Logo de ValorGol" width="180">
</p>

**ValorGol** es una aplicación web interactiva, hecha con Streamlit, para explorar el mercado de jugadores de fútbol profesional y poner a prueba el ojo del usuario con un juego sobre el valor de los futbolistas.

Proyecto grupal del trabajo final del curso **Algoritmos y Programación**, Universidad de Antioquia, semestre 2026-2. Docente: Natally Estrada.

---

## 👥 Integrantes

| | Integrante | Programa académico |
|---|---|---|
| <img src="assets/foto_estudiante_1.jpg" alt="Foto de Carlos" width="110"> | **Carlos Andrés Herrera Benavides** | Ingeniería Industrial, Universidad de Antioquia (Campus Caucasia) |
| <img src="assets/foto_estudiante_2.jpg" alt="Foto de Cristian" width="110"> | **Cristian Daniel Ramos Rivas** | Ingeniería Industrial, Universidad de Antioquia |

### Vínculos académicos, habilidades y fortalezas

**Carlos Andrés Herrera Benavides.** Estudiante de Ingeniería Industrial. Su formación incluye optimización, estadística y gestión de métodos y tiempos. En este proyecto lidera el repositorio, la limpieza de los datos, la página Explorar y la documentación base.

**Cristian Daniel Ramos Rivas.** Estudiante de Ingeniería Industrial, comprometido y responsable con el proyecto. Aporta constancia y puntualidad en las entregas, trabajo colaborativo y atención al detalle en el diseño de la interfaz y la experiencia de usuario. Se destaca por su disposición para aprender Python y Streamlit y por cumplir con seriedad las tareas asignadas en el Acta de responsabilidad. En este proyecto desarrolla el juego, las páginas Jugar, Mis datos e Inicio y la identidad visual.

---

## 🧭 Nombre del proyecto y detalles

**ValorGol** combina las palabras *valor* y *gol*: el valor de mercado de los jugadores y el mundo del fútbol. La aplicación se construye sobre un conjunto de datos real de jugadores (posición, país, club, edad y valor de mercado) y tiene cuatro páginas:

| Página | Qué ofrece |
|---|---|
| 🏠 **Inicio** | Presentación, contexto de los datos, indicadores generales, equipo, créditos y licencias |
| 🔎 **Explorar** | Tabla interactiva, filtros, detalle del jugador, estadísticas y gráficos |
| 🎮 **Jugar** | Juego «¿Cuánto vale?»: adivinar cuál de dos jugadores tiene mayor valor de mercado |
| 📊 **Mis datos** | Resumen de la actividad del usuario: partidas, puntajes, historial y jugadores consultados |

**Paleta de colores:** verde cancha `#1B7F3B`, verde oscuro `#0B2E1A`, amarillo `#F2C230` y blanco.

---

## 🔭 Reporte de visión

### Descripción general
ValorGol es una herramienta web que convierte una base de datos de futbolistas profesionales en una experiencia fácil de consultar y de jugar. El usuario puede filtrar jugadores, ver estadísticas y gráficos, y después jugar partidas de diez rondas en las que debe decidir cuál de dos jugadores reales tiene mayor valor de mercado.

### Objetivos
- Facilitar la consulta y el análisis de datos reales de jugadores de fútbol.
- Ofrecer una dinámica lúdica que use los datos de forma diferente a la consulta tradicional.
- Mostrar al usuario su propia actividad (partidas, puntajes y registros consultados) durante la sesión.
- Aplicar en un proyecto completo los conceptos del curso: funciones, estructuras de control, listas y diccionarios, manejo de excepciones, Pandas y programación orientada a objetos básica.

### Beneficios
- Aprender cómo se valoran los jugadores según su posición, edad y país.
- Entretenerse mientras se interpretan datos reales.
- Contar con un código organizado en módulos, documentado y fácil de ampliar.

---

## 🗂️ Estructura del repositorio

```text
valorgol/
├── .streamlit/config.toml     # tema visual
├── app.py                     # archivo principal
├── pages/                     # inicio, explorar, jugar, mis_datos
├── data/                      # raw/, limpieza.ipynb, datos.csv
├── src/                       # data.py, juego.py, estado.py, ui.py
├── assets/                    # logo y fotografías
├── docs/                      # licencia, requisitos, cronograma, presupuesto,
│                              # plan de versionado, manual de usuario
├── actas/                     # actas de entendimiento, colaboración y responsabilidad
├── requirements.txt
└── README.md
```

Parte de estos archivos se publican en las entregas siguientes, según el calendario del curso.

---

## ▶️ Instalación y ejecución

1. Instalar Python 3.10 o superior.
2. Instalar las librerías: `pip install -r requirements.txt`
3. Ejecutar la aplicación: `streamlit run app.py`

---

## 📚 Documentación

- [Actas](actas/)
- [Licencia](docs/LICENSE.md)
- [Especificación de requisitos](docs/requisitos.md)
- Plan de proyecto: [cronograma](docs/cronograma.xlsx) y [presupuesto](docs/presupuesto.xlsx)

## 📝 Créditos

- Datos: *Transfermarkt datasets*, publicados en Kaggle por David Cariboo (`davidcariboo/player-scores`) y en GitHub (`dcaribou/transfermarkt-datasets`), licencia CC0 1.0. Los datos originales provienen del sitio Transfermarkt.
- Librerías: Streamlit, pandas y Plotly.
