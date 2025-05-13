# Hechos conocidos
hechos = {"es_estudiante": True}

# Reglas por defecto
def es_mayor_de_edad(hechos):
    # Suponemos por defecto que un estudiante es mayor de edad
    if hechos.get("es_estudiante") and "es_menor" not in hechos:
        return True
    return False

print("¿Es mayor de edad por defecto?", es_mayor_de_edad(hechos))

# Se añade información que contradice el supuesto
hechos["es_menor"] = True

print("¿Es mayor de edad después de nueva evidencia?", es_mayor_de_edad(hechos))
