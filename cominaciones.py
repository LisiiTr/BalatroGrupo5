 
def dividirPaloValores(cartasJugadas):
    valores = [cartasJugadas['valor'] for cartasJugadas in cartasJugadas]
    palos   = [cartasJugadas['palo']  for cartasJugadas in cartasJugadas]
 
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
