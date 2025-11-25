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


