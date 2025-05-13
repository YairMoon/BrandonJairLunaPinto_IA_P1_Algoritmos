# Agente lógico simple basado en reglas

# Mundo del agente
percepciones = {"pared adelante"}

# Reglas
def decide(percepciones):
    if "pared adelante" in percepciones:
        return "girar a la derecha"
    else:
        return "avanzar"

print("Acción del agente:", decide(percepciones))
# La salida mostrará la acción del agente basada en sus percepciones.   