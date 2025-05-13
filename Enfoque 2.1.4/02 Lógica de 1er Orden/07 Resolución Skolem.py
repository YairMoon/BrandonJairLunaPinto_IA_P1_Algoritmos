# Ejemplo simbólico de Skolemización

# Fórmula: ∀x ∃y ama(x, y)
# Se convierte en: ama(x, f(x)), donde f es una función de Skolem

def ama(x):
    return f"{x} ama a f({x})"

for persona in ["juan", "ana"]:
    print(ama(persona))
# La salida mostrará que cada persona ama a una función de Skolem que depende de ella misma.
# En este caso, "juan ama a f(juan)" y "ana ama a f(ana)".