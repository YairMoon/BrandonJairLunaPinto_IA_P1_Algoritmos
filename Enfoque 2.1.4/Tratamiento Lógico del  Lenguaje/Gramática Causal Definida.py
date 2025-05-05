# La gramática causal define relaciones entre eventos, por ejemplo: "Si A ocurre, entonces B sucede."
# Simularemos un ejemplo simple de gramática causal en la que los eventos están relacionados.

def gramatica_causal(evento):
    reglas_causales = {
        "lluvia": "El suelo se moja.",
        "viento": "Las hojas caen."
    }
    if evento in reglas_causales:
        return reglas_causales[evento]
    else:
        return "No se conoce la causa."

# Ejemplo de uso
evento1 = "lluvia"
evento2 = "calor"
print(gramatica_causal(evento1))  # El suelo se moja.
print(gramatica_causal(evento2))  # No se conoce la causa.
# Output:
# El suelo se moja.