import math

# Calculamos la ganancia de información (Information Gain)
def ganancia_informacion(dato, atributo):
    # Total de ejemplos
    total = len(dato)
    
    # Valores únicos del atributo
    valores = set([ejemplo[atributo] for ejemplo in dato])
    
    # Entropía antes de dividir
    entropia_inicial = -sum([(len([x for x in dato if x[atributo] == v]) / total) * 
                             math.log2(len([x for x in dato if x[atributo] == v]) / total) 
                             for v in valores])
    
    # Dividimos el dato por cada valor del atributo y calculamos la entropía
    entropia_dividida = sum([(len([x for x in dato if x[atributo] == v]) / total) * 
                             -sum([(len([x for x in dato if x[atributo] == v and x[atributo2] == v2]) / 
                                    len([x for x in dato if x[atributo] == v])) * 
                                    math.log2(len([x for x in dato if x[atributo] == v and x[atributo2] == v2]) / 
                                              len([x for x in dato if x[atributo] == v])) 
                                    for v2 in set([x[atributo2] for x in dato if x[atributo] == v])]) 
                             for v in valores])
    
    return entropia_inicial - entropia_dividida


# Ejemplo de uso
datos = [{"atributo1": "valor1", "atributo2": "valor2", "clase": "A"},
         {"atributo1": "valor1", "atributo2": "valor3", "clase": "B"},
         {"atributo1": "valor2", "atributo2": "valor2", "clase": "A"}]

# Calculamos la ganancia de información
ganancia = ganancia_informacion(datos, "atributo1")
print("Ganancia de Información:", ganancia)
