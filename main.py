import random

#Variables declaradas
#mazoCompleto: contiene todas las cartas del mazo.
#manos: cantidad de veces que puede jugar combinaciones el user.
#descartes: cantidad de veces que puede descartar el user.
#mazoRonda: mazo de cada ronda, en donde se van eliminando las cartas que se le dan al jugador.
#manoJugador: cartas en mano que tiene el jugador, las cuales puede jugar o descartar.

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

#Esta funcion esta pensada para mas adelante poder reinciar los descarte, manos, mazos y demas.
def nuevaRonda(mazoCompleto):
    return mazoCompleto

#Esta funcion es para repartir las cartas. Recibe como parametros mazoRonda para se sepa las cartas que estan en juego, cantCartas para saber cuantas cartas repartir
# y mano jugador para agregar las cartas a la mano del jugador
#Repetimos el proceso la cantidad que me indica cantCartas
#Selecciono una carta al azar del mazo que se esta jugando en esta ronda
# #Agrego la carta al azar a la mano del jugador
#Elimino la carta del mazo en juego
def repartir(mazoRonda,cantCartas,manoJugador):
    for i in range(cantCartas):
        carta = random.choice(mazoRonda)
        manoJugador.append(carta)
        mazoRonda.remove(carta)

#Esta funcion es para cuando el jugador posterior a seleccionar las cartas, decide descartarlas.
#Recibe: seleccionCartas (Las cartas que se seleccionaron), manoJugador(las cartas que tiene el juagdor en la mano) y descartes(la cantidad de descartes que tiene el jugador)
#por cada carta seleccionada la elimino de la mano del jugador
#Invoco la funcion repartir, enviandole el mazo en juego, la cantidad de cartas que debe repartirle (el cual es la cantidad de cartas descartadas), y la mano del jugador.
#Lo envío nuevamente a la funcion para seleccionar cartas y que decida si jugar o descartar.
def descartarCartas(seleccionCartas,manoJugador,descartes):
    for carta in seleccionCartas:
        manoJugador.remove(carta)
    repartir(mazoRonda,len(seleccionCartas),manoJugador)
    descartes-=1
    juego(manoJugador,descartes)

#Esta funcion es el nucleo del juego, en donde se seleccionan las cartas y se decide si jugar o descartar.
#Se inicializa la variable seleccionCartas, la cual es una lista que contiene las cartas seleccionadas por el jugador. Se le muestran las cartas que puede seleccionar.
# recorriendo las lista manoJugador (las cartas que tiene en mano).
#Se le pide seleccionar 1 carta, ingresa a un while, que mientras cartaSeleccionada sea distinto a -1 o el largo de la lista seleccionCartas sea menor o igual a 5
# agregue la carta que selecciono el usuario, muestre las cartas seleccionadas y las cartas que tiene en la mano, para que pueda elegir nuevamente o ingresar -1 para salir y
# decidir si jugar o descartar.
#Cuando sale del while, es decir, cartaSeleccionada sea -1 o el largo de la lista seleccionCartas es menor o igual a 5, se le pide que ingrese si quiere jugar o descartar.
#Se verifica que la decision se valida y ademas que tenga descartes disponibles. Si una de estas dos no cumple, debe ingresar nuevamente.
#Dependiendo de la decision tomada, se invoca la función descartarCartas o jugarCartas.
def juego(manojugador,descartes):
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

# Funcion de jugarCartas, esta funcion sera la que deduzca la combinación
def jugarCartas(cartasJugadas):

    return True
 
# Funcion que determinara que combinación se jugo.
def combinacionnJugada(cartasJugadas):
    combinacion = []
    return combinacion
 
#Calculara las fichas que suman las cartas.
def calcularFichas(cartasJugadas, combinacion):
    cantidadFichas = 0
    return cantidadFichas
 
#Calculara el multiplicador de la jugada.
def calcularMultiplicador(combinacion, jokers):
    multiplicador = 0
    return multiplicador
 
#Calculara el puntaje total de la jugada
def calcularPuntaje(cantidadFichas,multiplicador):
    totalPuntaje = 0
    return totalPuntaje
 
#recorrera las cartas en mano y las mostrara en pantalla
def mostrarCartas(listaCartas):
    print("mostrará las cartas en mano")
 
#recorrera las cartas seleccionadas y las mostrara en pantalla
def mostrarCartasSelect(listaCartas):
    print("mostrará las cartas seleccionadas")
 
#Funcion para seleccionar las cartas. Debera recibir las cartas en mano del jugador e ir seleccionando las cartas que quiere jugar o descartar.
def seleccionar(manoJugador):
    cartasSeleccionadas = []
    return cartasSeleccionadas
 
#Esta función determinara el funcionamiento de la tienda
def tienda():
    sobre = 0
    return sobre
 
 
def eleccionAdquisicion():
    joker = []
    return joker
    

#Body del programa, para repartir e inicializar el juego.
repartir(mazoRonda, 10,manoJugador)

juego(manoJugador,descartes)
