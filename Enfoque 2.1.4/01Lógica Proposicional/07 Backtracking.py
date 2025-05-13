from itertools import product

# Evalúa si hay una combinación que haga verdadera la expresión
def satisfacible(expr, variables):
    for valores in product([False, True], repeat=len(variables)):
        asignacion = dict(zip(variables, valores))
        if eval(expr, {}, asignacion):
            return True, asignacion
    return False, None

# Expresión y variables
expresion = "p and not q"
variables = ["p", "q"]

# Comprobamos satisfacibilidad
es_satis, asignacion = satisfacible(expresion, variables)
print("¿Es satisfacible?", es_satis)
if es_satis:
    print("Asignación que satisface:", asignacion)
# La salida mostrará True si la expresión es satisfacible y False si no lo es.
# En este caso, "p and not q" es satisfacible si p es verdadero y q es falso.
