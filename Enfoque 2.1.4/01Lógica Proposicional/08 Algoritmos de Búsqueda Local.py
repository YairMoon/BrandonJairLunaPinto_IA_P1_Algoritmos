import random

# WalkSAT: algoritmo simple de búsqueda local
def walksat(clauses, symbols, max_flips=1000):
    model = {s: random.choice([True, False]) for s in symbols}
    for _ in range(max_flips):
        if all(any(model.get(lit.strip('-'), False) if '-' not in lit else not model.get(lit[1:], False)
                   for lit in clause) for clause in clauses):
            return model
        clause = random.choice([c for c in clauses if not any(
            model.get(lit.strip('-'), False) if '-' not in lit else not model.get(lit[1:], False)
            for lit in c)])
        var = random.choice(clause).strip('-')
        model[var] = not model[var]
    return None

# Prueba con cláusulas (forma: lista de listas)
clausulas = [["p", "-q"], ["-p", "r"], ["q", "-r"]]
simbolos = ["p", "q", "r"]

solucion = walksat(clausulas, simbolos)
print("Solución encontrada por WalkSAT:", solucion)
# Si la solución es None, significa que no se encontró una solución satisfactoria.
# Si se encontró una solución, se mostrará un diccionario con la asignación de variables.