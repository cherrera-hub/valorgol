# Especificación de requisitos

**Proyecto:** ValorGol, aplicación web de jugadores de fútbol con Streamlit.
**Curso:** Algoritmos y Programación, Universidad de Antioquia, 2026-2.
**Integrantes:** Carlos Andrés Herrera Benavides y Cristian Daniel Ramos Rivas.

## 1. Introducción

### 1.1 Propósito
Este documento describe lo que debe hacer ValorGol y las condiciones bajo las cuales debe funcionar.

### 1.2 Alcance
ValorGol permite explorar un conjunto de datos real de jugadores de fútbol, jugar partidas basadas en esos datos y consultar el resumen de la actividad del usuario durante la sesión.

### 1.3 Usuarios
Personas aficionadas al fútbol o interesadas en datos, sin necesidad de conocimientos técnicos. También la docente y los compañeros del curso, que revisan el proyecto.

### 1.4 Datos
La aplicación usa el archivo `data/datos.csv`, generado en `data/limpieza.ipynb` a partir de los datos originales de *Transfermarkt datasets* (Kaggle, licencia CC0 1.0).

## 2. Requisitos funcionales

Los requisitos funcionales definen lo que el software debe hacer.

### 2.1 Datos y navegación

| Código | Requisito |
|---|---|
| RF-01 | La aplicación debe cargar los datos desde `data/datos.csv` usando Pandas. |
| RF-02 | La aplicación debe tener cuatro páginas: Inicio, Explorar, Jugar y Mis datos. |
| RF-03 | El usuario debe poder pasar de una página a otra desde un menú de navegación claro y consistente. |
| RF-04 | La aplicación debe mostrar un mensaje claro si el archivo de datos no existe, está vacío o le faltan columnas. |

### 2.2 Página Inicio

| Código | Requisito |
|---|---|
| RF-05 | Debe mostrar el nombre, el logo y una descripción breve del propósito de la aplicación. |
| RF-06 | Debe explicar la temática de los datos, su fuente y su relevancia. |
| RF-07 | Debe describir las funcionalidades y ofrecer acceso directo a cada sección. |
| RF-08 | Debe mostrar al menos tres indicadores generales (jugadores, países, valor medio y partidas jugadas). |
| RF-09 | Debe presentar al equipo desarrollador y los objetivos del proyecto. |
| RF-10 | Debe reconocer las fuentes de datos, los recursos gráficos y las licencias. |

### 2.3 Página Explorar

| Código | Requisito |
|---|---|
| RF-11 | Debe mostrar los jugadores en una tabla interactiva que permita seleccionar un registro. |
| RF-12 | Debe permitir filtrar por posición, país, rango de edad, rango de valor de mercado y nombre. |
| RF-13 | Debe mostrar el detalle del jugador seleccionado (foto, posición, país, club, edad y valor). |
| RF-14 | Debe calcular al menos tres indicadores descriptivos de los datos filtrados (cantidad, valor medio, valor mediano y edad promedio). |
| RF-15 | Debe incluir al menos dos gráficos (valor medio por posición y edad frente a valor de mercado). |
| RF-16 | Los resultados, indicadores y gráficos deben actualizarse al cambiar los filtros. |
| RF-17 | Debe informar al usuario cuando ningún jugador cumple los filtros. |

### 2.4 Página Jugar: «¿Cuánto vale?»

| Código | Requisito |
|---|---|
| RF-18 | Debe explicar el objetivo, las reglas y la forma de participar. |
| RF-19 | Debe permitir iniciar una partida de 10 rondas. |
| RF-20 | En cada ronda debe mostrar dos jugadores reales del conjunto de datos y pedir al usuario que elija cuál tiene mayor valor de mercado. |
| RF-21 | Debe calcular el puntaje: 10 puntos por acierto y 2 puntos extra por cada acierto consecutivo adicional (racha). |
| RF-22 | Debe dar retroalimentación después de cada respuesta, indicando si fue correcta y el valor de ambos jugadores. |
| RF-23 | Al terminar la partida debe mostrar el puntaje, los aciertos y la mejor racha. |
| RF-24 | Debe guardar las partidas de la sesión (cantidad, puntajes y mejor resultado). |
| RF-25 | Debe permitir iniciar una nueva partida sin perder las estadísticas acumuladas. |

### 2.5 Página Mis datos

| Código | Requisito |
|---|---|
| RF-26 | Debe mostrar el resumen de actividad: partidas jugadas, puntaje acumulado, mejor resultado y jugadores consultados. |
| RF-27 | Debe mostrar estadísticas de juego, como la precisión global. |
| RF-28 | Debe mostrar el historial de partidas con fecha, puntaje, aciertos, mejor racha y duración. |
| RF-29 | Debe incluir un gráfico con la evolución del puntaje. |
| RF-30 | Debe mostrar un mensaje claro cuando el usuario todavía no tenga actividad. |
| RF-31 | Debe actualizarse automáticamente con las interacciones reales del usuario, sin ingresar datos a mano. |

## 3. Requisitos no funcionales

Los requisitos no funcionales describen cómo debe comportarse el sistema, más allá de sus funciones.

| Código | Categoría | Requisito |
|---|---|---|
| RNF-01 | Rendimiento | La carga de datos se almacena en caché para que las páginas respondan en pocos segundos. |
| RNF-02 | Rendimiento | La aplicación debe manejar más de 1.000 registros sin demoras apreciables al filtrar. |
| RNF-03 | Usabilidad | La interfaz debe ser clara, legible y coherente en las cuatro páginas, con la paleta de colores del proyecto. |
| RNF-04 | Usabilidad | Los botones, filtros y controles deben dar retroalimentación visible al usuario. |
| RNF-05 | Fiabilidad | La aplicación no debe fallar ante valores faltantes, entradas inválidas o resultados vacíos. |
| RNF-06 | Fiabilidad | El estado de la sesión (partidas y registros consultados) se conserva con `st.session_state` mientras dure la sesión. |
| RNF-07 | Seguridad y privacidad | La aplicación no pide ni guarda datos personales; la información de la sesión es temporal. |
| RNF-08 | Compatibilidad | Debe funcionar con Python 3.10 o superior, en Windows, Linux y macOS, y en navegadores web actuales. |
| RNF-09 | Portabilidad | Las dependencias se listan en `requirements.txt` y la aplicación se ejecuta con `streamlit run app.py`. |
| RNF-10 | Mantenibilidad | El código se organiza en módulos con nombres descriptivos, y las funciones principales tienen documentación. |
| RNF-11 | Legalidad | Se deben reconocer las fuentes de datos y respetar las licencias de los materiales usados. |

## 4. Restricciones

- Lenguaje: Python.
- Librerías principales: Streamlit, pandas y Plotly.
- La fuente de datos es el archivo `data/datos.csv`, con más de 1.000 registros y un tamaño menor a 100 MB (preferiblemente menos de 50 MB).
- El proyecto se entrega en un repositorio de GitHub y se sustenta de forma sincrónica con la docente.
