# Importamos el modelo de diagrama de influencia de la librería pgmpy
from pgmpy.models import InfluenceDiagram # Importamos la clase para diagramas de influencia

# Importamos los tipos de factores que usaremos: factores discretos y CPDs tabulares
from pgmpy.factors.discrete import DiscreteFactor, TabularCPD # Importamos la clase para definir CPDs tabulares

def decision_network_example():# Definimos una función para crear un modelo de red de decisión
    # Creamos un modelo de diagrama de influencia
    model = InfluenceDiagram()# Inicializamos el modelo de diagrama de influencia

    # Añadimos los nodos: "Clima" (variable aleatoria), "Salir" (decisión), "Utilidad" (nodo de utilidad)
    model.add_nodes_from(["Clima", "Salir", "Utilidad"])# Añadimos los nodos al modelo

    # Añadimos aristas: el clima y la decisión influyen en la utilidad
    model.add_edge("Clima", "Utilidad")# Añadimos una arista entre "Clima" y "Utilidad"
    model.add_edge("Salir", "Utilidad")# Añadimos una arista entre "Salir" y "Utilidad"

    # Definimos la distribución de probabilidad para el clima (70% bueno, 30% malo)
    cpd_clima = TabularCPD("Clima", 2, [[0.7], [0.3]])  # 2 estados: bueno (0), malo (1)
    model.add_cpds(cpd_clima)  # Añadimos la CPD al modelo

    # Definimos el nodo de utilidad como un DiscreteFactor sobre Clima y Salir
    utilidad = DiscreteFactor(
        variables=["Clima", "Salir"],  # Variables que afectan la utilidad
        cardinality=[2, 2],            # Cada una tiene 2 valores posibles (0 o 1)
        values=[
            [10, -5],   # Utilidad cuando el clima es bueno
            [-10, 0],   # Utilidad cuando el clima es malo
        ]
    )

    # Añadimos el nodo de utilidad al modelo
    model.add_factors(utilidad)

    # Verificamos que el modelo esté bien construido
    assert model.check_model()

    # Retornamos el modelo para su posterior uso o visualización
    return model


# ----------------------------
# Ejemplo de uso
# ----------------------------
if __name__ == "__main__":
    # Creamos el modelo de red de decisión
    model = decision_network_example()

    # Mostramos los nodos del modelo
    print("Nodos del modelo:", model.nodes())

    # Mostramos las aristas del modelo
    print("Aristas del modelo:", model.edges())

    # Mostramos las CPDs definidas en el modelo
    for cpd in model.cpds:
        print(cpd)

    # Mostramos los factores del modelo (incluyendo el nodo de utilidad)
    for factor in model.factors:# Iteramos sobre los factores del modelo
        print(factor)# Mostramos cada factor
    # Mostramos el número de nodos y aristas en el modelo