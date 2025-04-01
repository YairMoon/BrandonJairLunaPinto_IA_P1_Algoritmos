import random

# Búsqueda de Haz Local (Local Beam Search)
def local_beam_search(problem, heuristic, k=2, max_iterations=100):
    """
    Implementa el algoritmo de búsqueda de haz local.
    
    :param problem: Espacio del problema representado como un diccionario {nodo: [vecinos]}
    :param heuristic: Función heurística h(n)
    :param k: Número de estados a mantener en cada iteración
    :param max_iterations: Número máximo de iteraciones
    :return: Mejor solución encontrada
    """
    current_states = random.sample(list(problem.keys()), k)  # Selección aleatoria de k nodos iniciales
    
    for _ in range(max_iterations):
        all_neighbors = []
        for state in current_states:
            neighbors = problem.get(state, [])
            all_neighbors.extend(neighbors)  # Recolectamos todos los vecinos
        
        if not all_neighbors:
            break  # Si no hay vecinos, terminamos
        
        # Seleccionamos los k mejores vecinos según la heurística
        current_states = sorted(all_neighbors, key=heuristic, reverse=True)[:k]
    
    return max(current_states, key=heuristic)  # Retornamos el mejor estado encontrado

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
best_solution = local_beam_search(graph, heuristic)
print("Mejor solución encontrada por Búsqueda de Haz Local:", best_solution)
# Output esperado: Mejor solución encontrada por Búsqueda de Haz Local: G
# El resultado puede variar debido a la naturaleza aleatoria de la selección de nodos iniciales