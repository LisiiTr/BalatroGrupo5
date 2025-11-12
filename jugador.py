import random
import mazo
import juego

def crearJugador():
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

def mostrarJokersJugador(jugador):
    if len(jugador["jokers"]) > 0:
        i=1
        for joker in jugador["jokers"]:
            print(f"{i}. {joker['nombre']}: {joker['nombre']}")
            i+=1
    else:
        print("No hay jokers adquiridos")


def sumarPuntajeRanking(jugador):
    jugador['puntaje_ranking'] += jugador['puntaje'] 