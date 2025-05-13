# Simulamos reglas tipo Prolog con estructuras de datos

# Base de hechos
padres = {
    "juan": "carlos",
    "ana": "carlos",
}

# Regla: X y Y son hermanos si tienen el mismo padre y no son la misma persona
def son_hermanos(x, y):
    return padres.get(x) == padres.get(y) and x != y

print("¿Juan y Ana son hermanos?", son_hermanos("juan", "ana"))
# La salida mostrará True si Juan y Ana son hermanos según la base de hechos.
# En este caso, la función devolverá True porque ambos tienen el mismo padre (Carlos) y son diferentes personas.