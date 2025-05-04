# Definimos una gramática probabilística lexicalizada
gramatica_lexicalizada = {
    "S": [("NP", "VP", 1.0)],
    "NP": [("Det", "Noun", 0.6), ("Pronoun", "", 0.4)],
    "VP": [("Verb", "NP", 0.7), ("Verb", "", 0.3)],
    "Det": [("el", 0.5), ("la", 0.5)],
    "Noun": [("gato", 0.5), ("perro", 0.5)],
    "Verb": [("come", 0.5), ("duerme", 0.5)],
    "Pronoun": [("él", 1.0)]
}

# Función para generar una oración basada en la gramática lexicalizada
def generar_oracion_lexicalizada(gramatica, simbolo="S"):
    if simbolo not in gramatica:
        return simbolo

    regla = random.choices(gramatica[simbolo], [r[1] for r in gramatica[simbolo]])[0]
    return " ".join([generar_oracion_lexicalizada(gramatica, simbolo=s) for s in regla if s])

# Generar una oración
oracion_lexicalizada = generar_oracion_lexicalizada(gramatica_lexicalizada)
print("Oración generada con gramática lexicalizada:", oracion_lexicalizada)
