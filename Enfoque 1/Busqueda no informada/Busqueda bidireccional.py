from collections import deque

# Búsqueda Bidireccional
def bidirectional_search(graph, start, goal):
    """
    Implementa el algoritmo de Búsqueda Bidireccional.
    
    :param graph: Diccionario que representa el grafo {nodo: [vecinos]}
    :param start: Nodo inicial
    :param goal: Nodo objetivo
    :return: Lista con el camino encontrado o None si no hay camino
    """
    if start == goal:
        return [start]  # Si el inicio es igual al objetivo, retornamos directamente
    
    forward_queue = deque([[start]])  # Cola para la búsqueda desde el inicio
    backward_queue = deque([[goal]])  # Cola para la búsqueda desde el objetivo
    forward_visited = {start}  # Nodos visitados desde el inicio
    backward_visited = {goal}  # Nodos visitados desde el objetivo
    
    while forward_queue and backward_queue:
        # Expansión desde el inicio
        forward_path = forward_queue.popleft()
        forward_node = forward_path[-1]
        
        if forward_node in backward_visited:
            return forward_path + backward_queue[backward_visited[forward_node]][::-1]
        
        for neighbor in graph.get(forward_node, []):
            if neighbor not in forward_visited:
                forward_visited.add(neighbor)
                forward_queue.append(forward_path + [neighbor])
        
        # Expansión desde el objetivo
        backward_path = backward_queue.popleft()
        backward_node = backward_path[-1]
        
        if backward_node in forward_visited:
            return forward_queue[forward_visited[backward_node]] + backward_path[::-1]
        
        for neighbor in graph.get(backward_node, []):
            if neighbor not in backward_visited:
                backward_visited.add(neighbor)
                backward_queue.append(backward_path + [neighbor])
    
    return None  # Si no encontramos un camino, retornamos None

# Ejemplo de uso
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start = 'A'
goal = 'F'
print("Camino encontrado por Búsqueda Bidireccional:", bidirectional_search(graph, start, goal))
