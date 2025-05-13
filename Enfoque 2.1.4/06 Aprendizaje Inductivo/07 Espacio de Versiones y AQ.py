# Simulación de espacio de versiones utilizando un algoritmo AQ (algoritmo de aprendizaje)
# Definimos un conjunto de datos simple con características y etiquetas

# Características: [X, Y], Etiquetas: Z (la clase)
# Vamos a usar un conjunto de reglas para representar un conjunto de hipótesis

reglas = [
    {"condiciones": [("X", ">", 2), ("Y", "<", 4)], "clase": "A"},
    {"condiciones": [("X", "<=", 2), ("Y", ">=", 4)], "clase": "B"}
]

def clasificar(X, Y):
    for regla in reglas:
        condiciones = regla["condiciones"]
        if all(cond[0] == "X" and X > cond[2] or cond[0] == "Y" and Y < cond[2] for cond in condiciones):
            return regla["clase"]
    return "Desconocido"

# Probamos el clasificador AQ
print(clasificar(3, 5))  # Clase A
print(clasificar(1, 4))  # Clase B
