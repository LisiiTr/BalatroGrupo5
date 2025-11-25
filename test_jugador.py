import jugador


def test_sumarPuntajeRanking():
    resultado = jugador.sumarPuntajeRanking(jugador={'puntaje': 200,
                                             'puntaje_ranking': 0})
    assert resultado['puntaje_ranking'] == 200
    
    resultado = jugador.sumarPuntajeRanking(jugador={'puntaje': 300,
                                             'puntaje_ranking': 200})
    assert resultado['puntaje_ranking'] == 500

    resultado = jugador.sumarPuntajeRanking(jugador={'puntaje': 0,
                                             'puntaje_ranking': 200})
    assert resultado['puntaje_ranking'] == 200
