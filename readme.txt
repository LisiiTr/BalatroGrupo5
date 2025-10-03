En este primer entregable del 40%, el programa contiene las funcionalidades núcleo del juego. 

Tener en cuanta:

- Cada carta vale  una determinada cantidad de fichas, las cuales son fijas.
- Existen posibles combinaciones a formar: Escalera corrida, Color, Poker, Escalera, Full house, Trío, Doble par, Par y Carta alta.
Cada combinación equivale a una cantidad de fichas y a un multiplicador.
- El puntaje se basa en la suma de las fichas del valor de las cartas y las de las combinaciones, y ese monto se multiplica por el multiplicador de la combinación.
- En esta instancia del 40%, el pozo es un valor random entre 300 y 600.

Simplemente se crea un mazo, se establece el mazo que se va a jugar en la ronda, se crea un jugador, el cual tiene su respectivo nombre, cantidad de manos/descartes, puntaje,
un pozo que completar y la ronda en la que esta.
Luego se le reparten las cartas al jugador, y comienza la interacción del usuario.
El jugador selecciona las cartas que desea jugar o descartar. En esta instancia el jugador puede elegir como máximo 5 cartas y al menos 1.
Una vez que el jugador selecciona y decide si decide jugar o descartar, se bifurca el camino.
Si decide jugar, el juego detecta la combinación (cada combinación tiene una cantidad de fichas y un multiplicador base) y devuelve,
dependiendo la combinación más alta, la cantidad de fichas y el multiplicador, y luego el juego calcula la cantidad de fichas que suman las cartas.
Después de esto, el juego suma la cantidad de fichas de la combinación con la suma de fichas que dan las cartas, y las multiplica por el multiplicador.
Se le suma el puntaje al jugador y se verifica si alcanzó o no el pozo. Si lo alcanzó el jugador ganó la ronda y puede decidir dejar de jugar o pasar a la siguiente ronda.
Si no alcanzó el pozo, el juego le reparte la cantidad de cartas que jugó y vuelve a iniciar desde la selección.

Si el jugador decide descartar las cartas seleccionadas, se descartan las cartas y se le reparten unas nuevas.


Más adelante el jugador tendrá la posibilidad de adquirir jokers y cartas nuevas, mediante un sistema de tienda.
A medida que gane rondas el jugador podrá ganar monedas, y con esas monedas adquirir bonificadores.
En los próximos entregables el pozo será incremento y dejará de ser un random entre 300 y 600.

Cambios a realizar para nuevas funcionalidades:

- Modularizar la seleccion de cartas a una funcion SelectorCartas.

- Agregar al diccionario Jugador, un campo que contenga un diccionario de combinaciones. Ej:
    jugador['combinaciones]= {  
                                'Escalera Corrida':{'fichas': 100, 'multiplicador': 8},
                                'Poker':{'fichas': 60, 'multiplicador': 7}
                                ...
                            }
    De esta manera podemos implementar las cartas planeta, y aumkentar de nivel la combinación.

- Actualizar While de decisiones en función Juego. Genera un bucle infinito si los descartes son 0, y no valida bien el > <. 
    Cuando los descartes sean sero tiene que verificar que la decision sea 2 y los descartes 0.
 




Nuevas Funcionalidades:

- Agregar al diccionario Jugador, un campo "Monedas", donde se acumulara el dinero para gastar en la tienda.

- Generar archivo tienda, donde se aplicara la tienda.

- Posibilidad de deselección de cartas.
  
- Tienda:  Van a poder comprar 3 sobres y 2 bonificadores especificos (las cuales pueden ser jokers y/o planetas). Hay que definir si pueden actualizar la tienda o no.

    - Generar la lista de diccionarios de Planetas
    - Generar la lista de diccionarios de Jokers 
    - Crear lista de JOKERS y planerasen el diccionario Jugador

    - Crear función tienda, en esta tendra la opcion de compra de 3 sobre y 2 cartas. 
    def tienda(jugador):
            
            - Crear función donde se selecciones 2 bonificadores (planteas o jokers) randoms para la compra
                def bonificadoras (jugador,planetas)
                    debe seleccionar de manera random 2 cartas individuales y debera devolverlas
                    return nuevaCarta,planeta
        
        Aqui se le deberan mostrar los 3 sobres. Y 2 cartas de la funcion bonificadoras. Si las selecciona se debe agregar al jugador.
        Dependiendo lo que selecione, se debera invocar las siguientes funciones:

            - Crear función donde se genere una lista de 3 jokers random.
                def selectJocker(jugador,joker):
                    el sistema debera seleccionar de manera random del sistema 3 jokers y mostarlos, el jugador puede seleccionar 1.
                    la carta seleccionada se agrega al jugador

            - Crear función donde se genere una lista de 3 planetas random.
                def selectPlaneta(jugador,planetas):
                    el sistema debera seleccionar de manera random del sistema 3 planetas y mostarlos, el jugador puede seleccionar 1.
                    la carta seleccionada se agrega al jugador

            - Crear función donde se genere una lista de 3 cartas de mazo random.
                def selectNuevaCarta(jugador,joker):
                    el sistema debera seleccionar de manera random del sistema 3 cartas de mazo y mostarlos, el jugador puede seleccionar 1.
                    la carta seleccionada se agrega al jugador

    - Generar la opción de vender jokers que tiene adquiridos. (DEBE SER UNA OPCION DENTRO DE LA TIENDA, QUE REDIRIJA A ESTA FUNCION)

- Una vez aplicado los jokers, aplicarlos a la hora de calcular puntajes
    def calcularPuntaje() -> DENTRO DEL JUGADAS.PY
    sumar la invocación a jokers. DEPENDE MUCHO DE CUALES SEAN LOS JOKERS

- Una vez aplicados los jokers generar pozo incremental. El pozo se establecera en 300 la primera ronda y cuando se complete una ronda la funcion nuevaRonda() 
    ubicada en JUGADOR.PY, incrementara el pozo en un numero random de 1.2 y 1.6.
    

- Incorporación de ciegas. En este caso cada vez la ronda sea multiplicador de 3, se debera considerar una ciega. 
    Las ciegas en principio inhabilitaran a las los palos, las cartas de ciertos palos, no suman puntos. El palo es seleccionado de forma aleatorio. 
    Sería un def que sleccione un random de la lista palos. 




TUPLAS:
    - EN PALOS Y VALORES, PARRA QUE NO SEA MODIFIICABLE

CONJUNTOS:
    -