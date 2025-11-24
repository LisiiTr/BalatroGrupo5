import os
import json
import juego

def buscarRuta(nombre): #devolvemos la ruta del archivo que querramos usar con su respectivo nombre
    rutaArchivo= os.path.join(os.path.dirname(__file__), nombre)

    return rutaArchivo

def traerJugadores(rutaArchivo): #se leen los jugadores del ranking
    try:
        with open(rutaArchivo, 'r') as ranking:
            jugadores = json.load(ranking)
    except (FileNotFoundError):
        jugadores = []
    else:
        return jugadores


def cargarHistorico(jugador): #se cargan los jugadores en el ranking histórico

    rutaArchivo=buscarRuta("historico.json")
    jugadores= traerJugadores(rutaArchivo)

    with open(rutaArchivo,'w') as ranking:
        jugadorGuardar={}
        jugadorGuardar['nombre'] = jugador['nombre']
        jugadorGuardar['rondaMax'] = jugador['ronda']
        jugadorGuardar['puntajeTotal'] = jugador['puntaje_ranking']

        jugadores.append(jugadorGuardar)
        json.dump(jugadores,ranking,indent=4)


def leerRanking(): #se muestran los datos del ranking en pantalla
    try:
        with open(buscarRuta("historico.json"),'r') as ranking:
            datos=json.load(ranking)

        datos.sort(key=lambda jugador: jugador["puntajeTotal"], reverse=True) 

        juego.limpiarTerminal()
        i=1
        print(f"{'#':<3} | {'Nombre':<12} | {'Ronda':<6} | {'Puntaje':<7}")
        print("-" * 40)

        for i, j in enumerate(datos, 1):
            print(f"{i:<3} | {j['nombre']:<12} | {j['rondaMax']:<6} | {j['puntajeTotal']:<7}")

        input("\nEnter para continuar...")
    except Exception as e:
        print("Ha ocurrido un error ",e)



def traerPartidas():
    try:
        with open(buscarRuta("partidas_guardadas.json"), "r") as partidas_guardadas:
            partidas = json.load(partidas_guardadas)
    except Exception as e:
        print("Ha ocurrido un error al traer partidas.")
        partidas= dict()
    
    return partidas

def guardarPartida(jugador): 
    
    partida= f"{jugador['nombre']}-{jugador['ronda']}"

    partidas = dict()
    partidas = traerPartidas()
    try:
        partidas[partida] = jugador
    except Exception as e:
        print("Ha ocurrido un error agregar partida al dict.")

    try:
        with open(buscarRuta(f"partidas_guardadas.json"), "w") as partidas_guardadas:
            json.dump(partidas,partidas_guardadas,indent=4)
    except Exception as e:
        print("Ha ocurrido un error.")
    else: 
        print("La parida se guardo con exito!!")
        input("Enter para continuar...")
    

def mostrarPartidasGuardadas():
    partidas= traerPartidas()

    if partidas == {}:
        return -1 , []
    else:
        print("\nLas partidas guardadas son:\n")
        print(f"{'N°':<4} {'Jugador':<15} {'Ronda':<10}")
        print("-" * 32)

        for i, jugador in enumerate(partidas.values(), start=1):
            print(f"{i:<4} {jugador['nombre']:<15} {jugador['ronda']:<10}")
        
        nombres_partidas = [nombre for nombre in partidas.keys()]

        try:
            opcion=int(input("Seleccióne la partida que desea continuar: "))
            while opcion < 1 or opcion> len(partidas):
                opcion=int(input(f"Opción invalida, debe ser entre 1 y {len(partidas)} Seleccióne la partida que desea continuar: "))
        except ValueError:
            print("Ha ocurrido un error. Debe ingresar un numero")
            input("\nEnter para continuar...")
            juego.limpiarTerminal()
        
        return opcion , nombres_partidas

def cargarPartida():
    indice , nombres_partidas = mostrarPartidasGuardadas()
    if indice == -1:
        jugador = {}
        return jugador
    else:
        try:
            with open(buscarRuta(f"partidas_guardadas.json"), "r") as partida_guardada:
                partidas = json.load(partida_guardada)
                
                jugador = partidas[nombres_partidas[indice-1]]

                del partidas[nombres_partidas[indice-1]]
                
            try:
                with open(buscarRuta("partidas_guardadas.json"), "w") as partidas_guardadas:
                    json.dump(partidas,partidas_guardadas,indent=4)
            except Exception as e:
                print("Ha ocurrido un error.")

            print(f"La partida de {jugador['nombre']} en la ronda {jugador['ronda']} con un puntaje/pozo de {jugador['puntaje']}/{jugador['pozo']} ")
        except Exception as e:
            print("Ha ocurrido un error.")
        else:
            print("Partida cargada correctamente!!")
            input("Enter para continuar...")
            return jugador

