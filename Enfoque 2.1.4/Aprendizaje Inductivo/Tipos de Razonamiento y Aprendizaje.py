# Tipos de razonamiento: Deductivo, Inductivo y Abductivo

# Razonamiento deductivo: Parte de una premisa general para llegar a una conclusión específica
def razonamiento_deductivo(premisa, conclusion):
    if premisa:
        return f"Conclusión deducida: {conclusion}"
    else:
        return "No es posible deducir la conclusión."

# Razonamiento inductivo: Observamos casos específicos para llegar a una conclusión general
def razonamiento_inductivo(casos):
    generalizacion = "Puede que todos los casos observados sigan un patrón."
    return f"Generalización inductiva: {generalizacion}"

# Razonamiento abductivo: Dada una observación, encontrar la explicación más plausible
def razonamiento_abductivo(observacion):
    explicacion = "Es probable que la observación sea causada por un factor X."
    return f"Explicación abductiva: {explicacion}"

# Ejemplo de uso
print(razonamiento_deductivo(True, "El sol es una estrella"))
print(razonamiento_inductivo(["Caso1", "Caso2"]))
print(razonamiento_abductivo("El cielo está nublado"))
