import jokers

def test_calcularFichaPuntaje(): #Testea la Función calcularFichaPuntaje 

    fichas , multiplicador = jokers.calcularFichaPuntaje({"nombre": "Par", "descripcion": "Si la mano es Par, multiplica x3.", "tipo_bonificacion": "multiplicar", "bonificacion": 3, "probabilidad": 0.70, "rareza": "común"}, 30, 3, 3)
    assert fichas == 30 and multiplicador == 9

    fichas , multiplicador = jokers.calcularFichaPuntaje({"nombre": "Color Favorito", "descripcion": "Mismo palo en toda la jugada suma 200 fichas.", "tipo_bonificacion": "puntaje", "bonificacion": 200, "probabilidad": 0.62, "rareza": "común"}, 30, 3, 200)
    assert fichas == 230 and multiplicador == 3

    fichas , multiplicador = jokers.calcularFichaPuntaje({"nombre": "Rey del Multiplicador", "descripcion": "Aumenta el multiplicador base +1.", "tipo_bonificacion": "sum_multiplicador", "bonificacion": 1, "probabilidad": 0.58, "rareza": "común"}, 30, 3, 1)
    assert fichas == 30 and multiplicador == 4


