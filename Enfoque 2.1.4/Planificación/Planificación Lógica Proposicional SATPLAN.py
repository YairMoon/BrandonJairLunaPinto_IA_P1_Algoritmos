# SATPLAN utiliza un enfoque lógico proposicional para generar planes
from pyswip import Prolog

# Creamos un motor Prolog para trabajar con lógica proposicional
prolog = Prolog()

# Definimos hechos y reglas en Prolog
prolog.assertz("en_casa")
prolog.assertz("libro_disponible")

# Definimos la acción "ir_a_biblioteca" en Prolog
prolog.assertz("ir_a_biblioteca :- en_casa")

# Planificación: Queremos que "tiene_libro" sea verdadero
prolog.assertz("tiene_libro :- ir_a_biblioteca, libro_disponible")

# Consultamos si podemos alcanzar el objetivo
consulta = list(prolog.query("tiene_libro"))
print("Planificación con SATPLAN:", consulta)
# # La salida mostrará si es posible alcanzar el objetivo "tiene_libro" a partir de los hechos y reglas definidas.
# # En este caso, si estamos en casa y el libro está disponible, podemos ir a la biblioteca y tener el libro.