from itertools import product

# Verifica si dos expresiones son equivalentes lógicamente
def son_equivalentes(expr1, expr2, variables):
    for valores in product([False, True], repeat=len(variables)):
        asignacion = dict(zip(variables, valores))
        if eval(expr1, {}, asignacion) != eval(expr2, {}, asignacion):
            return False
    return True

# Expresiones lógicas
expr1 = "p or q"
expr2 = "not (not p and not q)"
variables = ['p', 'q']

# Comprobación de equivalencia
print("¿Son equivalentes?", son_equivalentes(expr1, expr2, variables))
# La salida mostrará True si las expresiones son equivalentes y False si no lo son.
# En este caso, "p or q" es equivalente a "not (not p and not q)" según las leyes de De Morgan.
