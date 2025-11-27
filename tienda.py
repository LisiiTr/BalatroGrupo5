import random
import juego

planetas = {
    "Mercurio": {
        "jugada": "par",
        "efecto": "Aumenta las fichas base y el multiplicador del Par.",
        "incremento": {"fichas": 15, "multiplicador": 1}
    },
    "Venus": {
        "jugada": "doble_par",
        "efecto": "Aumenta las fichas base y el multiplicador del Doble Par.",
        "incremento": {"fichas": 20, "multiplicador": 2}
    },
    "Tierra": {
        "jugada": "trio",
        "efecto": "Aumenta las fichas base y el multiplicador del Trío.",
        "incremento": {"fichas": 30, "multiplicador": 2}
    },
    "Marte": {
        "jugada": "escalera",
        "efecto": "Aumenta las fichas base y el multiplicador de la Escalera.",
        "incremento": {"fichas": 40, "multiplicador": 3}
    },
    "Júpiter": {
        "jugada": "color",
        "efecto": "Aumenta las fichas base y el multiplicador del Color.",
        "incremento": {"fichas": 50, "multiplicador": 2}
    },
    "Saturno": {
        "jugada": "full_house",
        "efecto": "Aumenta las fichas base y el multiplicador del Full House.",
        "incremento": {"fichas": 60, "multiplicador": 3}
    },
    "Urano": {
        "jugada": "poker",
        "efecto": "Aumenta las fichas base y el multiplicador del Póker.",
        "incremento": {"fichas": 70, "multiplicador": 1}
    },
    "Neptuno": {
        "jugada": "escalera_corrida",
        "efecto": "Aumenta las fichas base y el multiplicador de la Escalera de color.",
        "incremento": {"fichas": 80, "multiplicador": 4}
    },
    "Plutón": {
        "jugada": "carta_alta",
        "efecto": "Aumenta ligeramente las fichas base y el multiplicador de la Carta Alta.",
        "incremento": {"fichas": 10, "multiplicador": 1}
    }
}


def tienda(jugador): #Función que nos permite comprar cartas bonificadoras o sobres de cartas especiales. Para poder aforntar la dificultad de la partida.

    jokerCompra =jokerBonificador(jugador['jokersDisponibles'])
    cartaNueva= cartaBonificadora(jugador)
    
    comprar=True
    while comprar:
        
        bandera=True
        while bandera:
            try:
                juego.limpiarTerminal()


                print( "╔═══════════════════════════════════════════════════════════╗")
                print(f"║                MONEDAS DISPONIBLES: {jugador['monedas']:<22}║")
                print( "╠═══════════════════════════════════════════════════════════╣")
                print( "║                          TIENDA                           ║")
                print( "╠═══════════════════════════════════════════════════════════╣")
                print(f"║ 1. Carta nueva: {cartaNueva['nombre']:<3} (+{cartaNueva['bonificacion_fichas']:<4} fichas)      3 monedas         ║")
                print(f"║ 2. Joker nuevo: {jokerCompra['nombre']:<24}3 monedas         ║")
                print( "║ 3. Sobre de joker                       6 monedas         ║")
                print( "║ 4. Sobre de planetas                    6 monedas         ║")
                print( "║ 5. Sobre de cartas                      6 monedas         ║")
                print( "║ 6. Salir de la tienda                                     ║")
                print( "╚═══════════════════════════════════════════════════════════╝\n")

                opcionElegida = int(input("Seleccione una opción (1–6): "))

                while opcionElegida < 1 or opcionElegida > 6:
                    print("Opción inválida. Intente nuevamente.")
                    opcionElegida = int(input("Seleccione una opción (1–6): "))
            except ValueError:
                print("Debe ingresar un numero")
                input("Enter para continuar...")
            else: 
                bandera = False

        if opcionElegida == 1 and jugador["monedas"]>=3:
            jugador['mazoCompleto'].append(cartaNueva)
            cartaNueva= cartaBonificadora(jugador)
            jugador['monedas'] -= 3
            input("Enter para continuar...")
        elif opcionElegida == 2 and jugador["monedas"]>=3:
            jugador['jokers'].append(jokerCompra)
            jugador['jokersDisponibles'].remove(jokerCompra)

            jokerCompra =jokerBonificador(jugador['jokersDisponibles'])
            jugador['monedas'] -= 3
            input("Enter para continuar...")
        elif opcionElegida == 3 and jugador["monedas"]>=6:
            seleccionarJoker(jugador)
            jugador['monedas'] -= 6
            input("Enter para continuar...")
        elif opcionElegida == 4 and jugador["monedas"]>=6:
            jugador['monedas'] -= 6
            seleccionarPlaneta(jugador, planetas)
        elif opcionElegida == 5 and jugador["monedas"]>=6:
            jugador['monedas'] -= 6
            seleccionarNuevaCarta(jugador, jugador['mazoCompleto'])
            input("Enter para continuar...")
        elif opcionElegida == 6:
            comprar = False
        else:
            print("No tienes suficientes monedas para comprar esa opción.") 
            input("Enter para continuar...")

            
    return jugador


def cartaBonificadora(jugador): #Se selecciona una carta random del mazo y se le incrementan las fichas. La devuelve para que sea una opción de compra

    carta = random.choice(jugador['mazoCompleto'])
    factorMejora = random.uniform(1.5, 2.5)

    fichas_originales = carta['fichas']
    carta['fichas'] = round(fichas_originales * factorMejora)
    
    carta['bonificacion_fichas'] = carta['fichas'] - fichas_originales 
    
    carta_bonificadora= carta
    
    return carta_bonificadora


