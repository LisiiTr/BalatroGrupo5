import random

planetas = {
    "Mercurio": {
        "jugada": "Par",
        "efecto": "Aumenta las fichas base y el multiplicador del Par.",
        "incremento": {"fichas": 15, "multiplicador": 1}
    },
    "Venus": {
        "jugada": "Doble Par",
        "efecto": "Aumenta las fichas base y el multiplicador del Doble Par.",
        "incremento": {"fichas": 20, "multiplicador": 1}
    },
    "Tierra": {
        "jugada": "Trío",
        "efecto": "Aumenta las fichas base y el multiplicador del Trío.",
        "incremento": {"fichas": 30, "multiplicador": 1}
    },
    "Marte": {
        "jugada": "Escalera",
        "efecto": "Aumenta las fichas base y el multiplicador de la Escalera.",
        "incremento": {"fichas": 40, "multiplicador": 1}
    },
    "Júpiter": {
        "jugada": "Color",
        "efecto": "Aumenta las fichas base y el multiplicador del Color.",
        "incremento": {"fichas": 50, "multiplicador": 1}
    },
    "Saturno": {
        "jugada": "Full House",
        "efecto": "Aumenta las fichas base y el multiplicador del Full House.",
        "incremento": {"fichas": 60, "multiplicador": 1}
    },
    "Urano": {
        "jugada": "Póker (4 iguales)",
        "efecto": "Aumenta las fichas base y el multiplicador del Póker.",
        "incremento": {"fichas": 70, "multiplicador": 1}
    },
    "Neptuno": {
        "jugada": "Escalera de color",
        "efecto": "Aumenta las fichas base y el multiplicador de la Escalera de color.",
        "incremento": {"fichas": 80, "multiplicador": 1}
    },
    "Plutón": {
        "jugada": "Carta Alta",
        "efecto": "Aumenta ligeramente las fichas base y el multiplicador de la Carta Alta.",
        "incremento": {"fichas": 10, "multiplicador": 0}
    }
}


