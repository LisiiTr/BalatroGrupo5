import jugador
import mazo
import juego
 
 
# Función del programa principal
 

jugador = jugador.crearJugador()

mazo.repartirCartas(10, jugador)
juego.juego(jugador)
 