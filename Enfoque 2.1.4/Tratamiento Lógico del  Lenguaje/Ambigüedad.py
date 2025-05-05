# La ambigüedad se refiere a cuando una oración o expresión tiene más de un significado.
# Vamos a usar un ejemplo de ambigüedad en una oración: "Vimos a Juan en el parque."

def analizar_ambiguo(oracion):
    if "Vimos a Juan" in oracion:
        return "Puede significar que vimos a Juan o que Juan estaba viendo a nosotros."
    return "No es ambiguo."

# Ejemplo de uso
oracion = "Vimos a Juan en el parque"
print(analizar_ambiguo(oracion))  # Puede significar que vimos a Juan o que Juan estaba viendo a nosotros.
# Output:
# Puede significar que vimos a Juan o que Juan estaba viendo a nosotros.