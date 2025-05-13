import random  # Importamos la librería random para manejar la selección aleatoria.

# Búsqueda de Ascensión de Colinas (Hill Climbing Search)
def hill_climbing(problem, heuristic):
    """
    Implementa el algoritmo de ascensión de colinas.
    
    :param problem: Espacio del problema representado como un diccionario {nodo: [vecinos]}
    :param heuristic: Función heurística h(n)
    :return: Mejor solución encontrada
    """
    current = random.choice(list(problem.keys()))  # Seleccionamos un nodo inicial aleatorio.
    while True:
        neighbors = problem.get(current, [])  # Obtenemos los vecinos del nodo actual.
        if not neighbors:  # Si no hay vecinos (nodo hoja).
            return current  # Retornamos el nodo actual como solución.

        # Seleccionamos el mejor vecino según la función heurística.
        best_neighbor = max(neighbors, key=heuristic)
        if heuristic(best_neighbor) <= heuristic(current):  # Si no hay mejora en la heurística.
            return current  # Retornamos el nodo actual como solución.
        current = best_neighbor  # Movemos al mejor vecino.

# Definimos el espacio del problema
graph = {
    'A': ['B', 'C'],  # Desde 'A', podemos ir a 'B' y 'C'.
    'B': ['D', 'E'],  # Desde 'B', podemos ir a 'D' y 'E'.
    'C': ['F'],       # Desde 'C', podemos ir a 'F'.
    'D': [],          # 'D' es un nodo hoja.
    'E': ['G'],       # Desde 'E', podemos ir a 'G'.
    'F': [],          # 'F' es un nodo hoja.
    'G': []           # 'G' es un nodo hoja.
}

# Definimos la función heurística
def heuristic(node):
    """
    Función heurística que asigna un valor a cada nodo.
    """
    values = {'A': 1, 'B': 3, 'C': 2, 'D': 0, 'E': 5, 'F': 1, 'G': 6}  # Valores heurísticos de los nodos.
    return values.get(node, 0)  # Retornamos el valor heurístico del nodo.

# Ejecutar la búsqueda
global_best = hill_climbing(graph, heuristic)  # Ejecutamos el algoritmo de ascensión de colinas.
print("Mejor solución encontrada por Ascensión de Colinas:", global_best)  # Mostramos la mejor solución encontrada.

# Output esperado: Mejor solución encontrada por Ascensión de Colinas: D
# El resultado puede variar debido a la naturaleza aleatoria de la selección del nodo inicial.