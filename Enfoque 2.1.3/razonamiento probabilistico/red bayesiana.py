# Importamos las librerías necesarias
from pomegranate import BayesianNetwork

# Creamos una red bayesiana simple: lluvia → tráfico
# El nodo lluvia afecta si hay tráfico o no

# Definimos la estructura de la red y las probabilidades condicionales
model = BayesianNetwork("Ejemplo de Red Bayesiana")

# Añadimos nodos y sus distribuciones
from pomegranate import DiscreteDistribution, ConditionalProbabilityTable, State

# Nodo independiente: Lluvia
lluvia = DiscreteDistribution({
    "sí": 0.3,
    "no": 0.7
})

# Nodo dependiente: Tráfico (depende de si llueve o no)
trafico = ConditionalProbabilityTable([
    ["sí", "sí", 0.8],  # Si llueve, hay 80% de probabilidad de tráfico
    ["sí", "no", 0.2],  # Si llueve, 20% de no haber tráfico
    ["no", "sí", 0.2],  # Si no llueve, 20% de tráfico
    ["no", "no", 0.8],  # Si no llueve, 80% de no tráfico
], [lluvia])

# Creamos los estados (nodos en la red)
s_lluvia = State(lluvia, name="lluvia")
s_trafico = State(trafico, name="trafico")

# Añadimos los estados al modelo
model.add_states(s_lluvia, s_trafico)
model.add_edge(s_lluvia, s_trafico)  # Lluvia → Tráfico

# Finalizamos la construcción de la red
model.bake()

# Realizamos una inferencia: ¿Cuál es la probabilidad de tráfico si no llueve?
beliefs = model.predict_proba({"lluvia": "no"})

# Mostramos resultados
for state, belief in zip(model.states, beliefs):
    print(f"Probabilidades de '{state.name}': {belief}")
