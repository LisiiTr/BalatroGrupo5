import random

#
# Representación de carta:
#   {"nombre": "A♠", "valor": 1, "palo": "♠", "fichas": 11}
# Claves:
#   - nombre :   (etiqueta mostrable, p.ej. "A♠")
#   - valor  :   (A=1, 2..10, J=11, Q=12, K=13)
#   - palo   :   ("♠", "♥", "♦", "♣")
#   - fichas :   (A=11; 2..10 ; J/Q/K -> 10)
#                
 
#Inicializaciín / Reinicio de variables
def crearMazoCompleto():
    palos = ["♠", "♥", "♦", "♣"]
    rangos = {
        "A": 1,
        "2": 2, "3": 3, "4": 4, "5": 5,
        "6": 6, "7": 7, "8": 8, "9": 9,
        "10": 10, "J": 11, "Q": 12, "K": 13
    }
    mazo = {}
    for palo in palos:
        for etiqueta in rangos:
            valor= rangos[etiqueta]
            nombre=f"{etiqueta}{palo}"
            mazo[nombre] = {
                "nombre": nombre,
                "valor": valor,
                "palo": palo,
                "fichas": fichasValor(valor),
            }
    return mazo
 
def fichasValor(valor):
    if valor == 1:        
        return 11
    elif 2 <= valor <= 10:
        return valor
    else: 
        return 10  
 
def crearJugador():
    jugador = {}
    jugador['nombre'] = input("Ingrese el nombre con el que va a jugar: ")
    jugador['puntaje'] = 0
    jugador['pozo'] = random.randint(300, 600)
    jugador['ronda'] = 1
    jugador['manos'] = 5
    jugador['descartes'] = 3
    jugador['mazoCompleto'] = crearMazoCompleto()
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
    repartirCartas(10, jugador)
    juego(jugador)
 
 
 
def mostrarCartas(listaCartas):
    print("\nLas cartas en mano son:")
    i=1
    for carta in listaCartas:
        print(f"Carta {i}: {carta['nombre']} | Fichas: {carta['fichas']}")
        i += 1
 
def mostrarCartasSelect(listaCartas):
    print("\nLas cartas seleccionadas son:")
    i=1
    for carta in listaCartas:
        print(f"Carta seleccionada {i}: {carta['nombre']} | Fichas: {carta['fichas']}")
        i += 1
 
def repartirCartas(cantCartas,jugador):
    for i in range(cantCartas):
        indice = random.choice(list(jugador['mazoRonda']))
        carta = jugador['mazoRonda'].pop(indice)
        jugador['manoJugador'].append(carta)
 
 
# Flujo principal
def juego(jugador):
    while jugador['manos'] != 0 and jugador['puntaje'] < jugador['pozo']:
        seleccionCartas=[]
        print()
        print("----------------------------------------------------------------")
        print(f"Jugador: {jugador['nombre']} | Puntaje / Pozo: {jugador['puntaje']}/{jugador['pozo']}")
        print("----------------------------------------------------------------")
        print()
 
        mostrarCartas(jugador['manoJugador'])
        cartaSeleccionada=int(input("\nSeleccione una carta:"))
 
        while (cartaSeleccionada != -1) and (len(seleccionCartas) < 4):
            seleccionCartas.append(jugador['manoJugador'][cartaSeleccionada-1])
           
            mostrarCartasSelect(seleccionCartas)
           
            mostrarCartas(jugador['manoJugador'])
       
            cartaSeleccionada=int(input("\nSeleccione una carta o -1 para terminar:"))
        decision=int(input("Ingrese 1 si quiere jugar, o 2 si quiere descartar:"))
        while (decision < 1 or decision > 2) or jugador['descartes'] == 0:
            if jugador['descartes'] == 0:
                decision=int(input("No tiene mas descartes, debes ingresar 1 para jugar:"))
            else:
                decision=int(input("Valor invalido! Ingrese 1 si quiere jugar, o 2 si quiere descartar:"))
        if decision == 1:
            print("El jugador decidió jugar sus cartas")
            jugarCartas(jugador,seleccionCartas)
            jugador['manos'] -= 1
        elif decision == 2 and jugador['descartes'] > 0:
            print("El jugador decidio descartar sus cartas")
            descartarCartas(seleccionCartas,jugador)
            jugador['descartes'] -= 1
        repartirCartas(len(seleccionCartas),jugador)
    if jugador['puntaje'] < jugador['pozo'] and jugador['manos'] == 0:
        print("¡Te quedaste sin manos y no alcanzate el pozo! Perdiste.")
        print(f"Ultima ronda alcanzada:{jugador['ronda']} ¡Hasta la próxima!")
    elif jugador['puntaje'] >= jugador['pozo']:
        print()
        print("----------------------------------------------------------------")
        print("¡Alcanzaste el valor del pozo! Ganaste.")
        print("----------------------------------------------------------------")
        print()
        jugar=int(input("Quiere jugar otra ronda? 1 para 'Si' 2 para 'No':"))
        while jugar != 1 and jugar != 2:
            print("¡Opción invalida!")
            jugar=int(input("Quiere jugar otra ronda? 1 para 'Si' 2 para 'No':"))
        if jugar == 1:
            nuevaRonda(jugador)
        else:
            print()
            print("----------------------------------------------------------------")
            print(f"Ultima ronda alcanzada:{jugador['ronda']} ¡Hasta la próxima!")
            print("----------------------------------------------------------------")
            print()
 
