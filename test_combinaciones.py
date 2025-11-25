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
	resultado = combinaciones.escalera([5,4,3,2,1]) #La escalera es solo ascendente?
	assert resultado == False
	resultado = combinaciones.escalera([10,9,12,11,13])
	assert resultado == False	
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