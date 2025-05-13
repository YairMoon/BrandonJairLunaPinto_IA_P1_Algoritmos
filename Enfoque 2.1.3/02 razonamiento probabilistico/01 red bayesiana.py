# Importamos las librerías necesarias
from pomegranate import BayesianNetwork
# Importamos la clase BayesianNetwork para construir la red bayesiana.

# Creamos una red bayesiana simple: lluvia → tráfico
# El nodo lluvia afecta si hay tráfico o no

# Definimos la estructura de la red y las probabilidades condicionales
model = BayesianNetwork("Ejemplo de Red Bayesiana")
# Creamos un modelo de red bayesiana con el nombre "Ejemplo de Red Bayesiana".

# Añadimos nodos y sus distribuciones
from pomegranate import DiscreteDistribution, ConditionalProbabilityTable, State
# Importamos las clases necesarias para definir distribuciones y estados.

# Nodo independiente: Lluvia
lluvia = DiscreteDistribution({
    "sí": 0.3,  # Probabilidad de que llueva.
    "no": 0.7   # Probabilidad de que no llueva.
})

# Nodo dependiente: Tráfico (depende de si llueve o no)
trafico = ConditionalProbabilityTable([
    ["sí", "sí", 0.8],  # Si llueve, hay 80% de probabilidad de tráfico.
    ["sí", "no", 0.2],  # Si llueve, 20% de no haber tráfico.
    ["no", "sí", 0.2],  # Si no llueve, 20% de tráfico.
    ["no", "no", 0.8],  # Si no llueve, 80% de no tráfico.
], [lluvia])
# Definimos la probabilidad condicional de tráfico dado si llueve o no.

# Creamos los estados (nodos en la red)
s_lluvia = State(lluvia, name="lluvia")
s_trafico = State(trafico, name="trafico")
# Creamos los nodos de la red bayesiana con sus respectivas distribuciones.

# Añadimos los estados al modelo
model.add_states(s_lluvia, s_trafico)
# Añadimos los nodos "lluvia" y "tráfico" al modelo.

model.add_edge(s_lluvia, s_trafico)  # Lluvia → Tráfico
# Añadimos una relación entre los nodos: "lluvia" afecta a "tráfico".

# Finalizamos la construcción de la red
model.bake()
# Finalizamos la configuración del modelo para que esté listo para realizar inferencias.

# Realizamos una inferencia: ¿Cuál es la probabilidad de tráfico si no llueve?
beliefs = model.predict_proba({"lluvia": "no"})
# Calculamos las probabilidades condicionales dado que sabemos que no llueve.

# Mostramos resultados
for state, belief in zip(model.states, beliefs):
    print(f"Probabilidades de '{state.name}': {belief}")
# Iteramos sobre los nodos y mostramos las probabilidades calculadas para cada uno.