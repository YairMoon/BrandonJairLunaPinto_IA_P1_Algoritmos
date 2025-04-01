import heapq

# Búsqueda Voraz Primero el Mejor (Greedy Best-First Search)
def greedy_best_first_search(graph, start, goal, heuristic):
    """
    Implementa la búsqueda voraz primero el mejor.
    
    :param graph: Diccionario que representa el grafo {nodo: [vecinos]}
    :param start: Nodo inicial
    :param goal: Nodo objetivo
    :param heuristic: Función heurística h(n)
    :return: Lista con el camino desde start hasta goal o None si no hay camino
    """
    frontier = []  # Cola de prioridad para la frontera
    heapq.heappush(frontier, (heuristic(start, goal), [start]))  # Inicializamos con el nodo inicial
    visited = set()  # Conjunto de nodos visitados
    
    while frontier:
        _, path = heapq.heappop(frontier)  # Extraemos el nodo con menor valor heurístico
        node = path[-1]
        
        if node == goal:
            return path  # Si encontramos el objetivo, retornamos el camino
        
        if node not in visited:
            visited.add(node)  # Marcamos como visitado
            for neighbor in graph.get(node, []):  # Exploramos los vecinos
                if neighbor not in visited:
                    new_path = path + [neighbor]  # Generamos un nuevo camino
                    heapq.heappush(frontier, (heuristic(neighbor, goal), new_path))  # Añadimos con prioridad heurística
    
    return None  # Si no encontramos un camino, retornamos None

# Función heurística de ejemplo (distancia de Manhattan)
def heuristic(node, goal):
    x1, y1 = node
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)

# Ejemplo de uso
graph = {
    (0, 0): [(1, 0), (0, 1)],
    (1, 0): [(2, 0)],
    (0, 1): [(1, 1)],
    (1, 1): [(2, 1)],
    (2, 0): [(2, 1), (3, 0)],
    (2, 1): [(3, 1)],
    (3, 0): [(3, 1)],
    (3, 1): []
}

start = (0, 0)
goal = (3, 1)
print("Camino encontrado por Búsqueda Voraz Primero el Mejor:", greedy_best_first_search(graph, start, goal, heuristic))
# Output esperado: Camino encontrado por Búsqueda Voraz Primero el Mejor: [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1)]