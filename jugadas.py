import combinaciones
import jokers
import  os


# contempla tanto windows, como linux y macos
def limpiarTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def descartarCartas(seleccionCartas,jugador):
    print(jugador['manoJugador'])
    for carta in seleccionCartas:
        print(carta)
        jugador['manoJugador'].remove(carta)
    return jugador
 
 

totalPuntaje= lambda cantidadFichas,multiplicador: cantidadFichas * multiplicador
 
def jugarCartas(jugador,cartasJugadas):
    limpiarTerminal()
    
    try:
        fichas,multiplicador = calcularFichasMultiplicador(cartasJugadas,jugador)
        puntaje= totalPuntaje(fichas,multiplicador)
        jugador['puntaje'] += puntaje
    except Exception as e:
        print("Ha ocurrido un error: ",e)
    
    for carta in cartasJugadas:
        jugador['manoJugador'].remove(carta)
    print("<---------------------------------------------------------------->")
    print(f"Fichas: {fichas} | Multiplicador: {multiplicador} | Puntaje de la jugada: {puntaje}")
    print("<---------------------------------------------------------------->")
    print()
    return jugador

def calcularFichasMultiplicador(cartasJugadas,jugador):
    try:
        cantFichas = [carta['fichas'] for carta in cartasJugadas]
        fichas,multiplicador = combinaciones.combinacionJugada(jugador,cartasJugadas)
        fichas += sum(cantFichas)
    except Exception as e:
        print("Ha ocurrido un error: ",e)

    print(f"Las fichas por la combinación son: {fichas}   |   El multiplicador develto por la combinación es: {multiplicador}")
    fichas,multiplicador = jokers.calcularJokers(jugador,fichas, cartasJugadas, multiplicador)
    return fichas,multiplicador