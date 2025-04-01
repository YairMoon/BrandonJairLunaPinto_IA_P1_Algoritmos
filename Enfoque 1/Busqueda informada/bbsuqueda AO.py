class AOStar:
    """
    Implementa el algoritmo AO* para búsqueda en grafos.
    """
    def __init__(self, graph, heuristic):
        self.graph = graph  # Grafo con nodos y conexiones
        self.heuristic = heuristic  # Función heurística
        self.solved = {}  # Diccionario para almacenar costos solucionados

    def ao_star(self, node):
        """
        Realiza la búsqueda AO* a partir de un nodo dado.
        :param node: Nodo inicial
        :return: Mejor costo encontrado
        """
        if node not in self.graph:
            return self.heuristic(node)  # Si no tiene hijos, devolvemos h(n)
        
        min_cost = float("inf")  # Inicializamos con infinito
        best_path = None  # Inicializamos sin mejor camino
        
        for sub_nodes, cost in self.graph[node]:
            total_cost = cost + sum(self.ao_star(n) for n in sub_nodes)
            if total_cost < min_cost:
                min_cost = total_cost
                best_path = sub_nodes
        
        self.solved[node] = (min_cost, best_path)  # Guardamos el mejor resultado
        return min_cost

    def get_solution(self, start):
        """
        Obtiene la mejor solución desde el nodo inicial.
        :param start: Nodo inicial
        :return: Camino óptimo encontrado
        """
        if start not in self.solved:
            return None
        
        path = [start]
        while path[-1] in self.solved:
            _, next_nodes = self.solved[path[-1]]
            if not next_nodes:
                break
            path.append(next_nodes[0])  # Elegimos el primer nodo del mejor camino
        return path

# Definición del grafo con costos (AO*)
graph = {
    'A': [(['B', 'C'], 1)],
    'B': [(['D', 'E'], 2)],
    'C': [(['F'], 3)],
    'D': [],
    'E': [(['G'], 4)],
    'F': [],
    'G': []
}

# Función heurística (h(n))
def heuristic(node):
    return {'A': 6, 'B': 4, 'C': 2, 'D': 0, 'E': 1, 'F': 0, 'G': 0}.get(node, 0)

# Ejecutar AO*
ao_star_solver = AOStar(graph, heuristic)
ao_star_solver.ao_star('A')
print("Solución encontrada por AO*:", ao_star_solver.get_solution('A'))
