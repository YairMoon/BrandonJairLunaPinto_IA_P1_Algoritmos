# Encadenamiento hacia adelante: aplicar reglas si los hechos lo permiten
hechos = {"llueve"}

reglas = [
    ({"llueve"}, "el suelo está mojado"),
    ({"el suelo está mojado"}, "la calle está resbalosa"),
]

inferencias = set()

for premisas, conclusion in reglas:
    if premisas.issubset(hechos):
        inferencias.add(conclusion)

print("Inferencias hacia adelante:", inferencias)

# Encadenamiento hacia atrás: comprobar si un objetivo puede derivarse
objetivo = "la calle está resbalosa"
hechos = {"llueve", "el suelo está mojado"}

def puede_probar(obj, reglas, hechos):
    if obj in hechos:
        return True
    for premisas, conclusion in reglas:
        if conclusion == obj and premisas.issubset(hechos):
            return True
    return False

print("¿Se puede probar que la calle está resbalosa?", puede_probar(objetivo, reglas, hechos))
# La salida mostrará si el objetivo puede ser probado a partir de los hechos y reglas dadas.
# En este caso, "la calle está resbalosa" puede ser probado si "el suelo está mojado" es verdadero.