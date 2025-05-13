# Importamos SymPy para lógica simbólica
from sympy import symbols
from sympy.logic.boolalg import to_cnf

# Definimos variables proposicionales
p, q = symbols('p q')

# Definimos una fórmula lógica
expresion = ~(p >> q)

# Convertimos la expresión a Forma Normal Conjuntiva (FNC)
fnc = to_cnf(expresion, simplify=True)

print("Fórmula en FNC:", fnc)
# La salida mostrará la fórmula en Forma Normal Conjuntiva (FNC).   
# En este caso, la expresión ~(p >> q) se convierte en una forma que es una conjunción de disyunciones.
# Esto es útil en lógica proposicional y en algoritmos de resolución, ya que la FNC es un formato estándar para trabajar con expresiones lógicas.