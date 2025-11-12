import os
import json

def buscarRuta(nombre):
    rutaActual= os.path.dirname(__file__)
    rutaArchivo= os.path.join(rutaActual, nombre)

    return rutaArchivo

def traerJugadores(rutaArchivo):
    try:
        with open(rutaArchivo,'r') as ranking:
            datos=json.load(ranking)
    except Exception as e:
        print(e)
        return []
    else:
        return datos


def cargarHistorico(jugador):

    rutaArchivo=buscarRuta("historico.json")
    jugadores= traerJugadores(rutaArchivo)

    with open(rutaArchivo,'a') as ranking:
        jugadorGuardar={}
        jugadorGuardar['nombre'] = jugador['nombre']
        jugadorGuardar['rondaMax'] = jugador['ronda']
        jugadorGuardar['puntajeTotal'] = jugador['puntaje_ranking']

        jugadores.append(jugadorGuardar)
        json.dump(jugadores,ranking,indent=4)


def leerRanking():
    try:
        with open(buscarRuta("historico.json"),'r') as ranking:
            datos=json.load(ranking)

        datos.sort(key=lambda jugador: jugador["rondaMax"], reverse=True) 

        i=1
        for jugador in datos:
            print(f" {i} - {jugador['nombre']}      |    Ronda {jugador['rondaMax']}     |    Puntaje total: {jugador['puntajeTotal']}")
            i += 1
        input("Enter para continuar...")
    except Exception as e:
        print("Ha ocurrido un error ",e)





def guardarPartida(jugador,jokers):
    pass


def cargarPartida():
    pass


