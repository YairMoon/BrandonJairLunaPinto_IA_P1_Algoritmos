# Probabilidad a Priori
# La probabilidad a priori es el conocimiento inicial sobre un evento antes de considerar nueva evidencia

# Ejemplo: un dado cargado (no justo)
# La probabilidad a priori para cada cara es desigual y refleja nuestro conocimiento inicial
probabilidades_priori = {
    1: 0.05,
    2: 0.10,
    3: 0.15,
    4: 0.20,
    5: 0.25,
    6: 0.25
}

# Función para verificar validez de la distribución
def es_distribucion_valida(distribucion):
    return abs(sum(distribucion.values()) - 1.0) < 1e-6

# Mostrar probabilidades a priori
print("Probabilidad a Priori para cada cara del dado cargado:")
for cara, prob in probabilidades_priori.items():
    print("  Cara {cara}: {prob}")

# Validar la distribución
print("\n¿Es una distribución válida?", es_distribucion_valida(probabilidades_priori))
# La suma de las probabilidades debe ser 1 (o muy cercana por redondeo)