import mazo
import jugadas
import jugador as usuario
import  os


# contempla tanto windows, como linux y macos
def limpiarTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def selectorCartas(jugador):
    seleccionCartas=[]

    bandera=True
    while bandera:
        try:

            if len(seleccionCartas) >0:
                mazo.mostrarCartasSelect(seleccionCartas)
                mazo.mostrarCartas(jugador['manoJugador'])

                cartaSeleccionada=int(input("\nSeleccione una carta o -1 para terminar:"))
                while cartaSeleccionada<1 or cartaSeleccionada>10:
                    cartaSeleccionada=int(input("\nSeleccione un indice proporcionado o -1: "))
            else:
                mazo.mostrarCartas(jugador['manoJugador'])

                cartaSeleccionada=int(input("\nSeleccione una carta:"))
                while cartaSeleccionada<1 or cartaSeleccionada>10:
                    cartaSeleccionada=int(input("\nSeleccione un indice proporcionado: "))

            
            if cartaSeleccionada == -1:
                bandera= False

            while (cartaSeleccionada != -1) and (len(seleccionCartas) < 5):
                limpiarTerminal()
                if jugador['manoJugador'][cartaSeleccionada-1] in seleccionCartas:
                    seleccionCartas.remove(jugador['manoJugador'][cartaSeleccionada-1])  
                else:
                    seleccionCartas.append(jugador['manoJugador'][cartaSeleccionada-1])
                mazo.mostrarCartasSelect(seleccionCartas)
                if len(seleccionCartas) == 5:
                    bandera = False
                    break
                else:
                    mazo.mostrarCartas(jugador['manoJugador'])
                    cartaSeleccionada=int(input("\nSeleccione una carta o -1 para terminar:"))
                    if cartaSeleccionada == -1:
                        bandera= False
        except ValueError:
            print("Debe ingresar un numero")
        except IndexError:
            print("Debe ingresar una carta disponible")
        finally:
            limpiarTerminal()


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
        mazo.mostrarCartasSelect(seleccionCartas)
        bandera=True
        while bandera:
            try:
                decision=int(input("Ingrese 1 si quiere jugar, o 2 si quiere descartar:"))
                while (decision < 1 or decision > 2) or jugador['descartes'] == 0:
                    if jugador['descartes'] == 0:
                        decision=int(input("No tiene mas descartes, debes jugar las cartas:"))
                    else:
                        decision=int(input("Valor invalido! Ingrese 1 si quiere jugar, o 2 si quiere descartar:"))
            except ValueError:
                print("Debe ingresar un numero")
            else:
                bandera=False
                

        if decision == 1:
            print("El jugador decidió jugar sus cartas")
            jugadas.jugarCartas(jugador,seleccionCartas)
            jugador['manos'] -= 1
        elif decision == 2 and jugador['descartes'] > 0:
            print("El jugador decidio descartar sus cartas")
            jugadas.descartarCartas(seleccionCartas,jugador)
            jugador['descartes'] -= 1
        mazo.repartirCartas(len(seleccionCartas),jugador)