import cominaciones


def descartarCartas(seleccionCartas,jugador):
    print(jugador['manoJugador'])
    for carta in seleccionCartas:
        print(carta)
        jugador['manoJugador'].remove(carta)
    return jugador
 
 

totalPuntaje= lambda cantidadFichas,multiplicador: cantidadFichas * multiplicador
 
def jugarCartas(jugador,cartasJugadas):
    fichas,multiplicador = cominaciones.combinacionJugada(cartasJugadas)
    fichas += calcularFichas(cartasJugadas)
    puntaje= totalPuntaje(fichas,multiplicador)
    jugador['puntaje'] += puntaje
    for carta in cartasJugadas:
        jugador['manoJugador'].remove(carta)
    print(f"Fichas: {fichas} | Multiplicador: {multiplicador} | Puntaje de la jugada: {puntaje}")
    print("----------------------------------------------------------------")
    print()
    return jugador
   
def calcularFichas(cartasJugadas):
    fichas = [carta['fichas'] for carta in cartasJugadas]
    cantidadFichas = sum(fichas)
    return cantidadFichas