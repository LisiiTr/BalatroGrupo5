import random
import mazo
import juego

def crearJugador():
    jugador = {}
    jugador['nombre'] = input("Ingrese el nombre con el que va a jugar: ")
    jugador['puntaje'] = 0
    jugador['pozo'] = 300
    jugador['ronda'] = 1
    jugador['manos'] = 5
    jugador['descartes'] = 3
    jugador['mazoCompleto'] = mazo.crearMazoCompleto()
    jugador['mazoRonda'] = jugador['mazoCompleto'].copy()  
    jugador['manoJugador'] = []
    jugador['monedas'] = []
    jugador['jokers'] = [
                            {"nombre": "Sota Traviesa", "descripcion": "Cada J (Sota) suma +120 fichas.", "tipo_bonificacion": "puntaje", "bonificacion": 120, "probabilidad": 0.36, "rareza": "raro"},
                            {"nombre": "Poker", "descripcion": "Si hay 4 cartas del mismo rango, multiplica x3.", "tipo_bonificacion": "multiplicar", "bonificacion": 3, "probabilidad": 0.28, "rareza": "raro"},
                            {"nombre": "Rey de Copas", "descripcion": "Cada Rey otorga +2 al multiplicador.", "tipo_bonificacion": "sum_multiplicador", "bonificacion": 2, "probabilidad": 0.30, "rareza": "raro"},

                            #Legendarios 
                            {"nombre": "Joker Comodín", "descripcion": "Full House duplica el multiplicador (x4).", "tipo_bonificacion": "multiplicar", "bonificacion": 4, "probabilidad": 0.12, "rareza": "legendario"},
                            {"nombre": "As de Picas", "descripcion": "Si hay As de picas, +500 fichas.", "tipo_bonificacion": "puntaje", "bonificacion": 500, "probabilidad": 0.10, "rareza": "legendario"},
                        ]
    jugador['combinaciones'] = {
                                "carta_alta": (5, 1),
                                "par": (100, 8),
                                "doble_par": (60, 7),
                                "trio": (40, 4),
                                "escalera": (35, 4),
                                "color": (30, 4),
                                "full_house": (30, 3),
                                "poker": (20, 2),
                                "escalera_corrida": (10, 2)
                            }
    

    return jugador
 
def nuevaRonda(jugador):
    jugador['manoJugador'] = []
    jugador['mazoRonda'] = jugador['mazoCompleto'].copy()
    jugador['ronda'] += 1
    jugador['pozo'] = round(jugador['pozo']*random.uniform(1.2,1.8))
    jugador['puntaje'] = 0
    jugador['manos'] = 5
    jugador['descartes'] = 3
    print()
    print(f"Jugador: {jugador['nombre']} | Pozo: {jugador['pozo']}")
    print()
    mazo.repartirCartas(10, jugador)
    juego.juego(jugador)