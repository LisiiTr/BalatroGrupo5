import mazo
import juego
import tienda
import jugador as usuario
import archivos

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
            usuario.sumarPuntajeRanking(jugador)
            archivos.cargarHistorico(jugador)
        elif jugador['puntaje'] >= jugador['pozo']:
            print("\n----------------------------------------------------------------")
            print("¡Alcanzaste el valor del pozo! ")
            print("----------------------------------------------------------------\n")

            jugador['monedas'] += 5 + jugador['manos'] + jugador['descartes']
            
            print(f"Tenes {jugador['monedas']} monedas. ¿Quisieras ir a la tienda?")
            try:
                opcionSelect = int(input("Ingresa 1 para ir a la tienda. En caso de no querer ingresar cualquier otro numero: "))
                if opcionSelect == 1:
                    tienda.tienda(jugador)

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
                usuario.sumarPuntajeRanking(jugador)
                archivos.cargarHistorico(jugador)
                print("\n----------------------------------------------------------------")
                print(f"Ultima ronda alcanzada:{jugador['ronda']} ¡Hasta la próxima!")
                print("----------------------------------------------------------------\n")



activo=True
while activo:
    juego.limpiarTerminal()
    print("Elija una de las siguientes opciones o -1 para cerrar el programa: \n 1. Jugar nueva partida. \n 2. Continuar Partida. \n 3. Ver ranking. \n 4. Ver jokers.")

    bandera=True
    while bandera:
        try:

            opcion = int(input("Seleccione una opción segun su numeración: "))
            while (opcion < 1 or opcion > 4) and opcion != -1:
                opcion = int(input("Seleccione una opción dentro de numeración dada: "))

            bandera=False

        except ValueError:
            print("Debe ingresar un numero")

    if opcion==1:
        jugarPartida()
    elif opcion==2:
        print("Función")
    elif opcion==3:
        archivos.leerRanking()
    elif opcion==4:
        tienda.imprimirJokers()
    elif opcion==-1:
        activo=False
        print("Programa finalizado.")


 