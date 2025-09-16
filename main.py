import random

# ============================================================
# Representación de carta:
#   {"nombre": "A♠", "valor": 1, "palo": "♠", "fichas": 11}
# Claves:
#   - nombre : str  (etiqueta mostrable, p.ej. "A♠")
#   - valor  : int  (A=1, 2..10, J=11, Q=12, K=13)
#   - palo   : str  ("♠", "♥", "♦", "♣")
#   - fichas : int  (A=11; 2..10 -> n; J/Q/K -> 10)
# ============================================================

def fichas_por_valor(valor: int) -> int:
    """Devuelve las fichas base según el valor numérico de la carta."""
    if valor == 1:        # As
        return 11
    if 2 <= valor <= 10:  # 2..10
        return valor
    return 10             # J, Q, K

def carta_str(carta: dict) -> str:
    """Formato consistente para imprimir cartas."""
    # Ej: "A♠ (valor=1, palo=♠, fichas=11)"
    return f"{carta['nombre']} (valor={carta['valor']}, palo={carta['palo']}, fichas={carta['fichas']})"

def crear_mazo_completo():
    """Genera las 52 cartas como una lista de diccionarios."""
    palos = ["♠", "♥", "♦", "♣"]
    rangos = [("A", 1)] + [(str(n), n) for n in range(2, 11)] + [("J", 11), ("Q", 12), ("K", 13)]
    mazo = {}
    for palo in palos:
        for etiqueta, valor in rangos:
            nombre=f"{etiqueta}{palo}"
            mazo[nombre] = {
                "nombre": nombre,
                "valor": valor,
                "palo": palo,
                "fichas": fichas_por_valor(valor),
            }
    return mazo

# =========================
# Variables de estado global
# =========================
mazoCompleto = crear_mazo_completo()
mazoRonda = mazoCompleto.copy()   # copia independiente del mazo base - cada ronda tiene su propio mazo
manoJugador = []                 # cartas en mano del jugador (lista de dicts)

# =========================
# Setup del jugador
# =========================
def crearJugador():
    jugador = {}
    jugador['nombre'] = input("Ingrese el nombre con el que va a jugar: ")
    jugador['puntaje'] = 0
    jugador['pozo'] = random.randint(300, 600)
    jugador['ronda'] = 1
    jugador['manos'] = 5
    jugador['descartes'] = 3
    return jugador

def nuevaRonda(jugador, mazo_base):
    """Reinicia variables de ronda y reparte nuevas cartas."""
    global manoJugador, mazoRonda
    manoJugador = []
    mazoRonda = mazo_base.copy()  # copiar el mazo completo para esta ronda
    jugador['ronda'] += 1
    jugador['pozo'] = random.randint(300, 600)
    jugador['puntaje'] = 0
    jugador['manos'] = 5
    jugador['descartes'] = 3
    print()
    print(f"Jugador: {jugador['nombre']} | Pozo: {jugador['pozo']}")
    print()
    repartirCartas(mazoRonda, 10, manoJugador)
    juego(jugador, manoJugador)

# =========================
# Mecánicas de mazo/mano
# =========================
def repartirCartas(mazo_en_juego, cantCartas, mano):
    """Toma 'cantCartas' al azar del mazo en juego y las mueve a 'mano'."""
    for i in range(cantCartas):
        if not mazo_en_juego:
            break
        key = random.choice(list(mazo_en_juego))
        carta = mazo_en_juego.pop(key)
        mano.append(carta)

def descartarCartas(seleccionCartas, mano):
    """Saca de 'mano' todas las cartas seleccionadas."""
    for carta in seleccionCartas:
        mano.remove(carta)
    return mano

# =========================
# Scoring / combinaciones
# =========================
def calcularFichas(cartasJugadas):
    """Suma las fichas de las cartas jugadas."""
    cantidadFichas = 0
    for carta in cartasJugadas:
        cantidadFichas += carta['fichas']
    return cantidadFichas

def calcularPuntaje(cantidadFichas, multiplicador):
    """Calcula puntaje total."""
    return cantidadFichas * multiplicador

def dividirPaloValores(cartasJugadas):
    """Separa listas paralelas de valores y palos para evaluar combinaciones."""
    valores = []
    palos = []
    for c in cartasJugadas:
        valores.append(c['valor'])
        palos.append(c['palo'])
    return valores, palos

def escalera(valores):
    """True si hay 5 valores consecutivos (considerando A=1)."""
    if len(valores) == 5:
        for i in range(len(valores) - 1):
            if valores[i] + 1 != valores[i + 1]:
                return False
        return True
    return False

def color(palos):
    """True si los 5 palos son iguales."""
    if len(palos) == 5:
        for i in range(len(palos) - 1):
            if palos[i] != palos[i + 1]:
                return False
        return True
    return False

def poker(valores):
    """True si hay cuatro de un mismo valor."""
    for v in valores:
        if valores.count(v) == 4:
            return True
    return False

def par(valores):
    """True si hay al menos un par."""
    for v in valores:
        if valores.count(v) == 2:
            return True
    return False

def doblePar(valores):
    """True si hay dos pares distintos."""
    cantPares = []
    for v in valores:
        if valores.count(v) == 2 and v not in cantPares:
            cantPares.append(v)
    return len(cantPares) == 2

def trio(valores):
    """True si hay un trío."""
    for v in valores:
        if valores.count(v) == 3:
            return True
    return False

