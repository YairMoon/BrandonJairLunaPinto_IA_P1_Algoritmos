def backtracking_search(csp, assignment={}): # Búsqueda de Vuelta Atrás (Backtracking Search)
    """
    Implementa el algoritmo de búsqueda de vuelta atrás (Backtracking Search) para resolver un CSP.
    
    :param csp: Objeto CSP que contiene variables, dominios, vecinos y restricciones.
    :param assignment: Diccionario que representa la asignación actual de variables.
    :return: Una asignación completa que satisface las restricciones o None si no hay solución.
    """
    # Si ya se asignaron todas las variables, retorna la solución
    if len(assignment) == len(csp.variables):
        return assignment  # Retornamos la asignación completa.

    # Elegimos la siguiente variable no asignada
    unassigned = [v for v in csp.variables if v not in assignment]  # Variables sin asignar.
    var = unassigned[0]  # Seleccionamos la primera variable no asignada.

    # Probamos cada valor del dominio
    for value in csp.domains[var]:
        if csp.is_consistent(var, value, assignment):  # Verificamos si la asignación es consistente.
            # Si es consistente, asignamos y continuamos recursivamente
            assignment[var] = value  # Asignamos el valor a la variable.
            result = backtracking_search(csp, assignment)  # Llamada recursiva.
            if result:
                return result  # Si encontramos una solución, la retornamos.
            # Si no resultó, deshacemos (backtrack)
            del assignment[var]  # Eliminamos la asignación y retrocedemos.

    return None  # Si no hay solución, retornamos None.