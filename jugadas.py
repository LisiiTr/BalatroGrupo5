import combinaciones
import jokers
import juego


def descartarCartas(seleccionCartas,jugador): #Descarte de cartas seleccionadas
    for carta in seleccionCartas:
        jugador['manoJugador'].remove(carta)
    return jugador
 
 
#Función lambda para calcular el puntaje total.
totalPuntaje= lambda cantidadFichas,multiplicador: cantidadFichas * multiplicador
 
def jugarCartas(jugador,cartasJugadas): #Jugar cartas seleccionadas
    juego.limpiarTerminal()

    
    try:
        fichas,multiplicador = calcularFichasMultiplicador(cartasJugadas,jugador)
        puntaje= totalPuntaje(fichas,multiplicador)
        jugador['puntaje'] += puntaje
    except Exception as e:
        print("Ha ocurrido un error: ",e)
    
    for carta in cartasJugadas:
        jugador['manoJugador'].remove(carta)

    print("╔═════════════════════════════════════════════════════════════╗")
    print("║                          Total                              ║")
    print("╠═════════════════╦══════════════════════╦════════════════════╣")
    print(f"║ Fichas: {fichas:<6}  ║ Multiplicador: {multiplicador:<5} ║ Puntaje: {puntaje:<9} ║")
    print("╚═════════════════╩══════════════════════╩════════════════════╝\n")


    input("Enter para continuar...")
    juego.limpiarTerminal()
    return jugador

def calcularFichasMultiplicador(cartasJugadas,jugador): #Calcular y mostrar fichas y multiplicador de la combinacion jugada
    try:
        cantFichas = [carta['fichas'] for carta in cartasJugadas]
        fichas,multiplicador = combinaciones.combinacionJugada(jugador,cartasJugadas)
        fichas += sum(cantFichas)
    except Exception as e:
        print("Ha ocurrido un error: ",e)

    print( "╠═══════════════════╦═══════════════════════╣")
    print(f"║ Fichas: {fichas:^9} ║ Multiplicador: {multiplicador:^6} ║")
    print( "╚═══════════════════╩═══════════════════════╝")

    fichas,multiplicador = jokers.calcularJokers(jugador,fichas, cartasJugadas, multiplicador)
    return fichas,multiplicador