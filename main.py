import jugador
import mazo
import juego
import jugador as usuario


def jugarPartida():
    jugador = usuario.crearJugador()
    juego.limpiarTerminal()
    mazo.repartirCartas(10, jugador)
    juego.juego(jugador)

    puedeJugar=True
    while puedeJugar:
        
        if jugador['puntaje'] < jugador['pozo'] and jugador['manos'] == 0:
            print("¡Te quedaste sin manos y no alcanzate el pozo! Perdiste.")
            print(f"Ultima ronda alcanzada:{jugador['ronda']} ¡Hasta la próxima!")
            puedeJugar=False

        elif jugador['puntaje'] >= jugador['pozo']:
            print()
            print("----------------------------------------------------------------")
            print("¡Alcanzaste el valor del pozo! Ganaste.")
            print("----------------------------------------------------------------")
            print()
            try:
                jugar=int(input("Quiere jugar otra ronda? 1 para 'Si' 2 para 'No':"))
                while jugar != 1 and jugar != 2:
                    print("¡Opción invalida!")
                    jugar=int(input("Quiere jugar otra ronda? 1 para 'Si' 2 para 'No':"))
            except ValueError:
                print("Debe ingresar un numero")
            if jugar == 1:
                juego.limpiarTerminal()
                usuario.nuevaRonda(jugador)
            else:
                puedeJugar=False
                print()
                print("----------------------------------------------------------------")
                print(f"Ultima ronda alcanzada:{jugador['ronda']} ¡Hasta la próxima!")
                print("----------------------------------------------------------------")
                print()


activo=True
while activo:
    juego.limpiarTerminal()
    print("Elija una de las siguientes opciones o -1 para dejar cerrar el programa: \n 1. Jugar nueva partida. \n 2. Continuar Partida. \n 3. Ver ranking. \n 4. Ver jokers.")

    bandera=True
    while bandera:
        try:

            opcion = int(input("Seleccione una opción segun su numeración: "))
            while (opcion < 1 or opcion > 4) and opcion != -1:
                opcion = int(input("Seleccione una opción dentro de numeración dada: "))

            bandera=False

        except ValueError:
            print("Debe ingresar un numero")

    juego.limpiarTerminal()
    if opcion==1:
        jugarPartida()
    elif opcion==2:
        print("Función")
    elif opcion==3:
        print("Función")
    elif opcion==4:
        print("Función")
    elif opcion==-1:
        activo=False
        print("Programa finalizado.")


 