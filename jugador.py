import random
import mazo
import juego

def crearJugador():
    jugador = {}
    jugador['nombre'] = input("Ingrese el nombre con el que va a jugar: ")
    jugador['puntaje'] = 0
    jugador['pozo'] = random.randint(300, 600)
    jugador['ronda'] = 1
    jugador['manos'] = 5
    jugador['descartes'] = 3
    jugador['mazoCompleto'] = mazo.crearMazoCompleto()
    jugador['mazoRonda'] = jugador['mazoCompleto'].copy()  
    jugador['manoJugador'] = []  
    return jugador
 
def nuevaRonda(jugador, mazoRonda):
    jugador['manoJugador'] = []
    jugador['mazoRonda'] = jugador['mazoCompleto'].copy()
    jugador['ronda'] += 1
    jugador['pozo'] = random.randint(300, 600)
    jugador['puntaje'] = 0
    jugador['manos'] = 5
    jugador['descartes'] = 3
    print()
    print(f"Jugador: {jugador['nombre']} | Pozo: {jugador['pozo']}")
    print()
    mazo.repartirCartas(10, jugador)
    juego.juego(jugador)
 
 