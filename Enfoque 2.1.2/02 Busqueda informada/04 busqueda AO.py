class AOStar: # AO* Search Algorithm
    """
    Implementa el algoritmo AO* para búsqueda en grafos.
    """
    def __init__(self, graph, heuristic):
        # Inicializamos el grafo y la función heurística.
        self.graph = graph  # Grafo con nodos y conexiones.
        self.heuristic = heuristic  # Función heurística que estima el costo desde un nodo.
        self.solved = {}  # Diccionario para almacenar costos solucionados.

    def ao_star(self, node): 
        """
        Realiza la búsqueda AO* a partir de un nodo dado.
        :param node: Nodo inicial.
        :return: Mejor costo encontrado.
        """
        if node not in self.graph:  # Si el nodo no tiene hijos (es una hoja).
            return self.heuristic(node)  # Retornamos el valor heurístico del nodo.

        min_cost = float("inf")  # Inicializamos el costo mínimo con infinito.
        best_path = None  # Inicializamos el mejor camino como None.

        # Iteramos sobre las conexiones del nodo actual.
        for sub_nodes, cost in self.graph[node]:
            # Calculamos el costo total como el costo directo más el costo de los subnodos.
            total_cost = cost + sum(self.ao_star(n) for n in sub_nodes)
            if total_cost < min_cost:  # Si encontramos un costo menor.
                min_cost = total_cost  # Actualizamos el costo mínimo.
                best_path = sub_nodes  # Actualizamos el mejor camino.

        # Guardamos el mejor costo y camino en el diccionario de soluciones.
        self.solved[node] = (min_cost, best_path)
        return min_cost  # Retornamos el costo mínimo encontrado.

    def get_solution(self, start):
        """
        Obtiene la mejor solución desde el nodo inicial.
        :param start: Nodo inicial.
        :return: Camino óptimo encontrado.
        """
        if start not in self.solved:  # Si el nodo inicial no tiene solución calculada.
            return None

        path = [start]  # Inicializamos el camino con el nodo inicial.
        while path[-1] in self.solved:  # Mientras el último nodo tenga solución.
            _, next_nodes = self.solved[path[-1]]  # Obtenemos el mejor camino desde el nodo actual.
            if not next_nodes:  # Si no hay más nodos en el camino, terminamos.
                break
            path.append(next_nodes[0])  # Agregamos el primer nodo del mejor camino.
        return path  # Retornamos el camino óptimo.

# Definición del grafo con costos (AO*)
graph = {
    'A': [(['B', 'C'], 1)],  # Desde 'A', podemos ir a ['B', 'C'] con un costo de 1.
    'B': [(['D', 'E'], 2)],  # Desde 'B', podemos ir a ['D', 'E'] con un costo de 2.
    'C': [(['F'], 3)],       # Desde 'C', podemos ir a ['F'] con un costo de 3.
    'D': [],                 # 'D' es un nodo hoja.
    'E': [(['G'], 4)],       # Desde 'E', podemos ir a ['G'] con un costo de 4.
    'F': [],                 # 'F' es un nodo hoja.
    'G': []                  # 'G' es un nodo hoja.
}

# Función heurística (h(n))
def heuristic(node):
    """
    Función heurística que asigna un costo estimado a cada nodo.
    """
    return {'A': 6, 'B': 4, 'C': 2, 'D': 0, 'E': 1, 'F': 0, 'G': 0}.get(node, 0)

# Ejecutar AO*
ao_star_solver = AOStar(graph, heuristic)  # Creamos una instancia del algoritmo AO*.
ao_star_solver.ao_star('A')  # Ejecutamos la búsqueda desde el nodo 'A'.
print("Solución encontrada por AO*:", ao_star_solver.get_solution('A'))  # Mostramos la solución óptima.











