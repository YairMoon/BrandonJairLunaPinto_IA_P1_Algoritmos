import random # Importamos la librería random para manejar la selección aleatoria.

def min_conflicts(csp, max_steps=1000): ## Definimos la función de búsqueda local con mínimos conflictos.
    """
    Implementa el algoritmo de Búsqueda Local con Mínimos Conflictos.
    
    :param csp: Objeto CSP que contiene variables, dominios, vecinos y restricciones.
    :param max_steps: Número máximo de pasos permitidos.
    :return: Una asignación completa que satisface las restricciones o None si no hay solución.
    """
    # Inicializamos una asignación aleatoria
    assignment = {var: random.choice(csp.domains[var]) for var in csp.variables}
    
    for _ in range(max_steps):
        # Verificamos si la asignación actual es consistente
        conflicted_vars = [
            var for var in csp.variables
            if not csp.is_consistent(var, assignment[var], assignment)
        ]
        if not conflicted_vars:  # Si no hay conflictos, retornamos la solución
            return assignment
        
        # Elegimos una variable en conflicto al azar
        var = random.choice(conflicted_vars)
        
        # Seleccionamos el valor que minimiza los conflictos
        assignment[var] = min(
            csp.domains[var],
            key=lambda value: count_conflicts(csp, var, value, assignment)
        )
    
    return None  # Si no encontramos solución en el número máximo de pasos

def count_conflicts(csp, var, value, assignment):
    """
    Cuenta el número de conflictos para una variable y un valor dados.
    
    :param csp: Objeto CSP.
    :param var: Variable a evaluar.
    :param value: Valor a asignar a la variable.
    :param assignment: Asignación actual.
    :return: Número de conflictos.
    """
    assignment[var] = value  # Asignamos temporalmente el valor
    conflicts = sum(
        not csp.is_consistent(var, value, assignment)
        for neighbor in csp.neighbors[var]
    )
    del assignment[var]  # Restauramos la asignación original
    return conflicts