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
        """
        Función recursiva para realizar la búsqueda en profundidad limitada.
        
        :param node: Nodo actual
        :param path: Camino actual
        :param depth: Profundidad restante
        :return: Camino encontrado o None si no se encuentra solución
        """
        if node == goal:
            return path  # Si encontramos el objetivo, retornamos el camino
        if depth == 0:
            return None  # Si alcanzamos el límite de profundidad, retornamos None
        
        for neighbor in graph.get(node, []):  # Exploramos los vecinos
            new_path = list(path)  # Copiamos el camino actual
            new_path.append(neighbor)  # Agregamos el vecino al camino
            result = dls(neighbor, new_path, depth - 1)  # Llamada recursiva con menor profundidad
            if result:
                return result  # Si encontramos una solución, la retornamos
        
        return None  # Si no encontramos el objetivo, retornamos None
    
    return dls(start, [start], limit)  # Iniciamos la búsqueda desde el nodo inicial

# Ejemplo de uso
graph = {
    'A': ['B', 'C'],  # Desde 'A', podemos ir a 'B' y 'C'.
    'B': ['D', 'E'],  # Desde 'B', podemos ir a 'D' y 'E'.
    'C': ['F'],       # Desde 'C', podemos ir a 'F'.
    'D': [],          # 'D' es un nodo hoja.
    'E': ['F'],       # Desde 'E', podemos ir a 'F'.
    'F': []           # 'F' es un nodo hoja.
}

start = 'A'  # Nodo inicial.
goal = 'F'  # Nodo objetivo.
limit = 2  # Profundidad máxima permitida.
print("Camino encontrado por DLS:", depth_limited_search(graph, start, goal, limit))
# Output esperado: Camino encontrado por DLS: None (porque el objetivo está fuera del límite de profundidad)