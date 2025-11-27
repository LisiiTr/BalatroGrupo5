import combinaciones

def testFullHouse():
	resultado = combinaciones.fullHouse([4,4,4,5,5])
	assert resultado == True
	resultado = combinaciones.fullHouse([4,5,4,5,4])
	assert resultado == True
	resultado = combinaciones.fullHouse([4,5,4,5,5])
	assert resultado == True
	resultado = combinaciones.fullHouse([4,3,4,5,5])
	assert resultado == False
	resultado = combinaciones.fullHouse([4,3,4,4])
	assert resultado == False	
	resultado = combinaciones.fullHouse([4,3,4])
	assert resultado == False
	resultado = combinaciones.fullHouse([4,3])
	assert resultado == False
	resultado = combinaciones.fullHouse([4])
	assert resultado == False

def testEscalera():
	resultado = combinaciones.escalera([1,2,3,4,5])
	assert resultado == True
	resultado = combinaciones.escalera([6,7,8,9,10])
	assert resultado == True
	resultado = combinaciones.escalera([9,10,11,12,13])
	assert resultado == True
	resultado = combinaciones.escalera([5,4,3,2,1])
	assert resultado == True
	resultado = combinaciones.escalera([10,9,12,11,13])
	assert resultado == True	
	resultado = combinaciones.escalera([2,3,4])
	assert resultado == False
	resultado = combinaciones.escalera([2,3])
	assert resultado == False
	resultado = combinaciones.escalera([2])
	assert resultado == False

def testPoker():
	resultado = combinaciones.poker([2,2,2,2,5])
	assert resultado == True
	resultado = combinaciones.poker([4,5,4,4,4])
	assert resultado == True
	resultado = combinaciones.poker([1,1,6,1,1])
	assert resultado == True
	resultado = combinaciones.poker([11,11,11,11])
	assert resultado == True
	resultado = combinaciones.poker([7,7,7,3,5])
	assert resultado == False
	resultado = combinaciones.poker([8,8,3,3,8])
	assert resultado == False
	resultado = combinaciones.poker([9,6,10,6,9])
	assert resultado == False

def test_par():
	resultado=combinaciones.par([2,2,4,5,6])
	assert resultado == True
	resultado=combinaciones.par([3,3,4,4,6])
	assert resultado == True
	resultado=combinaciones.par([2,1,4,5,6])
	assert resultado == False
	resultado=combinaciones.par([1,1,1,7,8])
	assert resultado == False
	resultado=combinaciones.par([9,9,6,6,6])
	assert resultado == True
	resultado=combinaciones.par([2,2])
	assert resultado == True
	resultado=combinaciones.par([2,3,2])
	assert resultado == True
	resultado=combinaciones.par([1,6,6,6,6])
	assert resultado == False

def test_doblepar():
	resultado=combinaciones.doblePar([1,1,2,2,2])
	assert resultado == False
	resultado=combinaciones.doblePar([2,2,4,4,3])
	assert resultado == True
	resultado=combinaciones.doblePar([5,3,2,2,6])
	assert resultado == False
	resultado=combinaciones.doblePar([7,8,7,8,9])
	assert resultado == True
	resultado=combinaciones.doblePar([4,5,2,2,2])
	assert resultado == False
	resultado=combinaciones.doblePar([8,9,9,9,9])
	assert resultado == False

def test_trio():
	resultado=combinaciones.trio([1,1,2,2,2])
	assert resultado == True
	resultado=combinaciones.trio([1,1,1,6,5])
	assert resultado == True
	resultado=combinaciones.trio([1,2,3,4,5])
	assert resultado == False
	resultado=combinaciones.trio([1,1,2,2,7])
	assert resultado == False
	resultado=combinaciones.trio([8,8,8,8,3])
	assert resultado == False
	resultado=combinaciones.trio([1,3,1,4,1])
	assert resultado == True
	resultado=combinaciones.trio([9,9,5,2,3])
	assert resultado == False

def testColor():
    assert combinaciones.color(['♥','♥','♥','♥','♥']) == True # True: 5 corazones
    assert combinaciones.color(['♥','♥','♣','♥','♥']) == False  # False: mezcla de palos
    assert combinaciones.color(['♥','♥','♥','♥']) == False # False: longitud distinta de 5

def test_dividirPaloValores():
	# Caso de prueba: una mano de 5 cartas con distintos valores y palos (con un valor repetido).
    cartas = [
        {"valor": 1,  "palo": "♠"},
        {"valor": 10, "palo": "♥"},
        {"valor": 13, "palo": "♦"},
        {"valor": 7,  "palo": "♣"},
        {"valor": 5,  "palo": "♣"},
    ]
	# Asegura que la funcion separa correctamente una lista de cartas en dos listas paralelas de valor y palo, sin perder el orden 
    valores, palos = combinaciones.dividirPaloValores(cartas)
    assert valores == [1,10,13,7,5]
    assert palos   == ["♠","♥","♦","♣","♣"]

def test_analizarCombinacionesJokers_flags():
    # Caso de prueba: escalera de color (5 consecutivas mismo palo)
    cartas_test = [
        {"valor": 5, "palo": "♥"},
        {"valor": 6, "palo": "♥"},
        {"valor": 7, "palo": "♥"},
        {"valor": 8, "palo": "♥"},
        {"valor": 9, "palo": "♥"},
    ]
	# Debe detectar escalera de color (ambas banderas verdaderas y la combinada también)
    assert combinaciones.analizarCombinacionesJokers(cartas_test)["escalera_corrida"] == True # color + escalera
    assert combinaciones.analizarCombinacionesJokers(cartas_test)["color"] == True # mismo palo en 5 cartas
    assert combinaciones.analizarCombinacionesJokers(cartas_test)["escalera"] == True # 5 valores consecutivos
	# Asegura que no marque otras combinaciones que no sea "escalera"
    assert combinaciones.analizarCombinacionesJokers(cartas_test)["poker"] == False # no hay 4 iguales
    assert combinaciones.analizarCombinacionesJokers(cartas_test)["full_house"] == False # no hay 3+2