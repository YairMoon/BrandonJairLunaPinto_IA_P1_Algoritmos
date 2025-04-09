class CSP:
    def __init__(self, variables, domains, neighbors, constraints):
        # Lista de variables (por ejemplo, regiones del mapa)
        self.variables = variables

        # Diccionario de dominios: variable -> lista de valores posibles
        self.domains = domains

        # Diccionario de vecinos: variable -> lista de variables vecinas
        self.neighbors = neighbors

        # Función de restricciones que toma (A, a, B, b) y devuelve True si es válido
        self.constraints = constraints

    def is_consistent(self, var, value, assignment):
        # Verifica si asignar 'value' a 'var' no viola restricciones con los vecinos ya asignados
        for neighbor in self.neighbors[var]:
            if neighbor in assignment:
                if not self.constraints(var, value, neighbor, assignment[neighbor]):
                    return False
        return True
