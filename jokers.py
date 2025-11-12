import random
import combinaciones

def analizarMano(cartasJugadas):
    analisis= {}
    conteo_valores={}
    conteo_palos={}
    figuras=0
    ases=0
    valores,palos= combinaciones.dividirPaloValores(cartasJugadas)
    valores_unicos= set(valores)
    palos_unicos= set(palos)
    datos_combinaciones = combinaciones.analizarCombinacionesJokers(cartasJugadas)
    
    
    for valor in valores_unicos:
        conteo_valores[valor]=valores.count(valor)
    
    dieces= valores.count(13)
    sotas= valores.count(11)
    damas= valores.count(12)
    reyes= valores.count(13)
    rango_2_5=  valores.count(2) + valores.count(3) + valores.count(4) + valores.count(5)
    figuras= valores.count(11) + valores.count(12) + valores.count(13)
    ases= valores.count(1)
    corazones= palos.count('♥')

    for palo in palos_unicos:
        conteo_palos[palo]=palos.count(palo)


    analisis["conteo_valores"]=conteo_valores
    analisis["conteo_palos"]=conteo_palos
    analisis["figuras"]=figuras
    analisis["ases"]=ases
    analisis["rango_2_5"]=rango_2_5
    analisis["max_mismo_palo"]= max([palo for palo in analisis['conteo_palos'].values()])

    analisis["dieces"]=dieces
    analisis["sotas"]=sotas
    analisis["damas"]=damas
    analisis["reyes"]=reyes

    analisis["corazones"]=corazones

    analisis.update(datos_combinaciones)   

    return analisis
        
def calcularFichaPuntaje(joker, fichas, multiplicador, bonificacion):
    if joker["tipo_bonificacion"] == "sum_multiplicador":
        multiplicador += bonificacion
    elif joker["tipo_bonificacion"] == "puntaje":
        fichas  += bonificacion
    elif joker["tipo_bonificacion"] == "multiplicar":
        multiplicador = multiplicador * bonificacion

    return fichas,multiplicador
        

def detectarJokers(jugador,cartasJugadas, analisis, fichas, multiplicador):

    print(f"\n Los Jokers activados son: ")

    for joker in jugador["jokers"]:
        bonificar = False
        nombre = joker["nombre"]

        if nombre == "Par" and analisis["par"]:
            bonificacion=  joker['bonificacion']
            bonificar = True

        elif nombre == "Color Favorito" and analisis["color"]:
            bonificacion=  joker['bonificacion']
            bonificar = True

        elif nombre == "Corazón Generoso" and analisis["corazones"] > 0:
            bonificacion=  joker['bonificacion'] * analisis["corazones"]
            bonificar = True

        elif nombre == "As de Oro" and analisis["ases"] >= 1:
            bonificacion=  joker['bonificacion']
            bonificar = True

        elif nombre == "Rey del Multiplicador" and analisis["reyes"] >= 1:
            bonificacion=  joker['bonificacion'] * analisis["reyes"]
            bonificar = True

        elif nombre == "Dupla Segura" and (analisis["doble_par"] or analisis["par"]):
            bonificacion=  joker['bonificacion']
            bonificar = True

        elif nombre == "Punta y Hacha" and analisis["rango_2_5"] > 0:
            bonificacion=  joker['bonificacion'] * analisis["rango_2_5"]
            bonificar = True

        elif nombre == "Dama Cortés" and analisis["damas"] >= 1:
            bonificacion=  joker['bonificacion']
            bonificar = True

        elif nombre == "Trío Amable" and analisis["trio"]:
            bonificacion=  joker['bonificacion']
            bonificar = True

        elif nombre == "Diez Limpio" and analisis["dieces"] >= 1:
            bonificacion=  joker['bonificacion'] * analisis["dieces"]
            bonificar = True

        elif nombre == "Triple Doble" and analisis["doble_par"]:
            if analisis["doble_par"]:
                bonificacion=  joker['bonificacion']*1.5
            else:
                bonificacion=  joker['bonificacion']
            bonificar = True

        elif nombre == "Dama de Fortuna" and analisis["damas"] >= 1:
            bonificacion=  joker['bonificacion']
            bonificar = True

        elif nombre == "Palo Fiel" and analisis["max_mismo_palo"] >= 2:
            bonificacion=  joker['bonificacion']
            bonificar = True

        elif nombre == "Escalera Realista" and (analisis["escalera"] or analisis["escalera_corrida"]):
            bonificacion=  joker['bonificacion']
            bonificar = True

        elif nombre == "Doble As" and analisis["ases"] >= 2:
            bonificacion=  joker['bonificacion'] * analisis["ases"]
            bonificar = True

        elif nombre == "Sota Traviesa" and analisis["sotas"] >= 1:
            bonificacion=  joker['bonificacion'] * analisis["sotas"]
            bonificar = True

        elif nombre == "Poker" and analisis["poker"]:
            bonificacion=  joker['bonificacion'] 
            bonificar = True

        elif nombre == "Rey de Copas" and analisis["reyes"] >= 1:
            bonificacion=  joker['bonificacion'] * analisis["reyes"]
            bonificar = True

        elif nombre == "Joker Comodín" and analisis["full_house"]:
            bonificacion=  joker['bonificacion'] 
            bonificar = True

        elif nombre == "As de Picas" and ('A♠' in cartasJugadas):
            bonificacion=  joker['bonificacion'] 
            bonificar = True

        elif nombre == "Corona Triple" and analisis["figuras"] >= 3:
            bonificacion=  joker['bonificacion'] 
            bonificar = True

        elif nombre == "Motor Infinito" and analisis.get("ganadora", False):
            bonificacion=  joker['bonificacion'] 
            bonificar = True

        elif nombre == "Tesoro Oculto" and (analisis["color"] and analisis["escalera"]):
            bonificacion=  joker['bonificacion'] 
            bonificar = True

        elif nombre == "Fortuna Eterna" and fichas > (jugador["pozo"]*0.75):
            bonificacion=  joker['bonificacion'] 
            bonificar = True

        if bonificar:
            print(f"{nombre}.")
            fichas, multiplicador=calcularFichaPuntaje(joker, fichas, multiplicador,bonificacion)

    print(f"\n Las fichas acumuladas son: {fichas} | El multiplicador acumulado es:{multiplicador}")
    return  fichas, multiplicador

    



def calcularJokers(jugador,fichas, cartasJugadas, multiplicador):
    print(fichas, multiplicador)
    analisis=analizarMano(cartasJugadas)
    fichas, multiplicador= detectarJokers(jugador,cartasJugadas, analisis, fichas, multiplicador)
    print(fichas, multiplicador)


    return fichas, multiplicador