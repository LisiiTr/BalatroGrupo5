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
