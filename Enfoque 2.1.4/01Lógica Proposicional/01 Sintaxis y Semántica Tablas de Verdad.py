from itertools import product

# Definimos una función para imprimir la tabla de verdad
def tabla_verdad(expr, variables):
    # Iteramos sobre todas las combinaciones posibles de valores de verdad
    for valores in product([False, True], repeat=len(variables)):
        # Creamos un diccionario que asocia cada variable con un valor
        asignacion = dict(zip(variables, valores))
        # Evaluamos la expresión con los valores actuales
        resultado = eval(expr, {}, asignacion)
        # Mostramos la asignación y el resultado
        print(asignacion, "=>", resultado)

# Definimos una expresión lógica como string y sus variables
expresion = "(p and q) or not r"
variables = ['p', 'q', 'r']

# Llamamos a la función para mostrar la tabla de verdad
tabla_verdad(expresion, variables)
# La salida mostrará todas las combinaciones de valores de p, q y r, junto con el resultado de la expresión lógica.