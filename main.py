import mazo
import juego
import tienda
import jugador as usuario
import archivos

def jugarPartida(jugador): #Resultado de ronda, acceso a tienda, jugar de nuevo
    juego.limpiarTerminal()

    puedeJugar=True
    while puedeJugar:
        juego.juego(jugador)
        
        if jugador['puntaje'] < jugador['pozo'] and jugador['manos'] == 0:
            print("¡Te quedaste sin manos y no alcanzate el pozo! Perdiste.")
            print("╔════════════════════════════════════════════════════════╗")
            print(f"║      Ultima ronda alcanzada:{jugador['ronda']:<3} ¡Hasta la próxima!     ║")
            print("╚════════════════════════════════════════════════════════╝")
            input("\nEnter para continuar...")
            puedeJugar=False
            usuario.sumarPuntajeRanking(jugador)
            archivos.cargarHistorico(jugador)
        elif jugador['puntaje'] >= jugador['pozo']:
            juego.limpiarTerminal()
            print("╔════════════════════════════════════════════════════════╗")
            print("║             ¡Alcanzaste el valor del pozo!             ║")
            print("╚════════════════════════════════════════════════════════╝")

            jugador['monedas'] += 5 + jugador['manos'] + jugador['descartes']
            
            invalido = True
            while invalido:
                try:

                    print(f"Tenes {jugador['monedas']} monedas. ¿Quisieras ir a la tienda?")
                    opcionSelect = int(input("Ingresa 1 para ir a la tienda. En caso de no querer ingresar cualquier otro numero: "))
                    if opcionSelect == 1:
                        tienda.tienda(jugador)

                    jugar=int(input("Quiere jugar otra ronda? 1 para 'Si' 2 para 'No':"))
                    while jugar != 1 and jugar != 2:
                        print("¡Opción invalida!")
                        jugar=int(input("Quiere jugar otra ronda? 1 para 'Si' 2 para 'No':"))

                except ValueError:
                    print("Ha ocurrido un error. Debe ingresar un numero")
                    input("\nEnter para continuar...")
                    juego.limpiarTerminal()
                else:
                    invalido = False
            
            if jugar == 1:
                juego.limpiarTerminal()
                usuario.nuevaRonda(jugador)
                mazo.repartirCartas(10, jugador,False)
            else:   
                puedeJugar=False
                usuario.nuevaRonda(jugador)
                archivos.guardarPartida(jugador)
                usuario.sumarPuntajeRanking(jugador)
                print("╔════════════════════════════════════════════════════════╗")
                print(f"║  Ultima ronda alcanzada:{jugador['ronda']} ¡Hasta la próxima!  ║")
                print("╚════════════════════════════════════════════════════════╝")

def main(): #Menu principal con opciones
    activo=True
    while activo:
        juego.limpiarTerminal()

        bandera=True
        while bandera:
            print("Elija una de las siguientes opciones o -1 para cerrar el programa: \n 1. Jugar nueva partida \n 2. Continuar Partida \n 3. Ver Ranking \n 4. Ver Jokers")
            try:

                opcion = int(input("Seleccione una opción segun su numeración: "))
                while (opcion < 1 or opcion > 4) and opcion != -1:
                    opcion = int(input("Seleccione una opción dentro de numeración dada: "))

                bandera=False

            except ValueError:
                print("Ha ocurrido un error. Debe ingresar un numero")
                input("\nEnter para continuar...")
                juego.limpiarTerminal()

        if opcion==1:
            jugador = usuario.crearJugador()
            mazo.repartirCartas(10, jugador,False)
            jugarPartida(jugador)
        elif opcion==2:
            jugador = archivos.cargarPartida()
            if jugador != {}:
                mazo.repartirCartas(10, jugador,False)
                jugarPartida(jugador)
            else:
                print("No hay partidas guardadas. Debe iniciar una nueva partida.")
                input("\nEnter para continuar...")
        elif opcion==3:
            archivos.leerRanking()
        elif opcion==4:
            usuario.imprimirJokers()
        elif opcion==-1:
            activo=False
            print("Programa finalizado.")

main()

 