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
            
            bandera = True
            while bandera:
                invalido = True
                while invalido:
                    try:
                        print( "╔═══════════════════════════════════════════════════════════╗")
                        print(f"║                MONEDAS DISPONIBLES: {jugador['monedas']:<22}║")
                        print( "╠═══════════════════════════════════════════════════════════╣")
                        print(f"║ 1. Pasar De Ronda                                         ║")
                        print(f"║ 2. Guardar Partida                                        ║")
                        print( "║ 3. Tienda                                                 ║")
                        print( "╚═══════════════════════════════════════════════════════════╝\n")

                        print(jugador['mazoCompleto'])
                        
                        opcionSelect = int(input("Ingresa una opción: "))
                        while opcionSelect < 1 or opcionSelect > 3:
                            opcionSelect = int(input("La opción debe estar entre 1 y 3. Ingresa una opción: "))

                        if opcionSelect == 1:
                            bandera = False
                            juego.limpiarTerminal()
                            usuario.nuevaRonda(jugador)
                            mazo.repartirCartas(10, jugador,False)
                        elif opcionSelect == 2:   
                            puedeJugar=False
                            bandera = False
                            usuario.nuevaRonda(jugador)
                            archivos.guardarPartida(jugador)
                            usuario.sumarPuntajeRanking(jugador)
                            print( "╔════════════════════════════════════════════════════════╗")
                            print(f"║      Ultima ronda alcanzada:{jugador['ronda']:<3} ¡Hasta la próxima!     ║")
                            print( "╚════════════════════════════════════════════════════════╝")
                        elif opcionSelect == 3:
                            tienda.tienda(jugador)


                    except ValueError:
                        print("Ha ocurrido un error. Debe ingresar un numero")
                        input("\nEnter para continuar...")
                        juego.limpiarTerminal()
                    else:
                        invalido = False
            

def main(): #Menu principal con opciones
    activo=True
    while activo:
        juego.limpiarTerminal()

        bandera=True
        while bandera:
            print("Elija una de las siguientes opciones: \n 1. Nueva Partida \n 2. Continuar Partida \n 3. Ver Ranking \n 4. Ver Jokers \n 5. Cerrar Programa")
            try:

                opcion = int(input("Seleccione una opción segun su numeración: "))
                while (opcion < 1 or opcion > 5):
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
            juego.limpiarTerminal()
            jugador = archivos.cargarPartida()
            if jugador == -2:
                print("Volviste al menu!")
                input("\nEnter para continuar...")
            elif jugador != {}:
                mazo.repartirCartas(10, jugador,False)
                jugarPartida(jugador)
            else:
                print("No hay partidas guardadas. Debe iniciar una nueva partida.")
                input("\nEnter para continuar...")
        elif opcion==3:
            archivos.leerRanking()
        elif opcion==4:
            usuario.imprimirJokers()
        elif opcion==5:
            activo=False
            print("Programa finalizado.")

main()

 