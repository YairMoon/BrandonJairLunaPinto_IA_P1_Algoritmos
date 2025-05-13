# Simulación de lógica modal con funciones que representan mundos posibles

# Base de conocimiento con mundos posibles
mundos = {
    "m1": {"llueve": True, "nieve": False},
    "m2": {"llueve": True, "nieve": True},
    "m3": {"llueve": False, "nieve": False},
}

# Posibilidad: algo es posible si ocurre en al menos un mundo
def es_posible(prop):
    return any(m[prop] for m in mundos.values())

# Necesidad: algo es necesario si ocurre en todos los mundos
def es_necesario(prop):
    return all(m[prop] for m in mundos.values())

print("¿Es posible que llueva?", es_posible("llueve"))
print("¿Es necesario que nieve?", es_necesario("nieve"))
# Salida esperada:
# ¿Es posible que llueva? True