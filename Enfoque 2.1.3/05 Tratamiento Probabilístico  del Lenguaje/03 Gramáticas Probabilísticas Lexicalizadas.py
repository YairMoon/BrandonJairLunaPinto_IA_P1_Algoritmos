# Definimos una gramática probabilística lexicalizada
gramatica_lexicalizada = {
    "S": [("NP", "VP", 1.0)],  # S -> NP VP
    # La oración comienza con un sintagma nominal (NP) seguido de un sintagma verbal (VP).
    # Por ejemplo, "El gato come" o "Él duerme".
    "NP": [("Det", "Noun", 0.6), ("Pronoun", "", 0.4)],  # NP -> Det Noun | Pronoun
    # NP puede ser un determinante seguido de un sustantivo (60%) o un pronombre (40%).
    # Por ejemplo, "el gato" o "él".
    "VP": [("Verb", "NP", 0.7), ("Verb", "", 0.3)],  # VP -> Verb NP | Verb
    # VP puede ser un verbo seguido de un NP (70%) o solo un verbo (30%).
    # Por ejemplo, "come el gato" o "duerme".
    "Det": [("el", 0.5), ("la", 0.5)],  # Det -> el | la
    # Determinantes posibles: "el" o "la".
    # Por ejemplo, "el gato" o "la casa".
    "Noun": [("gato", 0.5), ("perro", 0.5)],  # Noun -> gato | perro
    # Sustantivos posibles: "gato" o "perro".
    # Por ejemplo, "el gato" o "la casa".
    "Verb": [("come", 0.5), ("duerme", 0.5)],  # Verb -> come | duerme
    # Verbos posibles: "come" o "duerme".
    # Por ejemplo, "el gato come" o "el perro duerme".
    "Pronoun": [("él", 1.0)]  # Pronoun -> él
    # Pronombre posible: "él".
    # Por ejemplo, "él come" o "él duerme".
}
# La gramática define reglas de producción con probabilidades asociadas.
# Por ejemplo:
# - "S" siempre se expande a "NP VP" con probabilidad 1.0.
# - "NP" puede ser "Det Noun" (60%) o "Pronoun" (40%).

# Función para generar una oración basada en la gramática lexicalizada
def generar_oracion_lexicalizada(gramatica, simbolo="S"): ## Definimos la función que generará una oración a partir de un símbolo inicial.
    """
    Genera una oración a partir de un símbolo inicial utilizando una gramática probabilística lexicalizada.

    :param gramatica: Diccionario que define las reglas de producción y sus probabilidades.
    :param simbolo: Símbolo inicial (por defecto "S").
    :return: Una oración generada como cadena de texto.
    """
    if simbolo not in gramatica: ## Verificamos si el símbolo no está en la gramática.
        # Si no está en la gramática, es una palabra terminal.
        return simbolo  # Si no está en la gramática, es una palabra terminal.

    # Seleccionar una regla de producción basada en las probabilidades
    regla = random.choices(gramatica[simbolo], [r[2] for r in gramatica[simbolo]])[0] 
    # `random.choices` selecciona una regla basada en las probabilidades definidas.

    # Generar recursivamente las partes de la regla
    return " ".join([generar_oracion_lexicalizada(gramatica, simbolo=s) for s in regla if s])
    # Para cada símbolo en la regla seleccionada, generamos recursivamente su expansión.

# Generar una oración
oracion_lexicalizada = generar_oracion_lexicalizada(gramatica_lexicalizada) 
# Llamamos a la función para generar una oración a partir del símbolo inicial "S".

print("Oración generada con gramática lexicalizada:", oracion_lexicalizada)
# Mostramos la oración generada.