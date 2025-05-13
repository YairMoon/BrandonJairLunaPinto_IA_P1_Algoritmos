# Red Bayesiana Dinámica - Modelo de influencia con pgmpy

from pgmpy.models import DynamicBayesianNetwork  # Importamos la clase para redes bayesianas dinámicas
from pgmpy.factors.discrete import TabularCPD  # Importamos TabularCPD para definir distribuciones condicionales

def dynamic_bayesian_network_example(): # Definimos una función para crear un modelo de red bayesiana dinámica
    # Inicializamos el modelo
    model = DynamicBayesianNetwork() # Inicializamos el modelo de red bayesiana dinámica

    # Definimos los nodos y aristas para el modelo
    model.add_edges_from([(('X', 0), ('Y', 0)),  # Relación entre X y Y en el tiempo 0
                          (('Y', 0), ('Z', 0)),  # Relación entre Y y Z en el tiempo 0
                          (('X', 1), ('Y', 1)),  # Relación entre X y Y en el tiempo 1
                          (('Y', 1), ('Z', 1))])  # Relación entre Y y Z en el tiempo 1

    # Definimos las CPDs (Distribuciones Condicionales Probabilísticas)
    cpd_x = TabularCPD(('X', 0), 2, [[0.8], [0.2]])  # Probabilidad inicial de X en el tiempo 0
    cpd_y_given_x = TabularCPD(('Y', 0), 2,  # Probabilidad de Y dado X en el tiempo 0
                                [[0.9, 0.2],  # P(Y=0 | X=0) y P(Y=0 | X=1)
                                 [0.1, 0.8]],  # P(Y=1 | X=0) y P(Y=1 | X=1)
                                evidence=[('X', 0)], evidence_card=[2])  # Evidencia: X en el tiempo 0
    cpd_z_given_y = TabularCPD(('Z', 0), 2,  # Probabilidad de Z dado Y en el tiempo 0
                                [[0.7, 0.3],  # P(Z=0 | Y=0) y P(Z=0 | Y=1)
                                 [0.4, 0.6]],  # P(Z=1 | Y=0) y P(Z=1 | Y=1)
                                evidence=[('Y', 0)], evidence_card=[2])  # Evidencia: Y en el tiempo 0

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
    # Creamos el modelo de red bayesiana dinámica
    model = dynamic_bayesian_network_example()

    # Mostramos las CPDs definidas en el modelo
    for cpd in model.cpds:
        print(cpd)