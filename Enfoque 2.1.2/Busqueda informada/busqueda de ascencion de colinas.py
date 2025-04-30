import random

# Búsqueda de Ascensión de Colinas (Hill Climbing Search)
def hill_climbing(problem, heuristic):
    """
    Implementa el algoritmo de ascensión de colinas.
    
    :param problem: Espacio del problema representado como un diccionario {nodo: [vecinos]}
    :param heuristic: Función heurística h(n)
    :return: Mejor solución encontrada
    """
    current = random.choice(list(problem.keys()))  # Seleccionamos un nodo inicial aleatorio
    while True:
        neighbors = problem.get(current, [])  # Obtenemos los vecinos
        if not neighbors:
            return current  # Si no hay vecinos, retornamos el nodo actual como solución
        
        best_neighbor = max(neighbors, key=heuristic)  # Seleccionamos el mejor vecino según la heurística
        if heuristic(best_neighbor) <= heuristic(current):
            return current  # Si no hay mejora, retornamos el nodo actual
        current = best_neighbor  # Movemos al mejor vecino

# Definimos el espacio del problema
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# Definimos la función heurística
def heuristic(node):
    values = {'A': 1, 'B': 3, 'C': 2, 'D': 0, 'E': 5, 'F': 1, 'G': 6}
    return values.get(node, 0)

# Ejecutar la búsqueda
global_best = hill_climbing(graph, heuristic)
print("Mejor solución encontrada por Ascensión de Colinas:", global_best)
# Output esperado: Mejor solución encontrada por Ascensión de Colinas: D
# El resultado puede variar debido a la naturaleza aleatoria de la selección del nodo inicial