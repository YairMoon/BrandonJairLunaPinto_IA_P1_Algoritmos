import random  # Importamos la librería random para manejar la selección aleatoria.

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
    current = random.choice(list(problem.keys()))  # Selección aleatoria de nodo inicial.
    best_solution = current  # Inicializamos la mejor solución como el nodo inicial.
    best_value = heuristic(current)  # Calculamos el valor heurístico del nodo inicial.
    tabu_list = []  # Lista tabú para evitar ciclos.

    for _ in range(max_iterations):  # Iteramos hasta el número máximo de iteraciones.
        neighbors = problem.get(current, [])  # Obtenemos los vecinos del nodo actual.
        if not neighbors:  # Si no hay vecinos, terminamos la búsqueda.
            break
        
        # Seleccionamos los vecinos que no están en la lista tabú.
        candidates = [n for n in neighbors if n not in tabu_list]
        if not candidates:  # Si todos los vecinos están en la lista tabú, terminamos.
            break
        
        next_node = max(candidates, key=heuristic)  # Seleccionamos el mejor vecino según la heurística.
        tabu_list.append(next_node)  # Agregamos el nodo seleccionado a la lista tabú.
        if len(tabu_list) > tabu_size:  # Si la lista tabú excede su tamaño máximo.
            tabu_list.pop(0)  # Eliminamos el nodo más antiguo de la lista tabú.
        
        # Si el nodo seleccionado tiene un mejor valor heurístico, actualizamos la mejor solución.
        if heuristic(next_node) > best_value:
            best_solution = next_node
            best_value = heuristic(next_node)
        
        current = next_node  # Movemos al mejor vecino seleccionado.

    return best_solution  # Retornamos la mejor solución encontrada.

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
best_solution = tabu_search(graph, heuristic)  # Ejecutamos el algoritmo de búsqueda tabú.
print("Mejor solución encontrada por Búsqueda Tabú:", best_solution)  # Mostramos la mejor solución encontrada.

# Output esperado: Mejor solución encontrada por Búsqueda Tabú: G
# El resultado puede variar debido a la naturaleza aleatoria de la selección del nodo inicial.