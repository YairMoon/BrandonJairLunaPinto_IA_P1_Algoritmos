# Búsqueda en Profundidad Limitada (DLS - Depth-Limited Search)
def depth_limited_search(graph, start, goal, limit):
    """
    Implementa el algoritmo de Búsqueda en Profundidad con un límite de profundidad.
    
    :param graph: Diccionario que representa el grafo {nodo: [vecinos]}
    :param start: Nodo inicial
    :param goal: Nodo objetivo
    :param limit: Profundidad máxima permitida
    :return: Lista con el camino desde start hasta goal o None si no hay camino dentro del límite
    """
    def dls(node, path, depth):
        if node == goal:
            return path  # Si encontramos el objetivo, retornamos el camino
        if depth == 0:
            return None  # Si alcanzamos el límite de profundidad, retornamos None
        
        for neighbor in graph.get(node, []):  # Exploramos los vecinos
            new_path = list(path)
            new_path.append(neighbor)
            result = dls(neighbor, new_path, depth - 1)  # Llamada recursiva con menor profundidad
            if result:
                return result
        
        return None  # Si no encontramos el objetivo, retornamos None
    
    return dls(start, [start], limit)

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
limit = 2
print("Camino encontrado por DLS:", depth_limited_search(graph, start, goal, limit))
