import mazo
import jugadas
import jugador as usuario
import  os
from itertools import zip_longest

def limpiarTerminal(): #Limpia la terminal usando libreria ´os´
    os.system('cls' if os.name == 'nt' else 'clear')

def hud_cominaciones_Jokers(combinaciones, jokers): #Interfaz visual de combinaciones y jokers

    col_izq = [
        "╔════════════════════════════════════════════════════════╗",
        "║                    COMBINACIONES                       ║",
        "╚════════════════════════════════════════════════════════╝",
    ]

    for nombre, (puntos, mult) in combinaciones.items():
        linea = f" {nombre.replace('_',' ').title():<21} ║ Pts:{puntos:<10} ║ x{mult:<3}"
        col_izq.append(linea)

    if jokers:
        col_der = [
            "╔════════════════════════════╗",
            "║           JOKERS           ║",
            "╚════════════════════════════╝",
            "",
        ]
    else:
        col_der = [
            "╔════════════════════════════╗",
            "║           JOKERS           ║",
            "╚════════════════════════════╝",
            "",
            "        No hay jokers        ",
        ]

    for i, j in enumerate(jokers, 1): 
            col_der.append(f"[{i}] {j.get('nombre')}  ({j.get('rareza')}): {j.get('descripcion')}")
    

    ancho_col = 60
    for izq, der in zip_longest(col_izq, col_der, fillvalue=""):
        print(f"{(izq):<{ancho_col}} ║   {der}")



def hud(jugador): #Interfaz visual del jugador
    limpiarTerminal()

    hud_cominaciones_Jokers(jugador["combinaciones"], jugador["jokers"])

    print("\n╔══════════════════════╦════════════════╦════════════════════╦═══════════════════════════════╗")
    print( f"║  Jugador: {jugador['nombre']:<9}  ║   Manos: {jugador['manos']:^3}   ║   Descartes: {jugador['descartes']:^3}   ║ Puntaje/Pozo: {jugador['puntaje']:>6}/{jugador['pozo']:<8} ║")
    print(  "╚══════════════════════╩════════════════╩════════════════════╩═══════════════════════════════╝\n")




def selectorCartas(jugador): #Seleccion, deseleccion y confirmacion de cartas
    seleccionCartas=[]

    bandera=True
    while bandera:
        try:
            hud(jugador)
            
            if len(seleccionCartas) >0:
                mazo.mostrarCartasSelect(seleccionCartas)
                print("\nLas cartas en mano son:")
                mazo.mostrarCartas(jugador['manoJugador'])

                cartaSeleccionada = int(input("\nElegí una carta (o seleccioná una ya elegida para quitarla). Ingresá -1 para finalizar: "))

                while cartaSeleccionada<1 and cartaSeleccionada != -1:
                    cartaSeleccionada=int(input("\nSeleccione un indice proporcionado o -1: "))
            else:
                print("\nLas cartas en mano son:")
                mazo.mostrarCartas(jugador['manoJugador'])

                cartaSeleccionada=int(input("\nSeleccione una carta:"))
                while cartaSeleccionada<1 and cartaSeleccionada != -1:
                    cartaSeleccionada=int(input("\nSeleccione un indice proporcionado: "))

            
            if cartaSeleccionada == -1:
                bandera= False

            while (cartaSeleccionada != -1) and (len(seleccionCartas) < 5):
                limpiarTerminal()
                if jugador['manoJugador'][cartaSeleccionada-1] in seleccionCartas:
                    seleccionCartas.remove(jugador['manoJugador'][cartaSeleccionada-1])  
                else:
                    seleccionCartas.append(jugador['manoJugador'][cartaSeleccionada-1])
                
                if len(seleccionCartas) == 5:
                    bandera = False
                    break
                else:
                    hud(jugador)
                    mazo.mostrarCartasSelect(seleccionCartas)
                    print("\nLas cartas en mano son:")
                    mazo.mostrarCartas(jugador['manoJugador'])
                    cartaSeleccionada=int(input("\nSeleccione una carta o -1 para terminar:"))
                    while cartaSeleccionada<1 and cartaSeleccionada != -1:
                        cartaSeleccionada=int(input("\nSeleccione una carta o -1 para terminar:"))
                    if cartaSeleccionada == -1:
                        bandera= False
        except ValueError:
            print("╔════════════════════════════════════════════════════════╗")
            print("║                Debe ingresar un numero                 ║")
            print("╚════════════════════════════════════════════════════════╝")
            input("\nEnter para continuar...")
            limpiarTerminal()
        except IndexError:
            print("╔════════════════════════════════════════════════════════╗")
            print("║           Debe ingresar una carta disponible           ║")
            print("╚════════════════════════════════════════════════════════╝")
            input("\nEnter para continuar...")
            limpiarTerminal()
        finally:
            limpiarTerminal()


    return seleccionCartas

def juego(jugador): #Decidir si jugar o descartar las cartas seleccionadas
    while jugador['manos'] != 0 and jugador['puntaje'] < jugador['pozo']:
        seleccionCartas=[]

        seleccionCartas= selectorCartas(jugador)
        bandera=True
        while bandera:
            try:
                mazo.mostrarCartasSelect(seleccionCartas)
                decision = int(input("Ingrese 1 si quiere jugar, o 2 si quiere descartar: "))

                if jugador['descartes'] == 0 and decision == 2:
                    print("No tienes más descartes, debes jugar las cartas.")
                    continue

                if decision not in (1, 2):
                    print("Valor inválido. Ingrese 1 para jugar o 2 para descartar.")
                    continue

                bandera = False

            except ValueError:
                print("Debe ingresar un número.")
                input("\nEnter para continuar...")
                limpiarTerminal()
                

        if decision == 1:
            print("El jugador decidió jugar sus cartas")
            jugadas.jugarCartas(jugador,seleccionCartas)
            jugador['manos'] -= 1
        elif decision == 2 and jugador['descartes'] > 0:
            limpiarTerminal()
            print("El jugador decidio descartar las cartas")
            mazo.mostrarCartas(seleccionCartas)
            input("\nEnter para continuar...")
            jugadas.descartarCartas(seleccionCartas,jugador)
            jugador['descartes'] -= 1
        
        if jugador['puntaje'] < jugador['pozo'] and jugador['manos']>0:
            mazo.repartirCartas(len(seleccionCartas),jugador,True)
        else:
            mazo.repartirCartas(len(seleccionCartas),jugador,False)
