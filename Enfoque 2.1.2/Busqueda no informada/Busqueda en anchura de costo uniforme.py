from queue import PriorityQueue

# Búsqueda de Costo Uniforme (Uniform Cost Search - UCS)
def uniform_cost_search(graph, start, goal):
    """
    Implementa el algoritmo de Búsqueda de Costo Uniforme.
    
    :param graph: Diccionario que representa el grafo con costos {nodo: {vecino: costo}}
    :param start: Nodo inicial
    :param goal: Nodo objetivo
    :return: Lista con el camino más barato desde start hasta goal o None si no hay camino
    """
    queue = PriorityQueue()  # Cola de prioridad para manejar caminos y costos
    queue.put((0, [start]))  # Insertamos el nodo inicial con costo 0
    visited = set()  # Conjunto de nodos visitados
    
    while not queue.empty():
        cost, path = queue.get()  # Extraemos el camino de menor costo
        node = path[-1]  # Último nodo del camino actual
        
        if node == goal:
            return path  # Si encontramos el objetivo, retornamos el camino
        
        if node not in visited:
            visited.add(node)  # Marcamos el nodo como visitado
            for neighbor, weight in graph.get(node, {}).items():  # Exploramos vecinos
                new_path = list(path)  # Copiamos el camino actual
                new_path.append(neighbor)  # Agregamos el vecino
                queue.put((cost + weight, new_path))  # Lo agregamos con su costo actualizado
    
    return None  # Si no encontramos el objetivo, retornamos None

# Ejemplo de uso
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'F': 3},
    'D': {},
    'E': {'F': 1},
    'F': {}
}

start = 'A'
goal = 'F'
print("Camino encontrado por UCS:", uniform_cost_search(graph, start, goal))
