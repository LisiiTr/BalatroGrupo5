import os
import json
import  juego

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





def guardarPartida(jugador,jokers): 
    pass


def cargarPartida():
    pass
