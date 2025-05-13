# Simulación de la Regla de la Cadena con 3 eventos: A, B y C

# Supongamos:
# P(A) = 0.6
# P(B|A) = 0.7, P(B|¬A) = 0.2
# P(C|A,B) = 0.9, P(C|A,¬B) = 0.5, P(C|¬A,B) = 0.6, P(C|¬A,¬B) = 0.1

# Evento A
P_A = 0.6
# Probabilidad marginal de que ocurra el evento A.

# Evento B condicionado a A
P_B_dado_A = 0.7  # Probabilidad de B dado que A ocurre.
P_B_dado_noA = 0.2  # Probabilidad de B dado que A no ocurre.

# Evento C condicionado a A y B
P_C_dado_A_B = 0.9  # Probabilidad de C dado que A y B ocurren.
P_C_dado_A_noB = 0.5  # Probabilidad de C dado que A ocurre y B no ocurre.
P_C_dado_noA_B = 0.6  # Probabilidad de C dado que A no ocurre y B ocurre.
P_C_dado_noA_noB = 0.1  # Probabilidad de C dado que ni A ni B ocurren.

# Calculamos la probabilidad conjunta usando la regla de la cadena
# P(A, B, C) = P(C|A,B) * P(B|A) * P(A)

P_A_B_C = P_C_dado_A_B * P_B_dado_A * P_A
# Multiplicamos las probabilidades condicionales siguiendo la regla de la cadena.

print(f"P(A ∧ B ∧ C) = {P_A_B_C:.4f}")
# Mostramos la probabilidad conjunta de A, B y C.