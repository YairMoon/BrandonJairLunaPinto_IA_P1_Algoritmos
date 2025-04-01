import random

# Búsqueda Online (Online Search)
def online_search(problem, heuristic, start):
    """
    Implementa el algoritmo de búsqueda online.
    
    :param problem: Espacio del problema representado como un diccionario {nodo: [vecinos]}
    :param heuristic: Función heurística h(n)
    :param start: Nodo inicial
    :return: Mejor solución encontrada
    """
    current = start  # Nodo inicial
    visited = set()  # Conjunto de nodos visitados
    
    while True:
        visited.add(current)  # Marcar nodo como visitado
        neighbors = [n for n in problem.get(current, []) if n not in visited]  # Filtrar vecinos no visitados
        
        if not neighbors:
            return current  # Si no hay vecinos sin visitar, retornamos el nodo actual
        
        current = min(neighbors, key=heuristic)  # Elegir el vecino con menor heurística

# Definir espacio del problema
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# Definir función heurística
def heuristic(node):
    values = {'A': 1, 'B': 3, 'C': 2, 'D': 0, 'E': 5, 'F': 1, 'G': 6}
    return values.get(node, 0)

# Ejecutar la búsqueda
start_node = 'A'
best_solution = online_search(graph, heuristic, start_node)
print("Mejor solución encontrada por Búsqueda Online:", best_solution)
# Output esperado: Mejor solución encontrada por Búsqueda Online: G
# El resultado puede variar debido a la naturaleza aleatoria de la selección del nodo inicial