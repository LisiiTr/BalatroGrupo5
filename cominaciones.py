 
def dividirPaloValores(cartasJugadas):
    valores = [carta["valor"] for carta in cartasJugadas]
    palos   = [carta["palo"]  for carta in cartasJugadas]
 
    return valores,palos
 
 
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
            if v not in cantPares:
                cantPares.append(v)
    if len(cantPares) == 2:
        return True
    else:
        return False
 
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
    if len(cantTrios) == 1 and len(cantPares) == 1:
        return True
    else:
        return False

def combinacionJugada(jugador, cartasJugadas):
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
        return jugador['combinaciones']["escalera_corrida"]
    elif es_poker:
        print()
        print("----------------------------------------------------------------")
        print("La combinación jugada es: Poker")
        return jugador['combinaciones']["poker"]
    elif es_fullHouse:
        print()
        print("----------------------------------------------------------------")
        print("La combinación jugada es: Full house")
        return jugador['combinaciones']["full_house"]
    elif es_color and (not es_escalera):
        print()
        print("----------------------------------------------------------------")
        print("La combinación jugada es: Color")
        return jugador['combinaciones']["color"]
    elif es_escalera and (not es_color):
        print()
        print("----------------------------------------------------------------")
        print("La combinación jugada es: Escalera")
        return jugador['combinaciones']["escalera"]
    elif es_trio:
        print()
        print("----------------------------------------------------------------")
        print("La combinación jugada es: Trio")
        return jugador['combinaciones']["trio"]
    elif es_doblePar:
        print()
        print("----------------------------------------------------------------")
        print("La combinación jugada es: Doble Par")
        return jugador['combinaciones']["doble_par"]
    elif es_par:
        print()
        print("----------------------------------------------------------------")
        print("La combinación jugada es: Par")
        return jugador['combinaciones']["par"]
    else:
        print()
        print("----------------------------------------------------------------")
        print("La combinación jugada es: Carta Alta")
        return jugador['combinaciones']["carta_alta"]


def analizarCombinacionesJokers(cartasJugadas):
    valores, palos = dividirPaloValores(cartasJugadas)
    valores.sort()
    combinaciones={
        "escalera_corrida": False,
        "escalera": False,
        "poker": False,
        "color": False,
        "trio": False,
        "par": False,
        "doble_par": False,
        "full_house": False,
        "carta_alta": False
    }
    es_escalera = escalera(valores)
    es_poker = poker(valores)
    es_color = color(palos)
    es_trio = trio(valores)
    es_par = par(valores)
    es_doblePar = doblePar(valores)
    es_fullHouse = fullHouse(valores)
    
    if es_color and es_escalera:
        combinaciones["escalera_corrida"] = True
    combinaciones["poker"] = es_poker
    combinaciones["full_house"] = es_fullHouse
    combinaciones["color"] = es_color
    combinaciones["escalera"] = es_escalera
    combinaciones["trio"] = es_trio
    combinaciones["doble_par"] = es_doblePar
    combinaciones["par"]  = es_par

    return combinaciones