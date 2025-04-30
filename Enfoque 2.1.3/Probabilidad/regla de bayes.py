# Regla de Bayes
# P(A | B) = [P(B | A) * P(A)] / P(B)

# Ejemplo clásico: test médico
# A = tener la enfermedad
# B = resultado positivo del test

# Probabilidades conocidas:
P_A = 0.01         # P(A): probabilidad de tener la enfermedad (1%)
P_B_dado_A = 0.9   # P(B | A): test da positivo si la persona tiene la enfermedad
P_B_dado_noA = 0.2 # P(B | no A): test da falso positivo (20%)

# Usamos la ley total para calcular P(B):
P_noA = 1 - P_A
P_B = P_B_dado_A * P_A + P_B_dado_noA * P_noA

# Aplicamos la regla de Bayes para calcular P(A | B)
P_A_dado_B = (P_B_dado_A * P_A) / P_B

# Mostrar resultados
print("Regla de Bayes aplicada a un test médico:")
print(f"P(A): {P_A}")
print(f"P(B | A): {P_B_dado_A}")
print(f"P(B | no A): {P_B_dado_noA}")
print(f"P(B): {P_B:.4f}")
print(f"P(A | B): {P_A_dado_B:.4f} => Probabilidad de tener la enfermedad si el test es positivo")
