import random
import juego

def crearMazoCompleto(): #Creación del mazo
    palos = ["♠", "♥", "♦", "♣"]
    rangos = {
        "A": 1,
        "2": 2, "3": 3, "4": 4, "5": 5,
        "6": 6, "7": 7, "8": 8, "9": 9,
        "10": 10, "J": 11, "Q": 12, "K": 13
    }
    mazo = []
    for palo in palos:
        for etiqueta in rangos:
            valor= rangos[etiqueta]
            nombre=f"{etiqueta}{palo}"
            carta = {
                "nombre": nombre,
                "valor": valor,
                "palo": palo,
                "fichas": fichasValor(valor),
            }
            mazo.append(carta)
    return mazo
 
def fichasValor(valor): #Asignación de fichas a cada carta
    if valor == 1:        
        return 11
    elif 2 <= valor <= 10:
        return valor
    else: 
        return 10 
    

def mostrarCartas(listaCartas): #Se muestran las cartas en mano al usuario
    i=1
    linea1 = ""
    linea2 = ""
    linea3 = ""
    linea4 =""
    for c in listaCartas:
        linea1 += "┌───┐ "
        linea2 += f"|{c['nombre']:<3}| "
        linea3 += "└───┘ "
        linea4+= f"  {i}   "
        i+=1
    print(linea1)
    print(linea2)
    print(linea3)
    print(linea4)
 
def mostrarCartasSelect(listaCartas): #Se muestran las cartas seleccionadas por el usuario
    print("\nLas cartas seleccionadas son:")
    i=1
    linea1 = ""
    linea2 = ""
    linea3 = ""
    linea4 =""
    for c in listaCartas:
        linea1 += "┌───┐ "
        linea2 += f"|{c['nombre']:<3}| "
        linea3 += "└───┘ "
        linea4+= f"  {i}   "
        i+=1
    print(linea1)
    print(linea2)
    print(linea3)
    print(linea4)
 
def repartirCartas(cantCartas,jugador,imprimir): #Se reparten las cartas al jugador cada vez que sea necesario
    cartas_repartidas=[]
    for i in range(cantCartas):
        carta = random.choice(jugador['mazoRonda'])
        jugador['mazoRonda'].remove(carta)
        jugador['manoJugador'].append(carta)
        cartas_repartidas.append(carta)
    
    juego.limpiarTerminal()
    if imprimir:
        print("╔════════════════════════════════════════════════════════╗")
        print(f"║    Se agregaron a su mano las siguientes {cantCartas:<2} cartas:    ║")
        print("╚════════════════════════════════════════════════════════╝")
        mostrarCartas(cartas_repartidas)
        input("\nEnter para continuar...")
    
    return jugador 