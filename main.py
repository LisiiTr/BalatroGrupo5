import random

## Tuplas: ("A♠",  1,    "♠" ,   11)
## Diccionario : (Nombre: "A♠", Valor: 1, Palo:"♠", fichas:11)
'''
    A   = 1
    2   = 2
    3   = 3
    4   = 4
    5   = 5
    6   = 6
    7   = 7
    8   = 8
    9   = 9
    10  = 10 
    J   = 11 
    Q   = 12
    K   = 13

    Escalera minima: A 2 3 4 5
    Escalera maxima 9 10 J Q K
'''



#Variables declaradas
#mazoCompleto: contiene todas las cartas del mazo.
#manos: cantidad de veces que puede jugar combinaciones el user.
#descartes: cantidad de veces que puede descartar el user.
#mazoRonda: mazo de cada ronda, en donde se van eliminando las cartas que se le dan al jugador.
#manoJugador: cartas en mano que tiene el jugador, las cuales puede jugar o descartar.

mazoCompleto=[
        ("A♠",  1,    "♠" ,   11),("2♠",  2,    "♠" ,   2),("3♠",   3,    "♠" ,    3),("4♠",  4,    "♠" ,    4),("5♠",  5,    "♠" ,   5),("6♠",  6,    "♠" ,   6),("7♠",  7,    "♠" ,   7),("8♠",   8,    "♠" ,    8),("9♠",  9,    "♠" ,    9),("10♠",  10,    "♠" ,   10),("J♠",  11,    "♠" ,   10),("Q♠",  12,    "♠" ,   10),("K♠",  13,    "♠" ,   10),
        ("A♥",  1,    "♥" ,   11),("2♥",  2,    "♥" ,   2),("3♥",   3,    "♥" ,    3),("4♥",  4,    "♥" ,    4),("5♥",  5,    "♥" ,   5),("6♥",  6,    "♥" ,   6),("7♥",  7,    "♥" ,   7),("8♥",   8,    "♥" ,    8),("9♥",  9,    "♥" ,    9),("10♥",  10,    "♥" ,   10),("J♥",  11,    "♥" ,   10),("Q♥",  12,    "♥" ,   10),("K♥",  13,    "♥" ,   10),
        ("A♦",  1,    "♦" ,   11),("2♦",  2,    "♦" ,   2),("3♦",   3,    "♦" ,    3),("4♦",  4,    "♦" ,    4),("5♦",  5,    "♦" ,   5),("6♥",  6,    "♦" ,   6),("7♦",  7,    "♦" ,   7),("8♦",   8,    "♦" ,    8),("9♦",  9,    "♦" ,    9),("10♦",  10,    "♦" ,   10),("J♦",  11,    "♦" ,   10),("Q♦",  12,    "♦" ,   10),("K♦",  13,    "♦" ,   10),
        ("A♣",  1,    "♣" ,   11),("2♣",  2,    "♣" ,   2),("3♣",   3,    "♣" ,    3),("4♣",  4,    "♣" ,    4),("5♣",  5,    "♣" ,   5),("6♣",  6,    "♣" ,   6),("7♣",  7,    "♣" ,   7),("8♣",   8,    "♣" ,    8),("9♣",  9,    "♣" ,    9),("10♣",  10,    "♣" ,   10),("J♣",  11,    "♣" ,   10),("Q♣",  12,    "♣" ,   10),("K♣",  13,    "♣" ,   10),
        ]

mazoRonda = mazoCompleto
manoJugador = []

def crearJugador():
    jugador={}
    jugador['nombre']= input("Ingrese el nombre con el que va a jugar:")
    jugador['puntaje']=0
    jugador['pozo']= random.randint(300,600)
    jugador['ronda']=1
    jugador['manos']=3
    jugador['descartes']=3
    return jugador


#Esta funcion esta pensada para mas adelante poder reinciar los descarte, manos, mazos y demas.
def nuevaRonda(jugador,mazoCompleto):
    manoJugador=[]
    mazoRonda=mazoCompleto
    jugador['ronda'] += 1
    jugador['pozo'] = random.randint(300,600)
    jugador['puntaje'] = 0
    jugador['manos']=3
    jugador['descartes']=3
    print()
    print(f"Jugador:{jugador['nombre']} | Pozo:{jugador['pozo']}")
    print()
    repartirCartas(mazoRonda,10,manoJugador)
    juego(jugador,manoJugador)
#Esta funcion es para repartir las cartas. Recibe como parametros mazoRonda para se sepa las cartas que estan en juego, cantCartas para saber cuantas cartas repartir
# y mano jugador para agregar las cartas a la mano del jugador
#Repetimos el proceso la cantidad que me indica cantCartas
#Selecciono una carta al azar del mazo que se esta jugando en esta ronda
# #Agrego la carta al azar a la mano del jugador
#Elimino la carta del mazo en juego
def repartirCartas(mazoRonda,cantCartas,manoJugador):
    for i in range(cantCartas):
        carta = random.choice(mazoRonda)
        manoJugador.append(carta)
        mazoRonda.remove(carta)