def jokerBonificador(jokers): #Se selecciona un joker random y la devuelve para que sea una opción de compra
    
    joker_seleccionado = random.choice(jokers)
    
    joker_bonificadora= joker_seleccionado
    
    return joker_bonificadora



def seleccionarJoker(jugador):#Función del sobre de Jokers, se agarran al azar 3 jokers disponibles y el usuario puede agarrar solo 1.
    jokersRandoms=[]
    while len(jokersRandoms) < 3:
        jokerRandom= random.choice(jugador['jokersDisponibles'])
        if jokerRandom not in jokersRandoms:
            jokersRandoms.append(jokerRandom)
        
    
    bandera=True
    while bandera:
        for i,j in enumerate (jokersRandoms,start=1):
            print(f'{i}- {j["nombre"]} | {j["descripcion"]}')
            

        try:
            jokerIndice= int(input("Seleccione un joker:"))
            while jokerIndice < 1 or jokerIndice > 3:
                jokerIndice= int(input("La selección debe ser entre 1 y 3. Seleccione un joker:"))


        except ValueError:
            print("Ha ocurrido un error. Debe ingresar un numero")
            input("\nEnter para continuar...")
            juego.limpiarTerminal()
        else: 
            bandera=False

    
    jugador['jokers'].append(jokersRandoms[jokerIndice-1])
    jokersLista= jugador['jokersDisponibles']
    jokersLista.remove(jokersRandoms[jokerIndice-1])
    jugador['jokersDisponibles'] = jokersLista


    return jugador

def seleccionarPlaneta(jugador, planetas): #Función del sobre de planetas, se agarran al azar 3 planetas disponibles y el usuario puede agarrar solo 1.

    planetasRandoms = []
    nombres_planetas = list(planetas.keys())

    while len(planetasRandoms) < 3:
        nombre_random = random.choice(nombres_planetas)
        if nombre_random not in [p['nombre'] for p in planetasRandoms]:
            planeta = {
                "nombre": nombre_random,
                "jugada": planetas[nombre_random]["jugada"],
                "efecto": planetas[nombre_random]["efecto"],
                "incremento": planetas[nombre_random]["incremento"]
            }
            planetasRandoms.append(planeta)

    

    bandera = True
    while bandera:
        print("\n=== PLANETAS DISPONIBLES ===")
        for i in range(len(planetasRandoms)):
            planeta = planetasRandoms[i]
            print(f"{i + 1}. {planeta['nombre']} | Jugada: {planeta['jugada'].replace('_', ' ').title()}")
            print(f"   Efecto: {planeta['efecto']}")
            print(f"   Incremento → Fichas: +{planeta['incremento']['fichas']}, Multiplicador: +{planeta['incremento']['multiplicador']}")
            print()

        try:
            indice = int(input("Seleccione el número del planeta que desea (1-3): "))
            while indice < 1 or indice > 3:
                indice = int(input("Número inválido. Ingrese 1, 2 o 3: "))
        except ValueError:
            print("Debe ingresar un número válido.")
            input("\nEnter para continuar...")
            juego.limpiarTerminal()
        else:
            bandera = False

    planeta_elegido = planetasRandoms[indice - 1]

    fichas,multiplicador = jugador["combinaciones"][planeta_elegido["jugada"]]
    fichas += planeta_elegido['incremento']['fichas']
    multiplicador += planeta_elegido['incremento']['multiplicador']
    jugador["combinaciones"][planeta_elegido["jugada"]] = (fichas,multiplicador)



    print(f"\nHas elegido el planeta {planeta_elegido['nombre']}.")
    print(f"Efecto: {planeta_elegido['efecto']}")
    print("¡Fue agregado correctamente a tu colección!\n")
    input("\nEnter para continuar...")


    return jugador


def seleccionarNuevaCarta(jugador, mazo): #Función del sobre de cartas de mazo, se agarran al azar 3 cartas de mazo y el usuario puede agarrar solo 1.

    cartasRandoms = []

    while len(cartasRandoms) < 3:
        cartaRandom = random.choice(mazo)
        if cartaRandom not in cartasRandoms:
            cartasRandoms.append(cartaRandom)

    bandera = True
    while bandera:
        print("\n=== NUEVAS CARTAS DISPONIBLES ===")
        for i in range(len(cartasRandoms)):
            carta = cartasRandoms[i]
            print(f"{i + 1}. {carta['nombre']} | Valor: {carta['valor']} | Palo: {carta['palo']} | Fichas: {carta['fichas']}")

        try:
            indice = int(input("\nSeleccione el número de la carta que desea (1-3): "))
            while indice < 1 or indice > 3:
                indice = int(input("Número inválido. Ingrese 1, 2 o 3: "))
        except ValueError:
            print("Debe ingresar un número válido.")
        else:
            bandera = False

    carta_elegida = cartasRandoms[indice - 1]

    jugador['mazoCompleto'].append(carta_elegida)

    print(f"\nHas elegido la carta {carta_elegida['nombre']} ({carta_elegida['palo']}) con valor {carta_elegida['valor']}.")
    print("¡Fue agregada correctamente a tu mazo!\n")

    return jugador