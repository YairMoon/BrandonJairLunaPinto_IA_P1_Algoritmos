# Reglas IF-THEN en un sistema experto básico
def sistema_experto(temperatura):
    if temperatura > 38:
        return "Posible fiebre"
    elif temperatura < 35:
        return "Hipotermia"
    else:
        return "Temperatura normal"

# Evaluamos algunos casos
print(sistema_experto(39))  # Posible fiebre
print(sistema_experto(34))  # Hipotermia