#Esta funcion es para cuando el jugador posterior a seleccionar las cartas, decide descartarlas.
#Recibe: seleccionCartas (Las cartas que se seleccionaron), manoJugador(las cartas que tiene el juagdor en la mano) y descartes(la cantidad de descartes que tiene el jugador)
#por cada carta seleccionada la elimino de la mano del jugador
#Invoco la funcion repartir, enviandole el mazo en juego, la cantidad de cartas que debe repartirle (el cual es la cantidad de cartas descartadas), y la mano del jugador.
#Lo envío nuevamente a la funcion para seleccionar cartas y que decida si jugar o descartar.
def descartarCartas(seleccionCartas,manoJugador):
    for carta in seleccionCartas:
        manoJugador.remove(carta)
    return manoJugador


# Funcion de jugarCartas, esta funcion sera la que deduzca la combinación
def jugarCartas(jugador,cartasJugadas,manoJugador):
    fichas,multiplicador = combinacionJugada(cartasJugadas)
    fichas += calcularFichas(cartasJugadas)
    puntaje = calcularPuntaje(fichas,multiplicador)
    jugador['puntaje'] += puntaje
    for carta in cartasJugadas:
        manoJugador.remove(carta)
    print("Fichas: ",fichas," | Multiplicador: ",multiplicador, " | Puntaje de la jugada: ", puntaje)
    

#Esta funcion es el nucleo del juego, en donde se seleccionan las cartas y se decide si jugar o descartar.
#Se inicializa la variable seleccionCartas, la cual es una lista que contiene las cartas seleccionadas por el jugador. Se le muestran las cartas que puede seleccionar.
# recorriendo las lista manoJugador (las cartas que tiene en mano).
#Se le pide seleccionar 1 carta, ingresa a un while, que mientras cartaSeleccionada sea distinto a -1 o el largo de la lista seleccionCartas sea menor o igual a 5
# agregue la carta que selecciono el usuario, muestre las cartas seleccionadas y las cartas que tiene en la mano, para que pueda elegir nuevamente o ingresar -1 para salir y
# decidir si jugar o descartar.
#Cuando sale del while, es decir, cartaSeleccionada sea -1 o el largo de la lista seleccionCartas es menor o igual a 5, se le pide que ingrese si quiere jugar o descartar.
#Se verifica que la decision se valida y ademas que tenga descartes disponibles. Si una de estas dos no cumple, debe ingresar nuevamente.
#Dependiendo de la decision tomada, se invoca la función descartarCartas o jugarCartas.
def juego(jugador,manoJugador):
    while jugador['manos'] != 0 and jugador['puntaje'] < jugador['pozo']:
        seleccionCartas=[]
        mostrarCartas(manoJugador)
        cartaSeleccionada=int(input("Seleccione una carta:"))

        while (cartaSeleccionada != -1) and (len(seleccionCartas) <= 5):
            seleccionCartas.append(manoJugador[cartaSeleccionada-1])
            
            mostrarCartasSelect(seleccionCartas)
            
            mostrarCartas(manoJugador)
        
            cartaSeleccionada=int(input("Seleccione una carta o -1 para terminar:"))
        decision=int(input("Ingrese 1 si quiere jugar, o 2 si quiere descartar:"))
        while (decision < 1 or decision > 2) or jugador['descartes'] == 0:
            if jugador['descartes'] == 0:
                decision=int(input("No tiene mas descartes, debes ingresar 1 para jugar:"))
            else:
                decision=int(input("Valor invalido! Ingrese 1 si quiere jugar, o 2 si quiere descartar:"))
        if decision == 1:
            print("El jugador decidió jugar sus cartas")
            jugarCartas(jugador,seleccionCartas,manoJugador)
            repartirCartas(mazoRonda,len(seleccionCartas),manoJugador)
            jugador['manos'] -= 1
        elif decision == 2 and jugador['descartes'] > 0:
            print("El jugador decidio descartar sus cartas")
            descartarCartas(seleccionCartas,manoJugador)
            repartirCartas(mazoRonda,len(seleccionCartas),manoJugador)
            jugador['descartes'] -= 1
            
    if jugador['puntaje'] < jugador['pozo'] and jugador['manos'] == 0:
        print("¡Te quedaste sin manos y no alcanzate el pozo! Perdiste.")
        print(f"Ultima ronda alcanzada:{jugador['ronda']} ¡Hasta la próxima!")
    elif jugador['puntaje'] >= jugador['pozo']:
        print("¡Alcanzaste el valor del pozo! Ganaste.")
        jugar=int(input("Quiere jugar otra ronda? 1 para 'Si' 2 para 'No':"))
        while jugar != 1 and jugar != 2:
            print("¡Opción invalida!")
            jugar=int(input("Quiere jugar otra ronda? 1 para 'Si' 2 para 'No':"))
        if jugar == 1:
            nuevaRonda(jugador,mazoCompleto)
        else:
            print(f"Ultima ronda alcanzada:{jugador['ronda']} ¡Hasta la próxima!")
        


 
