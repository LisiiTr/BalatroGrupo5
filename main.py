import random

mazoCompleto=[
        "A♠","2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","J♠","Q♠","K♠",
        "A♥","2♥","3♥","4♥","5♥","6♥","7♥","8♥","9♥","10♥","J♥","Q♥","K♥",
        "A♦","2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦","10♦","J♦","Q♦","K♦",
        "A♣","2♣","3♣","4♣","5♣","6♣","7♣","8♣","9♣","10♣","J♣","Q♣","K♣"
        ]

manos = 5
descartes = 3
mazoRonda = []
manoJugador = []

def crearMazo(mazoCompleto):
    return mazoCompleto


def repartir(mazoRonda,cantCartas):
    mazoJugador=[]
    for i in range(cantCartas):
        carta = random.choice(mazoRonda)
        mazoJugador.append(carta)
        mazoRonda.remove(carta)
    return mazoJugador


mazoRonda = crearMazo(mazoCompleto)

manoJugador = repartir(mazoRonda, 10)

print("Este es el mazo de la ronda:",mazoRonda)
print("Este es la mano del jugador:",manoJugador)