from collections import deque  # Importamos deque para manejar colas de manera eficiente.

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
    forward_visited = {start: [start]}  # Diccionario para registrar los caminos visitados desde el inicio
    backward_visited = {goal: [goal]}  # Diccionario para registrar los caminos visitados desde el objetivo

    while forward_queue and backward_queue:  # Mientras ambas colas tengan elementos.
        # Expansión desde el inicio
        forward_path = forward_queue.popleft()  # Extraemos el primer camino de la cola.
        forward_node = forward_path[-1]  # Último nodo del camino actual.

        if forward_node in backward_visited:  # Si el nodo está en la búsqueda inversa.
            return forward_path + backward_visited[forward_node][::-1][1:]  # Unimos los caminos.

        for neighbor in graph.get(forward_node, []):  # Exploramos los vecinos del nodo actual.
            if neighbor not in forward_visited:  # Si el vecino no ha sido visitado.
                forward_visited[neighbor] = forward_path + [neighbor]  # Registramos el camino.
                forward_queue.append(forward_path + [neighbor])  # Añadimos el nuevo camino a la cola.

        # Expansión desde el objetivo
        backward_path = backward_queue.popleft()  # Extraemos el primer camino de la cola inversa.
        backward_node = backward_path[-1]  # Último nodo del camino actual.

        if backward_node in forward_visited:  # Si el nodo está en la búsqueda directa.
            return forward_visited[backward_node] + backward_path[::-1][1:]  # Unimos los caminos.

        for neighbor in graph.get(backward_node, []):  # Exploramos los vecinos del nodo actual.
            if neighbor not in backward_visited:  # Si el vecino no ha sido visitado.
                backward_visited[neighbor] = backward_path + [neighbor]  # Registramos el camino.
                backward_queue.append(backward_path + [neighbor])  # Añadimos el nuevo camino a la cola.

    return None  # Si no encontramos un camino, retornamos None.

# Ejemplo de uso
graph = {
    'A': ['B', 'C'],  # Desde 'A', podemos ir a 'B' y 'C'.
    'B': ['A', 'D', 'E'],  # Desde 'B', podemos ir a 'A', 'D' y 'E'.
    'C': ['A', 'F'],  # Desde 'C', podemos ir a 'A' y 'F'.
    'D': ['B'],  # Desde 'D', podemos ir a 'B'.
    'E': ['B', 'F'],  # Desde 'E', podemos ir a 'B' y 'F'.
    'F': ['C', 'E']  # Desde 'F', podemos ir a 'C' y 'E'.
}

start = 'A'  # Nodo inicial.
goal = 'F'  # Nodo objetivo.
print("Camino encontrado por Búsqueda Bidireccional:", bidirectional_search(graph, start, goal))
# Output esperado: Camino encontrado por Búsqueda Bidireccional: ['A', 'C', 'F']