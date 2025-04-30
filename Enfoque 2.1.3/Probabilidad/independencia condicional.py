# Independencia Condicional
# Dos eventos A y B son condicionalmente independientes dado C si:
# P(A ∩ B | C) = P(A | C) * P(B | C)

# Ejemplo: Diagnóstico médico
# A = dolor de cabeza
# B = fiebre
# C = infección

# Probabilidades conocidas:
P_A_dado_C = 0.7    # P(Dolor de cabeza | Infección)
P_B_dado_C = 0.8    # P(Fiebre | Infección)
P_AyB_dado_C = 0.56 # P(Dolor de cabeza y Fiebre | Infección)

# Verificamos independencia condicional:
producto = P_A_dado_C * P_B_dado_C
es_independiente = abs(P_AyB_dado_C - producto) < 1e-6

# Mostrar resultados con formato claro
print("Verificación de Independencia Condicional")
print("----------------------------------------")
print(f"P(Dolor de cabeza y Fiebre | Infección) = {P_AyB_dado_C:.4f}")
print(f"P(Dolor de cabeza | Infección) * P(Fiebre | Infección) = {producto:.4f}")
print(f"¿Son independientes dado infección? {'SÍ' if es_independiente else 'NO'}")
print("----------------------------------------")
