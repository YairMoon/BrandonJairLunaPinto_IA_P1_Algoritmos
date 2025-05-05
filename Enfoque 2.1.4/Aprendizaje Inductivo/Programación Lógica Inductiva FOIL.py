# FOIL (First Order Inductive Logic Programming) es un enfoque para aprender reglas lógicas
# Simple simulación de FOIL con un conjunto de hechos y reglas

# Definimos un conjunto de hechos (datos)
hechos = [
    {"tiene_pelo": True, "es_mujer": True, "es_madre": False},
    {"tiene_pelo": True, "es_mujer": False, "es_madre": True},
    {"tiene_pelo": False, "es_mujer": True, "es_madre": True}
]

# Reglas de inferencia basadas en hechos
def foil(hechos):
    reglas = []
    for hecho in hechos:
        if hecho["tiene_pelo"] and hecho["es_mujer"]:
            reglas.append("Si tiene_pelo y es_mujer entonces es madre.")
    return reglas

# Generamos las reglas con FOIL
reglas_aprendidas = foil(hechos)
print("Reglas FOIL aprendidas:", reglas_aprendidas)