#Descartes
def descartarCartas(seleccionCartas,jugador):
    for carta in seleccionCartas:
        jugador['manoJugador'].remove(carta)
    return jugador['manoJugador']
 
 
#Funciones de cuando se juega la mano
totalPuntaje= lambda cantidadFichas,multiplicador: cantidadFichas * multiplicador
 
def jugarCartas(jugador,cartasJugadas):
    fichas,multiplicador = combinacionJugada(cartasJugadas)
    fichas += calcularFichas(cartasJugadas)
    puntaje= totalPuntaje(fichas,multiplicador)
    jugador['puntaje'] += puntaje
    for carta in cartasJugadas:
        jugador['manoJugador'].remove(carta)
    print(f"Fichas: {fichas} | Multiplicador: {multiplicador} | Puntaje de la jugada: {puntaje}")
    print("----------------------------------------------------------------")
    print()
   
def calcularFichas(cartasJugadas):
 
 
 
    fichas = [carta['fichas'] for carta in cartasJugadas]
    cantidadFichas = sum(fichas)
    return cantidadFichas
 
def dividirPaloValores(cartasJugadas):
    valores = [cartasJugadas['valor'] for cartasJugadas in cartasJugadas]
    palos   = [cartasJugadas['palo']  for cartasJugadas in cartasJugadas]
 
    return valores,palos
 
def combinacionJugada(cartasJugadas):
    valores, palos = dividirPaloValores(cartasJugadas)
    valores.sort()
 
    es_escalera = escalera(valores)
    es_poker = poker(valores)
    es_color = color(palos)
    es_trio = trio(valores)
    es_par = par(valores)
    es_doblePar = doblePar(valores)
    es_fullHouse = fullHouse(valores)
 
    if es_escalera and es_color:
        print()
        print("----------------------------------------------------------------")
        print("La combinación jugada es: Escalera Corrida")
        return 100, 8
    elif es_poker:
        print()
        print("----------------------------------------------------------------")
        print("La combinación jugada es: Poker")
        return 60, 7
    elif es_fullHouse:
        print()
        print("----------------------------------------------------------------")
        print("La combinación jugada es: Full house")
        return 40, 4
    elif es_color and (not es_escalera):
        print()
        print("----------------------------------------------------------------")
        print("La combinación jugada es: Color")
        return 35, 4
    elif es_escalera and (not es_color):
        print()
        print("----------------------------------------------------------------")
        print("La combinación jugada es: Escalera")
        return 30, 4
    elif es_trio:
        print()
        print("----------------------------------------------------------------")
        print("La combinación jugada es: Trio")
        return 30, 3
    elif es_doblePar:
        print()
        print("----------------------------------------------------------------")
        print("La combinación jugada es: Doble Par")
        return 20, 2
    elif es_par:
        print()
        print("----------------------------------------------------------------")
        print("La combinación jugada es: Par")
        return 10, 2
    else:
        print()
        print("----------------------------------------------------------------")
        print("La combinación jugada es: Carta Alta")
        return 5, 1
 
# Combinaciones
def escalera(valores):
    if len(valores) == 5:
        for i in range(len(valores) - 1):
            if valores[i] + 1 != valores[i + 1]:
                return False
        return True
    else:
        return False
 
def color(palos):
    if len(palos) == 5:
        if palos.count(palos[1]) == 5:
            return True
    return False
 
def poker(valores):
    for v in valores:
        if valores.count(v) == 4:
            return True
    return False
 
def par(valores):
    for v in valores:
        if valores.count(v) == 2:
            return True
    return False
 
def doblePar(valores):
    cantPares = []
    for v in valores:
        if valores.count(v) == 2:
            cantPares.append(v)
    return len(cantPares) == 2
 
def trio(valores):
    for v in valores:
        if valores.count(v) == 3:
            return True
    return False
 
def fullHouse(valores):
    cantPares = []
    cantTrios = []
    for v in valores:
        if valores.count(v) == 3:
            cantTrios.append(v)
    for v in valores:
        if valores.count(v) == 2:
            cantPares.append(v)
    return len(cantTrios) == 1 and len(cantPares) == 1
 
 
# Función del programa principal
 
def main():
    
    jugador = crearJugador()
 
    repartirCartas(10, jugador)
    juego(jugador)
 
 
 
main()
 