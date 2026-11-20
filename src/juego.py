"""Lógica del juego '¿Cuánto vale?' (programación orientada a objetos)."""
import random
import time
from datetime import datetime

PUNTOS_BASE = 10
BONO_RACHA = 2
RATIO_MINIMO = 1.15   # el jugador más caro debe valer al menos 15 % más


class Partida:
    """Una partida de N rondas: elegir cuál de dos jugadores vale más."""

    def __init__(self, df, rondas=10):
        if len(df) < 2:
            raise ValueError("Se necesitan al menos 2 jugadores para jugar.")
        self.df = df
        self.rondas = rondas
        self.ronda_actual = 0
        self.puntaje = 0
        self.aciertos = 0
        self.racha = 0
        self.mejor_racha = 0
        self.terminada = False
        self.par = None
        self.inicio = time.time()
        self.nueva_ronda()

    def nueva_ronda(self):
        """Sortea dos jugadores con valores claramente distintos."""
        intentos = 0
        while True:
            i, j = random.sample(range(len(self.df)), 2)
            a = self.df.iloc[i].to_dict()
            b = self.df.iloc[j].to_dict()
            mayor = max(a["valor_eur"], b["valor_eur"])
            menor = min(a["valor_eur"], b["valor_eur"])
            intentos += 1
            if (menor > 0 and mayor / menor >= RATIO_MINIMO) or intentos >= 100:
                break
        self.par = (a, b)

    def responder(self, eleccion):
        """Evalúa la elección (0 o 1), actualiza puntaje y avanza de ronda."""
        a, b = self.par
        correcto = 0 if a["valor_eur"] > b["valor_eur"] else 1
        acierto = eleccion == correcto
        if acierto:
            self.racha += 1
            self.aciertos += 1
            self.mejor_racha = max(self.mejor_racha, self.racha)
            puntos = PUNTOS_BASE + BONO_RACHA * (self.racha - 1)
        else:
            self.racha = 0
            puntos = 0
        self.puntaje += puntos
        resultado = {
            "acierto": acierto,
            "puntos": puntos,
            "nombres": (a["nombre"], b["nombre"]),
            "valores": (a["valor_eur"], b["valor_eur"]),
        }
        self.ronda_actual += 1
        if self.ronda_actual >= self.rondas:
            self.terminada = True
        else:
            self.nueva_ronda()
        return resultado

    def resumen(self):
        """Datos de la partida para guardar en el historial."""
        return {
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "puntaje": self.puntaje,
            "aciertos": self.aciertos,
            "rondas": self.rondas,
            "mejor_racha": self.mejor_racha,
            "duracion_s": round(time.time() - self.inicio),
        }
