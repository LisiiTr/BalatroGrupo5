import random

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
    

def mostrarCartas(listaCartas):
    print("\nLas cartas en mano son:")
    i=1
    linea1 = ""
    linea2 = ""
    linea3 = ""
    linea4 =""
    for c in listaCartas:
        linea1 += "┌─────┐ "
        linea2 += f"| {c['nombre']:<3} | "
        linea3 += "└─────┘ "
        linea4+= f"-- {i} -- "
        i+=1
    print(linea1)
    print(linea2)
    print(linea3)
    print(linea4)
 
def mostrarCartasSelect(listaCartas):
    print("\nLas cartas seleccionadas son:")
    i=1
    linea1 = ""
    linea2 = ""
    linea3 = ""
    linea4 =""
    for c in listaCartas:
        linea1 += "┌─────┐ "
        linea2 += f"| {c['nombre']:<3} | "
        linea3 += "└─────┘ "
        linea4+= f"-- {i} -- "
        i+=1
    print(linea1)
    print(linea2)
    print(linea3)
    print(linea4)
 
def repartirCartas(cantCartas,jugador):
    for i in range(cantCartas):
        indice = random.choice(list(jugador['mazoRonda']))
        carta = jugador['mazoRonda'].pop(indice)
        jugador['manoJugador'].append(carta)
 