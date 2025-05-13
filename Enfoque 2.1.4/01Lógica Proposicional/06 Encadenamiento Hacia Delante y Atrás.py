# Encadenamiento hacia adelante: deducción basada en hechos
hechos = {"p", "q"}  # Hechos conocidos
reglas = [("p and q", "r")]  # Si p y q entonces r

# Aplicamos las reglas para deducir nuevos hechos
for antecedente, consecuente in reglas:
    if eval(antecedente, {}, {h: True for h in hechos}):
        hechos.add(consecuente)

print("Hechos después del encadenamiento hacia adelante:", hechos)
# La salida mostrará los hechos deducidos después de aplicar las reglas.
# En este caso, si p y q son verdaderos, se deduce que r también es verdadero.