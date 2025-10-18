import mazo
import jugadas
import jugador as usuario
import  os


# contempla tanto windows, como linux y macos
def limpiarTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def selectorCartas(jugador):
    seleccionCartas=[]
    mazo.mostrarCartas(jugador['manoJugador'])
    cartaSeleccionada=int(input("\nSeleccione una carta:"))
    while (cartaSeleccionada != -1) and (len(seleccionCartas) < 5):
        limpiarTerminal()
        if jugador['manoJugador'][cartaSeleccionada-1] in seleccionCartas:
            seleccionCartas.remove(jugador['manoJugador'][cartaSeleccionada-1])  
        else:
            seleccionCartas.append(jugador['manoJugador'][cartaSeleccionada-1])
        mazo.mostrarCartasSelect(seleccionCartas)
        if len(seleccionCartas) == 5:
            break
        else:
            mazo.mostrarCartas(jugador['manoJugador'])
            cartaSeleccionada=int(input("\nSeleccione una carta o -1 para terminar:"))
    return seleccionCartas

def juego(jugador):
    while jugador['manos'] != 0 and jugador['puntaje'] < jugador['pozo']:
        seleccionCartas=[]

        print()
        print("----------------------------------------------------------------")
        print(f"Jugador: {jugador['nombre']} | Puntaje / Pozo: {jugador['puntaje']}/{jugador['pozo']}")
        print("----------------------------------------------------------------")
        print()

        seleccionCartas= selectorCartas(jugador)

        decision=int(input("Ingrese 1 si quiere jugar, o 2 si quiere descartar:"))
        while (decision < 1 or decision > 2) or jugador['descartes'] == 0:
            if jugador['descartes'] == 0:
                decision=int(input("No tiene mas descartes, debes ingresar 1 para jugar:"))
            else:
                decision=int(input("Valor invalido! Ingrese 1 si quiere jugar, o 2 si quiere descartar:"))
        if decision == 1:
            print("El jugador decidió jugar sus cartas")
            jugadas.jugarCartas(jugador,seleccionCartas)
            jugador['manos'] -= 1
        elif decision == 2 and jugador['descartes'] > 0:
            print("El jugador decidio descartar sus cartas")
            jugadas.descartarCartas(seleccionCartas,jugador)
            jugador['descartes'] -= 1
        mazo.repartirCartas(len(seleccionCartas),jugador)
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
            usuario.nuevaRonda(jugador)
        else:
            print()
            print("----------------------------------------------------------------")
            print(f"Ultima ronda alcanzada:{jugador['ronda']} ¡Hasta la próxima!")
            print("----------------------------------------------------------------")
            print()
