import heapq

# Definir el grafo: nodos y sus vecinos con distancia
graph = {}

# Interactivo: el usuario ingresa los nodos y conexiones
print("=== Grafo de rutas casa → escuela ===")
while True:
    nodo = input("Ingresa un nodo (o 'fin' para terminar): ")
    if nodo.lower() == 'fin':
        break
    graph[nodo] = {}
    while True:
        vecino = input(f"  Nodo vecino de {nodo} (o 'ok' para terminar): ")
        if vecino.lower() == 'ok':
            break
        peso = float(input(f"    Distancia de {nodo} a {vecino} (km): "))
        graph[nodo][vecino] = peso

# Función Dijkstra
def dijkstra(grafo, inicio, fin):
    # Cola de prioridad: (distancia acumulada, nodo actual, camino recorrido)
    queue = [(0, inicio, [inicio])]
    visited = set()  # Nodos visitados
    
    while queue:
        dist, nodo, path = heapq.heappop(queue)
        if nodo == fin:
            return dist, path
        if nodo in visited:
            continue
        visited.add(nodo)
        for vecino, peso in grafo[nodo].items():
            if vecino not in visited:
                # Se agrega vecino con nueva distancia y camino actualizado
                heapq.heappush(queue, (dist + peso, vecino, path + [vecino]))

# Solicitar nodo de inicio y fin
inicio = input("Nodo de inicio: ")
fin = input("Nodo destino: ")

distancia, ruta = dijkstra(graph, inicio, fin)
print(f"\nRuta óptima: {' → '.join(ruta)}")
print(f"Distancia total: {distancia} km")
# Ejemplo de uso:
# Ingresar nodos y conexiones:
# Nodo: Casa