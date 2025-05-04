import random

# Definimos una gramática probabilística
gramatica = {
    "S": [("NP", "VP", 1.0)],  # S -> NP VP
    "NP": [("Det", "Noun", 0.6), ("Pronoun", "", 0.4)],  # NP -> Det Noun | Pronoun
    "VP": [("Verb", "NP", 0.7), ("Verb", "", 0.3)],  # VP -> Verb NP | Verb
    "Det": [("el", 0.5), ("la", 0.5)],  # Det -> el | la
    "Noun": [("gato", 0.5), ("perro", 0.5)],  # Noun -> gato | perro
    "Verb": [("come", 0.5), ("duerme", 0.5)],  # Verb -> come | duerme
    "Pronoun": [("él", 1.0)]  # Pronoun -> él
}

# Función para generar una oración basada en la gramática probabilística
def generar_oracion(gramatica, simbolo="S"):
    if simbolo not in gramatica:
        return simbolo  # Si no está en la gramática, es una palabra terminal

    regla = random.choices(gramatica[simbolo], [r[1] for r in gramatica[simbolo]])[0]  # Elegir una regla
    return " ".join([generar_oracion(gramatica, simbolo=s) for s in regla if s])

# Generar una oración
oracion = generar_oracion(gramatica)
print("Oración generada:", oracion)