jokers = (
    #Comunes
    {"nombre": "Par", "descripcion": "Si la mano es Par, multiplica x3.", "tipo_bonificacion": "multiplicar", "bonificacion": 3, "probabilidad": 0.70, "rareza": "común"},
    {"nombre": "Color Favorito", "descripcion": "Mismo palo en toda la jugada suma 200 fichas.", "tipo_bonificacion": "puntaje", "bonificacion": 200, "probabilidad": 0.62, "rareza": "común"},
    {"nombre": "Corazón Generoso", "descripcion": "Cada corazón aporta +25 fichas.", "tipo_bonificacion": "puntaje", "bonificacion": 25, "probabilidad": 0.68, "rareza": "común"},
    {"nombre": "As de Oro", "descripcion": "Si aparece cualquier As, suma +100 fichas.", "tipo_bonificacion": "puntaje", "bonificacion": 100, "probabilidad": 0.65, "rareza": "común"},
    {"nombre": "Rey del Multiplicador", "descripcion": "Aumenta el multiplicador base +1.", "tipo_bonificacion": "sum_multiplicador", "bonificacion": 1, "probabilidad": 0.58, "rareza": "común"},
    {"nombre": "Dupla Segura", "descripcion": "Parejas suman +150 fichas.", "tipo_bonificacion": "puntaje", "bonificacion": 150, "probabilidad": 0.60, "rareza": "común"},
    {"nombre": "Punta y Hacha", "descripcion": "Cartas 2–5 suman +20 fichas cada una.", "tipo_bonificacion": "puntaje", "bonificacion": 20, "probabilidad": 0.66, "rareza": "común"},
    {"nombre": "Dama Cortés", "descripcion": "Si hay al menos una Dama, +1 al multiplicador.", "tipo_bonificacion": "sum_multiplicador", "bonificacion": 1, "probabilidad": 0.55, "rareza": "común"},
    {"nombre": "Trío Amable", "descripcion": "Si la mano es Trío, multiplica x2.", "tipo_bonificacion": "multiplicar", "bonificacion": 2, "probabilidad": 0.57, "rareza": "común"},
    {"nombre": "Diez Limpio", "descripcion": "Cada carta 10 suma +30 fichas.", "tipo_bonificacion": "puntaje", "bonificacion": 30, "probabilidad": 0.63, "rareza": "común"},

    #Raros
    {"nombre": "Triple Doble", "descripcion": "Dobles parejas obtienen multiplicador x2 adicional.", "tipo_bonificacion": "multiplicar", "bonificacion": 2, "probabilidad": 0.42, "rareza": "raro"},
    {"nombre": "Dama de Fortuna", "descripcion": "Si hay una Dama, +2 al multiplicador.", "tipo_bonificacion": "sum_multiplicador", "bonificacion": 2, "probabilidad": 0.40, "rareza": "raro"},
    {"nombre": "Palo Fiel", "descripcion": "Por cada carta del mismo palo, +80 fichas.", "tipo_bonificacion": "puntaje", "bonificacion": 80, "probabilidad": 0.38, "rareza": "raro"},
    {"nombre": "Escalera Realista", "descripcion": "Escalera o escalera real multiplica x4.", "tipo_bonificacion": "multiplicar", "bonificacion": 4, "probabilidad": 0.32, "rareza": "raro"},
    {"nombre": "Doble As", "descripcion": "Por cada As en la mano, +2 al multiplicador.", "tipo_bonificacion": "sum_multiplicador", "bonificacion": 2, "probabilidad": 0.35, "rareza": "raro"},
    {"nombre": "Sota Traviesa", "descripcion": "Cada J (Sota) suma +120 fichas.", "tipo_bonificacion": "puntaje", "bonificacion": 120, "probabilidad": 0.36, "rareza": "raro"},
    {"nombre": "Poker", "descripcion": "Si hay 4 cartas del mismo rango, multiplica x3.", "tipo_bonificacion": "multiplicar", "bonificacion": 3, "probabilidad": 0.28, "rareza": "raro"},
    {"nombre": "Rey de Copas", "descripcion": "Cada Rey otorga +2 al multiplicador.", "tipo_bonificacion": "sum_multiplicador", "bonificacion": 2, "probabilidad": 0.30, "rareza": "raro"},

    #Legendarios 
    {"nombre": "Joker Comodín", "descripcion": "Full House duplica el multiplicador (x4).", "tipo_bonificacion": "multiplicar", "bonificacion": 4, "probabilidad": 0.12, "rareza": "legendario"},
    {"nombre": "As de Picas", "descripcion": "Si hay As de picas, +500 fichas.", "tipo_bonificacion": "puntaje", "bonificacion": 500, "probabilidad": 0.10, "rareza": "legendario"},
    {"nombre": "Corona Triple", "descripcion": "Si hay 3 figuras (J/Q/K) en la mano, multiplica x6.", "tipo_bonificacion": "multiplicar", "bonificacion": 6, "probabilidad": 0.07, "rareza": "legendario"},
    {"nombre": "Motor Infinito", "descripcion": "Hand ganadora obtiene +5 al multiplicador base.", "tipo_bonificacion": "sum_multiplicador", "bonificacion": 5, "probabilidad": 0.06, "rareza": "legendario"},
    {"nombre": "Tesoro Oculto", "descripcion": "Color + Escalera en la misma mano multiplica x8.", "tipo_bonificacion": "multiplicar", "bonificacion": 8, "probabilidad": 0.05, "rareza": "legendario"},
    {"nombre": "Fortuna Eterna", "descripcion": "Si la mano supera cierto umbral de fichas, suma +800 fichas.", "tipo_bonificacion": "puntaje", "bonificacion": 800, "probabilidad": 0.04, "rareza": "legendario"}
)