def fullHouse(valores):
    """True si hay un trío + un par."""
    cantPares = []
    cantTrios = []
    for v in valores:
        if valores.count(v) == 3 and v not in cantTrios:
            cantTrios.append(v)
    for v in valores:
        if valores.count(v) == 2 and v not in cantPares:
            cantPares.append(v)
    return len(cantTrios) == 1 and len(cantPares) == 1

def combinacionJugada(cartasJugadas):
    """Devuelve (fichas_base, multiplicador) según la combinación detectada."""
    valores, palos = dividirPaloValores(cartasJugadas)
    valores.sort()

    es_escalera = escalera(valores)
    es_poker = poker(valores)
    es_color = color(palos)
    es_trio = trio(valores)
    es_par = par(valores)
    es_doblePar = doblePar(valores)
    es_fullHouse = fullHouse(valores)

    if es_escalera and es_color:
        print("Es: Escalera Corrida")
        return 100, 8
    elif es_poker:
        print("Es: Poker")
        return 60, 7
    elif es_fullHouse:
        print("Es: Full house")
        return 40, 4
    elif es_color and (not es_escalera):
        print("Es: Color")
        return 35, 4
    elif es_escalera and (not es_color):
        print("Es: Escalera")
        return 30, 4
    elif es_trio:
        print("Es: Trio")
        return 30, 3
    elif es_doblePar:
        print("Es: Doble Par")
        return 20, 2
    elif es_par:
        print("Es: Par")
        return 10, 2
    else:
        print("Es: Carta Alta")
        return 5, 1

# =========================
# UI de mano / selección
# =========================
def mostrarCartas(listaCartas):
    """Muestra cartas disponibles para seleccionar."""
    print("\nLas cartas en mano son:")
    for i, carta in enumerate(listaCartas, start=1):
        print(f"carta {i}: {carta_str(carta)}")

def mostrarCartasSelect(listaCartas):
    """Muestra cartas seleccionadas momentáneamente."""
    print("\nLas cartas seleccionadas son:")
    for i, carta in enumerate(listaCartas, start=1):
        print(f"carta {i}: {carta_str(carta)}")

def seleccionar(mano):
    """(Reservado para lógica futura de selección programática)."""
    return []

# =========================
# Jugar / descartar / loop
# =========================
def jugarCartas(jugador, cartasJugadas, mano):
    """Evalúa la jugada, suma puntaje y retira las cartas de la mano."""
    fichas_base, multiplicador = combinacionJugada(cartasJugadas)
    fichas_totales = fichas_base + calcularFichas(cartasJugadas)
    puntaje = calcularPuntaje(fichas_totales, multiplicador)
    jugador['puntaje'] += puntaje
    for carta in cartasJugadas:
        mano.remove(carta)
    print(f"Fichas: {fichas_totales} | Multiplicador: {multiplicador} | Puntaje de la jugada: {puntaje}")



def juego(jugador,manoJugador):
    while jugador['manos'] != 0 and jugador['puntaje'] < jugador['pozo']:
        seleccionCartas=[]
        mostrarCartas(manoJugador)
        cartaSeleccionada=int(input("\nSeleccione una carta:"))

        while (cartaSeleccionada != -1) and (len(seleccionCartas) <= 5):
            seleccionCartas.append(manoJugador[cartaSeleccionada-1])
            
            mostrarCartasSelect(seleccionCartas)
            
            mostrarCartas(manoJugador)
        
            cartaSeleccionada=int(input("\nSeleccione una carta o -1 para terminar:"))
        decision=int(input("Ingrese 1 si quiere jugar, o 2 si quiere descartar:"))
        while (decision < 1 or decision > 2) or jugador['descartes'] == 0:
            if jugador['descartes'] == 0:
                decision=int(input("\nNo tiene mas descartes, debes ingresar 1 para jugar:"))
            else:
                decision=int(input("\nValor invalido! Ingrese 1 si quiere jugar, o 2 si quiere descartar:"))
        if decision == 1:
            print("El jugador decidió jugar sus cartas")
            jugarCartas(jugador,seleccionCartas,manoJugador)
            repartirCartas(mazoRonda,len(seleccionCartas),manoJugador)
            jugador['manos'] -= 1
        elif decision == 2 and jugador['descartes'] > 0:
            print("\nEl jugador decidio descartar sus cartas")
            descartarCartas(seleccionCartas,manoJugador)
            repartirCartas(mazoRonda,len(seleccionCartas),manoJugador)
            jugador['descartes'] -= 1
            
    if jugador['puntaje'] < jugador['pozo'] and jugador['manos'] == 0:
        print("\n¡Te quedaste sin manos y no alcanzate el pozo! Perdiste.")
        print(f"Ultima ronda alcanzada:{jugador['ronda']} ¡Hasta la próxima!")
    elif jugador['puntaje'] >= jugador['pozo']:
        print("¡Alcanzaste el valor del pozo! Ganaste.")
        jugar=int(input("Quiere jugar otra ronda? 1 para 'Si' 2 para 'No':"))
        while jugar != 1 and jugar != 2:
            print("¡Opción invalida!")
            jugar=int(input("Quiere jugar otra ronda? 1 para 'Si' 2 para 'No':"))
        if jugar == 1:
            nuevaRonda(jugador,mazoCompleto)
        else:
            print(f"Ultima ronda alcanzada:{jugador['ronda']} ¡Hasta la próxima!")

# =========================
# Body del programa
# =========================
if __name__ == "__main__":
    jugador = crearJugador()

    print()
    print(f"Jugador: {jugador['nombre']} | Pozo: {jugador['pozo']}")
    print()

    repartirCartas(mazoRonda, 10, manoJugador)
    juego(jugador, manoJugador)

