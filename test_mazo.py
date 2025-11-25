import mazo

def test_fichasValor():
    resultado = mazo.fichasValor(3)
    assert resultado == 3
    resultado = mazo.fichasValor(1)
    assert resultado == 11
    resultado = mazo.fichasValor(2)
    assert resultado == 2
    resultado = mazo.fichasValor(10)
    assert resultado == 10
    resultado = mazo.fichasValor(11)
    assert resultado == 10
    resultado = mazo.fichasValor(12)
    assert resultado == 10
    resultado = mazo.fichasValor(13)
    assert resultado == 10

def test_crearMazoCompleto():
    resultado = mazo.crearMazoCompleto()
    assert len(resultado) == 52

def test_repartirCartas():
    resultado =  mazo.repartirCartas(10,jugador = { 'mazoCompleto' : mazo.crearMazoCompleto() ,
                                                      'mazoRonda' : mazo.crearMazoCompleto(),
                                                      'manoJugador': []} )
    assert len(resultado['manoJugador']) == 10
    resultado =  mazo.repartirCartas(3,jugador = { 'mazoCompleto' : mazo.crearMazoCompleto() ,
                                                      'mazoRonda' : mazo.crearMazoCompleto(),
                                                      'manoJugador': []} )
    assert len(resultado['manoJugador']) == 3
    resultado =  mazo.repartirCartas(0,jugador = { 'mazoCompleto' : mazo.crearMazoCompleto() ,
                                                      'mazoRonda' : mazo.crearMazoCompleto(),
                                                      'manoJugador': []} )
    assert len(resultado['manoJugador']) == 0