#Calculara las fichas que suman las cartas.
def calcularFichas(cartasJugadas):
  
    cantidadFichas = 0
    for carta in cartasJugadas:
        cantidadFichas += carta[3]
    return cantidadFichas
 
#Calculara el puntaje total de la jugada
def calcularPuntaje(cantidadFichas,multiplicador):
    totalPuntaje = cantidadFichas * multiplicador
    return totalPuntaje
 
#recorrera las cartas en mano y las mostrara en pantalla
def mostrarCartas(listaCartas):
    print("Las cartas en mano son:")
    for i in range(len(manoJugador)): 
        print("carta",i+1,":",manoJugador[i])
 
#recorrera las cartas seleccionadas y las mostrara en pantalla
def mostrarCartasSelect(listaCartas):
    print("Las cartas seleccionadas son:")
    for i in range(len(listaCartas)):
        print("carta",i+1,":",listaCartas[i])
 
#Funcion para seleccionar las cartas. Debera recibir las cartas en mano del jugador e ir seleccionando las cartas que quiere jugar o descartar.
def seleccionar(manoJugador):
    cartasSeleccionadas = []
    return cartasSeleccionadas
 

def dividirPaloValores(cartasJugadas):
    valores=[]
    palos=[]
    for nombre,valor, palo, fichas in cartasJugadas:
        valores.append(valor)
        palos.append(palo)
    return valores,palos

    #valores=[1,2,3,4,5]
    #palos=["♠","♠","♠","♠","♠"]

def escalera(valores):
    #valores=[1,2,3,4,5]
    if len(valores)==5:
        for i in range(len(valores)-1):
            if valores[i] + 1 != valores[i+1]:
                return False
        return True
    else:
        return False
 
def color (palos):
    if len(palos)==5:
        for i in range(len(palos)-1):
            if palos[i] != palos[i+1]:
                return False
        return True
    else:
        return False

def poker(valores):
    for v in valores:
        #valores=[1,1,1,1,5]
        if valores.count(v) == 4:
            return True
    return False

def par(valores):
    #valores=[1,2,3,3,5]
    for v in valores:
        if valores.count(v) == 2:
            return True 
    return False

def doblePar(valores):
    cantPares=[]
    #valores=[2,2,3,3,5]
    for v in valores:
        if valores.count(v) == 2:
            #pares=[2,3]
            if v not in cantPares:
                cantPares.append(v)    
    if len(cantPares) == 2:
        return True
    return False

def trio(valores):
    for v in valores:
        if valores.count(v) == 3:
            return True
    return False

def fullHouse(valores):
    cantPares=[]
    cantTrios=[]

    for v in valores:
        if valores.count(v) == 3:
            if v not in cantTrios:
                cantTrios.append(v)
    for v in valores:
        if valores.count(v) == 2:
            if v not in cantPares:
                cantPares.append(v)

    if len(cantTrios)==1 and len(cantPares)==1:
        return True
    else:
        return False

def combinacionJugada(cartasJugadas):

    valores,palos = dividirPaloValores(cartasJugadas)

    valores.sort()

    es_escalera = escalera(valores)
    es_poker = poker(valores)
    es_color = color(palos)
    es_trio = trio(valores)
    es_par = par(valores)
    es_doblePar = doblePar(valores)
    es_fullHouse = fullHouse(valores)

    if es_escalera and es_color:
        print("Es: Escalera Corrida")
        return 100 , 8
    elif es_poker:
        print("Es: Poker")
        return 60 , 7
    elif es_fullHouse:
        print("Es: Full house")
        return 40 , 4
    elif es_color and (not es_escalera):
        print("Es: Color")
        return 35 , 4
    elif es_escalera and (not es_color):
        print("Es: Escalera")
        return 30 ,4
    elif es_trio:
        print("Es: Trio")
        return 30 , 3
    elif es_doblePar:
        print("Es: Doble Par")
        return 20 , 2
    elif es_par:
        print("Es: Par")
        return 10 , 2
    else:
        print("Es: Carta Alta")
        return 5 , 1
    

#Body del programa, para repartir e inicializar el juego.
jugador= crearJugador()

print()
print(f"Jugador:{jugador['nombre']} | Pozo:{jugador['pozo']}")
print()

repartirCartas(mazoRonda, 10,manoJugador)

juego(jugador,manoJugador)
