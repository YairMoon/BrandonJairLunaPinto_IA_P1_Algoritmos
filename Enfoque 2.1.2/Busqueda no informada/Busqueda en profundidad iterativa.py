# Búsqueda en Profundidad Iterativa (IDS - Iterative Deepening Search)
def iterative_deepening_search(graph, start, goal, max_depth):
    """
    Implementa el algoritmo de Búsqueda en Profundidad Iterativa.
    
    :param graph: Diccionario que representa el grafo {nodo: [vecinos]}
    :param start: Nodo inicial
    :param goal: Nodo objetivo
    :param max_depth: Profundidad máxima a alcanzar
    :return: Lista con el camino desde start hasta goal o None si no hay camino dentro del límite
    """
    def depth_limited_search(node, path, depth):
        if node == goal:
            return path  # Si encontramos el objetivo, retornamos el camino
        if depth == 0:
            return None  # Si alcanzamos el límite de profundidad, retornamos None
        
        for neighbor in graph.get(node, []):  # Exploramos los vecinos
            new_path = list(path)
            new_path.append(neighbor)
            result = depth_limited_search(neighbor, new_path, depth - 1)  # Llamada recursiva
            if result:
                return result
        
        return None  # Si no encontramos el objetivo, retornamos None
    
    for depth in range(max_depth + 1):  # Iteramos desde profundidad 0 hasta el máximo
        result = depth_limited_search(start, [start], depth)
        if result:
            return result  # Si encontramos una solución, la retornamos
    
    return None  # Si no encontramos ninguna solución, retornamos None

# Ejemplo de uso
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start = 'A'
goal = 'F'
max_depth = 3
print("Camino encontrado por IDS:", iterative_deepening_search(graph, start, goal, max_depth))
