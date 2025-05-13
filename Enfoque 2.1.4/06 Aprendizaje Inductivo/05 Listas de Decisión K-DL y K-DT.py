# Ejemplo simple de K-DL (K-Decision List)
# Definimos reglas de decisión
def k_dl(features):
    if features[0] == 1 and features[1] == 0:
        return "Clase A"
    elif features[0] == 0 and features[1] == 1:
        return "Clase B"
    else:
        return "Clase C"

# Probamos las reglas de decisión
print(k_dl([1, 0]))  # Clase A
print(k_dl([0, 1]))  # Clase B
print(k_dl([0, 0]))  # Clase C
