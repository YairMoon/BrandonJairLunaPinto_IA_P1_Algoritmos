# Supongamos que tenemos las proposiciones:
p = True      # p: "Está lloviendo"
p_implica_q = True  # p → q: "Si llueve, el suelo está mojado"

# Aplicamos Modus Ponens
if p and p_implica_q:
    q = True  # Inferimos que q es verdadera
else:
    q = False

print("¿El suelo está mojado?", q)
# En este caso, si p es verdadero y p implica q, entonces q también es verdadero.
# Esto es un ejemplo de Modus Ponens, que es una regla de inferencia lógica.