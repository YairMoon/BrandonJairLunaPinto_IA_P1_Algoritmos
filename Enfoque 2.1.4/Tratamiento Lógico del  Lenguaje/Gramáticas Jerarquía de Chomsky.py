# La jerarquía de Chomsky clasifica las gramáticas en 4 tipos según su poder expresivo:
# Tipo 0: Gramáticas no restringidas
# Tipo 1: Gramáticas sensibles al contexto
# Tipo 2: Gramáticas libres de contexto
# Tipo 3: Gramáticas regulares

# Vamos a definir un ejemplo de gramática libre de contexto (Tipo 2)
# La regla de producción será: S -> aSb | ε

# Función para verificar si una cadena es válida según una gramática
def es_valida_cadena(cadena):
    if cadena == "":
        return True
    elif cadena[0] == "a" and cadena[-1] == "b":
        return es_valida_cadena(cadena[1:-1])
    else:
        return False

# Ejemplo de uso
print(es_valida_cadena("aabb"))  # True
print(es_valida_cadena("ab"))    # True
print(es_valida_cadena("aaabbb"))  # True
print(es_valida_cadena("abc"))   # False
