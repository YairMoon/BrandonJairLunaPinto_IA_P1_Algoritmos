# Definimos una base de conocimiento como una lista de proposiciones verdaderas
base_conocimiento = ["llueve", "nublado", "mojado"]

# Función para consultar si una proposición está en la base
def consulta_base(proposicion):
    return proposicion in base_conocimiento

# Prueba de consulta
print("¿Está mojado?", consulta_base("mojado"))
print("¿Hace sol?", consulta_base("soleado"))
