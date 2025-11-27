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
        print("╔═══════╦══════════════╦═════════╦═══════════╗")
        print("║  Pos  ║    Nombre    ║  Ronda  ║  Puntaje  ║")
        print("╠═══════╬══════════════╬═════════╬═══════════╣")

        for i, jugador in enumerate(datos, 1):
            num      = f"{i:^5}"
            nombre   = f"{jugador['nombre']:^12}"        
            ronda    = f"{jugador['rondaMax']:^7}"       
            puntaje  = f"{jugador['puntajeTotal']:^9}"   
            
            print(f"║ {num} ║ {nombre} ║ {ronda} ║ {puntaje} ║")

        print("╚═══════╩══════════════╩═════════╩═══════════╝")

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
        print("Ocurrió un error al guardar la partida.")
    else: 
        print("La parida se guardo con exito!!")
        input("Enter para continuar...")
    

def mostrarPartidasGuardadas():
    partidas= traerPartidas()

    if partidas == {}:
        return -1 , []
    else:

        print("╔══════╦══════════════╦═════════╗")
        print("║  N°  ║    Nombre    ║  Ronda  ║")
        print("╠══════╬══════════════╬═════════╣")

        for i, jugador in enumerate(partidas.values(), start=1):
            num      = f"{i:^4}"
            nombre   = f"{jugador['nombre']:^12}"        
            ronda    = f"{jugador['ronda']:^7}"         
            
            print(f"║ {num} ║ {nombre} ║ {ronda} ║")

        print("╚══════╩══════════════╩═════════╝")






        nombres_partidas = [nombre for nombre in partidas.keys()]
        invalido = True
        while invalido:
            try:
                opcion=int(input("Seleccione el N° de la partida que desea continuar, o -1 para volver atras: "))
                if opcion == -1:
                    return -2 , nombres_partidas
                while opcion < 1 or opcion> len(partidas):
                    opcion=int(input(f"Opción invalida, debe ser entre 1 y {len(partidas)} Seleccione el N° de la partida que desea continuar: "))
                    if opcion == -1:
                        return -2 , nombres_partidas
            except ValueError:
                print("Ha ocurrido un error. Debe ingresar un numero")
                input("\nEnter para continuar...")
                juego.limpiarTerminal()
            else:
                invalido = False
    
        return opcion , nombres_partidas

def cargarPartida():
    indice , nombres_partidas = mostrarPartidasGuardadas()
    if indice == -1:
        jugador = {}
        return jugador
    elif indice == -2:
        return -2
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

