import random
import mazo
import juego

def crearJugador(): #Se inicializa el diccionario jugador con todas las variables necesarias
    jugador = {}
    jugador['nombre'] = input("Ingrese el nombre con el que va a jugar: ")
    jugador['puntaje'] = 0
    jugador['puntaje_ranking'] = 0
    jugador['pozo'] = 300
    jugador['ronda'] = 1
    jugador['manos'] = 5
    jugador['descartes'] = 3
    jugador['mazoCompleto'] = mazo.crearMazoCompleto()
    jugador['mazoRonda'] = jugador['mazoCompleto'].copy()  
    jugador['manoJugador'] = []
    jugador['monedas'] = 0
    jugador['jokers'] = []
    jugador['planetas'] = []
    jugador['combinaciones'] = {
                                "carta_alta": (5, 1),
                                "par": (10, 2),
                                "doble_par": (20, 2),
                                "trio": (30, 3),
                                "escalera": (30, 4),
                                "color": (35, 4),
                                "full_house": (40, 4),
                                "poker": (60, 7),
                                "escalera_corrida": (100, 8)
                            }
    jugador['jokersDisponibles'] = (
                                    {"nombre": "Par", "descripcion": "Si la mano es Par, multiplica x3.", "tipo_bonificacion": "multiplicar", "bonificacion": 3, "probabilidad": 0.70, "rareza": "común"},
                                    {"nombre": "Color Favorito", "descripcion": "Mismo palo en toda la jugada suma 200 fichas.", "tipo_bonificacion": "puntaje", "bonificacion": 200, "probabilidad": 0.62, "rareza": "común"},
                                    {"nombre": "Corazón Generoso", "descripcion": "Cada corazón aporta +25 fichas.", "tipo_bonificacion": "puntaje", "bonificacion": 25, "probabilidad": 0.68, "rareza": "común"},
                                    {"nombre": "As de Oro", "descripcion": "Si aparece cualquier As, suma +100 fichas.", "tipo_bonificacion": "puntaje", "bonificacion": 100, "probabilidad": 0.65, "rareza": "común"},
                                    {"nombre": "Rey del Multiplicador", "descripcion": "Aumenta el multiplicador base +1.", "tipo_bonificacion": "sum_multiplicador", "bonificacion": 1, "probabilidad": 0.58, "rareza": "común"},
                                    {"nombre": "Dupla Segura", "descripcion": "Parejas suman +150 fichas.", "tipo_bonificacion": "puntaje", "bonificacion": 150, "probabilidad": 0.60, "rareza": "común"},
                                    {"nombre": "Punta y Hacha", "descripcion": "Cartas 2–5 suman +20 fichas cada una.", "tipo_bonificacion": "puntaje", "bonificacion": 20, "probabilidad": 0.66, "rareza": "común"},
                                    {"nombre": "Dama Cortés", "descripcion": "Si hay al menos una Dama, +1 al multiplicador.", "tipo_bonificacion": "sum_multiplicador", "bonificacion": 1, "probabilidad": 0.55, "rareza": "común"},
                                    {"nombre": "Trío Amable", "descripcion": "Si la mano es Trío, multiplica x2.", "tipo_bonificacion": "multiplicar", "bonificacion": 2, "probabilidad": 0.57, "rareza": "común"},
                                    {"nombre": "Diez Limpio", "descripcion": "Cada carta 10 suma +30 fichas.", "tipo_bonificacion": "puntaje", "bonificacion": 30, "probabilidad": 0.63, "rareza": "común"},

                                    {"nombre": "Triple Doble", "descripcion": "Dobles parejas obtienen multiplicador x2 adicional.", "tipo_bonificacion": "multiplicar", "bonificacion": 2, "probabilidad": 0.42, "rareza": "raro"},
                                    {"nombre": "Dama de Fortuna", "descripcion": "Si hay una Dama, +2 al multiplicador.", "tipo_bonificacion": "sum_multiplicador", "bonificacion": 2, "probabilidad": 0.40, "rareza": "raro"},
                                    {"nombre": "Palo Fiel", "descripcion": "Por cada carta del mismo palo, +80 fichas.", "tipo_bonificacion": "puntaje", "bonificacion": 80, "probabilidad": 0.38, "rareza": "raro"},
                                    {"nombre": "Escalera Realista", "descripcion": "Escalera o escalera real multiplica x4.", "tipo_bonificacion": "multiplicar", "bonificacion": 4, "probabilidad": 0.32, "rareza": "raro"},
                                    {"nombre": "Doble As", "descripcion": "Por cada As en la mano, +2 al multiplicador.", "tipo_bonificacion": "sum_multiplicador", "bonificacion": 2, "probabilidad": 0.35, "rareza": "raro"},
                                    {"nombre": "Sota Traviesa", "descripcion": "Cada J (Sota) suma +120 fichas.", "tipo_bonificacion": "puntaje", "bonificacion": 120, "probabilidad": 0.36, "rareza": "raro"},
                                    {"nombre": "Poker", "descripcion": "Si hay 4 cartas del mismo rango, multiplica x3.", "tipo_bonificacion": "multiplicar", "bonificacion": 3, "probabilidad": 0.28, "rareza": "raro"},
                                    {"nombre": "Rey de Copas", "descripcion": "Cada Rey otorga +2 al multiplicador.", "tipo_bonificacion": "sum_multiplicador", "bonificacion": 2, "probabilidad": 0.30, "rareza": "raro"},

                                    {"nombre": "Joker Comodín", "descripcion": "Full House duplica el multiplicador (x4).", "tipo_bonificacion": "multiplicar", "bonificacion": 4, "probabilidad": 0.12, "rareza": "legendario"},
                                    {"nombre": "As de Picas", "descripcion": "Si hay As de picas, +500 fichas.", "tipo_bonificacion": "puntaje", "bonificacion": 500, "probabilidad": 0.10, "rareza": "legendario"},
                                    {"nombre": "Corona Triple", "descripcion": "Si hay 3 figuras (J/Q/K) en la mano, multiplica x6.", "tipo_bonificacion": "multiplicar", "bonificacion": 6, "probabilidad": 0.07, "rareza": "legendario"},
                                    {"nombre": "Motor Infinito", "descripcion": "Hand ganadora obtiene +5 al multiplicador base.", "tipo_bonificacion": "sum_multiplicador", "bonificacion": 5, "probabilidad": 0.06, "rareza": "legendario"},
                                    {"nombre": "Tesoro Oculto", "descripcion": "Color + Escalera en la misma mano multiplica x8.", "tipo_bonificacion": "multiplicar", "bonificacion": 8, "probabilidad": 0.05, "rareza": "legendario"},
                                    {"nombre": "Fortuna Eterna", "descripcion": "Si la mano supera cierto umbral de fichas, suma +800 fichas.", "tipo_bonificacion": "puntaje", "bonificacion": 800, "probabilidad": 0.04, "rareza": "legendario"}
                                )
    

    return jugador
 
def nuevaRonda(jugador): #Se restablecen variables del diccionario jugador y se incrementan las necesarias para que se desarrolle el juego
    sumarPuntajeRanking(jugador)
    jugador['manoJugador'] = []
    jugador['mazoRonda'] = jugador['mazoCompleto'].copy()
    jugador['ronda'] += 1
    jugador['pozo'] = round(jugador['pozo']*random.uniform(1.5,2))
    jugador['puntaje'] = 0
    jugador['manos'] = 5
    jugador['descartes'] = 3
    print()
    print(f"Jugador: {jugador['nombre']} | Pozo: {jugador['pozo']}")
    print()
    mazo.repartirCartas(10, jugador)
    juego.juego(jugador)

def mostrarJokersJugador(jugador): #Muestra los jokers que el jugador tiene en la mano
    if len(jugador["jokers"]) > 0:
        i=1
        for joker in jugador["jokers"]:
            print(f"{i}. {joker['nombre']}: {joker['nombre']}")
            i+=1
    else:
        print("No hay jokers adquiridos")


def sumarPuntajeRanking(jugador): #Suma el puntaje de la tabla historica.
    jugador['puntaje_ranking'] += jugador['puntaje'] 