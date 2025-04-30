# Red Bayesiana Dinámica - Modelo de influencia con pgmpy

from pgmpy.models import DynamicBayesianNetwork
from pgmpy.factors.discrete import DiscreteFactor, TabularCPD

def dynamic_bayesian_network_example():
    # Inicializamos el modelo
    model = DynamicBayesianNetwork()

    # Definimos los nodos y aristas para el modelo
    model.add_edges_from([(('X', 0), ('Y', 0)),
                          (('Y', 0), ('Z', 0)),
                          (('X', 1), ('Y', 1)),
                          (('Y', 1), ('Z', 1))])

    # Definimos las CPDs
    cpd_x = TabularCPD(('X', 0), 2, [[0.8], [0.2]])
    cpd_y_given_x = TabularCPD(('Y', 0), 2, [[0.9, 0.2], [0.1, 0.8]], evidence=[('X', 0)], evidence_card=[2])
    cpd_z_given_y = TabularCPD(('Z', 0), 2, [[0.7, 0.3], [0.4, 0.6]], evidence=[('Y', 0)], evidence_card=[2])

    # Añadimos las CPDs al modelo
    model.add_cpds(cpd_x, cpd_y_given_x, cpd_z_given_y)

    # Verificamos que el modelo es válido
    model.check_model()

    # Retornamos el modelo para su posterior uso
    return model


# ----------------------------
# Ejemplo de uso
# ----------------------------
if __name__ == "__main__":
    model = dynamic_bayesian_network_example()

    # Mostramos las CPDs
    for cpd in model.cpds:
        print(cpd)
