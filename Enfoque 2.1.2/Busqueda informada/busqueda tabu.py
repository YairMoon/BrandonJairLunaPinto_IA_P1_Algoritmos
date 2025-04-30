import random

# Búsqueda Tabú (Tabu Search)
def tabu_search(problem, heuristic, max_iterations=100, tabu_size=5):
    """
    Implementa el algoritmo de búsqueda tabú.
    
    :param problem: Espacio del problema como un diccionario {nodo: [vecinos]}
    :param heuristic: Función heurística h(n)
    :param max_iterations: Número máximo de iteraciones
    :param tabu_size: Tamaño de la lista tabú
    :return: Mejor solución encontrada
    """
    current = random.choice(list(problem.keys()))  # Selección aleatoria de nodo inicial
    best_solution = current
    best_value = heuristic(current)
    tabu_list = []  # Lista tabú para evitar ciclos
    
    for _ in range(max_iterations):
        neighbors = problem.get(current, [])  # Obtener vecinos
        if not neighbors:
            break  # Si no hay vecinos, terminamos
        
        # Seleccionamos el mejor vecino que no esté en la lista tabú
        candidates = [n for n in neighbors if n not in tabu_list]
        if not candidates:
            break  # Si todos los vecinos están en tabú, terminamos
        
        next_node = max(candidates, key=heuristic)  # Seleccionamos el mejor vecino
        tabu_list.append(next_node)  # Agregamos a la lista tabú
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)  # Mantenemos el tamaño de la lista tabú
        
        if heuristic(next_node) > best_value:
            best_solution = next_node
            best_value = heuristic(next_node)
        
        current = next_node  # Movemos al mejor vecino
    
    return best_solution

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
best_solution = tabu_search(graph, heuristic)
print("Mejor solución encontrada por Búsqueda Tabú:", best_solution)
# Output esperado: Mejor solución encontrada por Búsqueda Tabú: D
# El resultado puede variar debido a la naturaleza aleatoria de la selección del nodo inicial
