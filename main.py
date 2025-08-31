import random

mazoCompleto=[
        "A♠","2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","J♠","Q♠","K♠",
        "A♥","2♥","3♥","4♥","5♥","6♥","7♥","8♥","9♥","10♥","J♥","Q♥","K♥",
        "A♦","2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦","10♦","J♦","Q♦","K♦",
        "A♣","2♣","3♣","4♣","5♣","6♣","7♣","8♣","9♣","10♣","J♣","Q♣","K♣"
        ]

manos = 5
descartes = 3
mazoRonda = mazoCompleto
manoJugador = []

def reiniciarMazo(mazoCompleto):
    return mazoCompleto


def repartir(mazoRonda,cantCartas,manoJugador):
    for i in range(cantCartas):
        print("entre",cantCartas)
        carta = random.choice(mazoRonda)
        manoJugador.append(carta)
        mazoRonda.remove(carta)
    return manoJugador

def descartarCartas(seleccionCartas,manoJugador,descartes):
    for carta in seleccionCartas:
        manoJugador.remove(carta)
    print(len(seleccionCartas))
    repartir(mazoRonda,len(seleccionCartas),manoJugador)
    descartes-=1
    seleccionarCartas(manoJugador,descartes)

def seleccionarCartas(manojugador,descartes):
    seleccionCartas=[]
    print("Las cartas en mano son:")
    for i in range(len(manoJugador)):
        print("carta",i+1,":",manoJugador[i])
    cartaSeleccionada=int(input("Seleccione una carta:"))
    while (cartaSeleccionada != -1) and (len(seleccionCartas) <= 5):
        seleccionCartas.append(manoJugador[cartaSeleccionada-1])
        print("Las cartas seleccionadas son:")
        for i in range(len(seleccionCartas)):
            print("carta",i+1,":",seleccionCartas[i])
        print("Las cartas en mano son:")
        for i in range(len(manoJugador)): 
            print("carta",i+1,":",manoJugador[i])
        cartaSeleccionada=int(input("Seleccione una carta o -1 para terminar:"))
    decision=int(input("Ingrese 1 si quiere jugar, o 2 si quiere descartar:"))
    while (decision < 1 or decision > 2) or descartes == 0:
        if descartes == 0:
            decision=int(input("No tiene mas descartes, debes ingresar 1 para jugar:"))
        else:
            decision=int(input("Valor invalido! Ingrese 1 si quiere jugar, o 2 si quiere descartar:"))
    if decision == 1:
        print("El jugador decidió jugar sus cartas")
    elif decision == 2 and descartes > 0:
        print("El jugador decidio descartar sus cartas")
        descartarCartas(seleccionCartas,manoJugador,descartes)
    
    

repartir(mazoRonda, 10,manoJugador)


print("Este es el mazo de la ronda:",mazoRonda)
print("Este es la mano del jugador:",manoJugador)

seleccionarCartas(manoJugador,descartes)
