def backjumping_search(csp, assignment={}, level=0, conflict={}): # Búsqueda con Salto Atrás Dirigido por Conflictos (Backjumping Search)
    """
    Implementa el algoritmo de búsqueda con salto atrás dirigido por conflictos (Backjumping Search).
    
    :param csp: Objeto CSP que contiene variables, dominios, vecinos y restricciones.
    :param assignment: Diccionario que representa la asignación actual de variables.
    :param level: Nivel actual de la búsqueda (profundidad en el árbol de búsqueda).
    :param conflict: Diccionario que almacena los conflictos para cada variable.
    :return: Una asignación completa que satisface las restricciones o None si no hay solución.
    """
    # Si todas las variables están asignadas, retornamos la solución
    if len(assignment) == len(csp.variables):
        return assignment

    # Seleccionamos la primera variable no asignada
    var = [v for v in csp.variables if v not in assignment][0]

    # Probamos cada valor del dominio de la variable seleccionada
    for value in csp.domains[var]:
        if csp.is_consistent(var, value, assignment):  # Verificamos si la asignación es consistente
            assignment[var] = value  # Asignamos el valor a la variable
            result = backjumping_search(csp, assignment, level + 1, conflict)  # Llamada recursiva
            if result:
                return result  # Si encontramos una solución, la retornamos
            del assignment[var]  # Si no hay solución, deshacemos la asignación
        else:
            # Guardamos los conflictos para realizar el salto
            for neighbor in csp.neighbors[var]:
                if neighbor in assignment:  # Solo consideramos vecinos ya asignados
                    conflict[var] = conflict.get(var, set()) | {neighbor}  # Registramos el conflicto

    # Si hay conflictos, realizamos el salto atrás
    if var in conflict:
        # Aquí se puede implementar lógica para saltar al nivel más alto con conflicto
        return None  # Actualmente, simplemente retornamos None

    return None  # Si no encontramos solución, retornamos None