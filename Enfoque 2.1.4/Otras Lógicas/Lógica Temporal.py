# Simulación básica de lógica temporal con una secuencia de estados

# Estados del sistema en el tiempo
tiempo = [
    {"luz": "apagada"},
    {"luz": "encendida"},
    {"luz": "encendida"},
    {"luz": "apagada"},
]

# ¿Estuvo encendida alguna vez?
def fue_verdadero(prop, valor):
    return any(estado.get(prop) == valor for estado in tiempo)

# ¿Siempre ha estado encendida?
def siempre_verdadero(prop, valor):
    return all(estado.get(prop) == valor for estado in tiempo)

print("¿La luz estuvo encendida alguna vez?", fue_verdadero("luz", "encendida"))
print("¿La luz siempre estuvo encendida?", siempre_verdadero("luz", "encendida"))
# Salida esperada:
# ¿La luz estuvo encendida alguna vez? True