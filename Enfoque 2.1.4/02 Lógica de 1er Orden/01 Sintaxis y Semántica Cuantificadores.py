# Este ejemplo ilustra el uso de cuantificadores en lógica de primer orden con Python

# Definimos un conjunto de personas
personas = ["Ana", "Juan", "Luis"]

# Creamos una función que representa una propiedad: ser estudiante
def es_estudiante(nombre):
    return nombre in ["Ana", "Luis"]

# Cuantificador existencial: ¿existe alguien que sea estudiante?
existe_estudiante = any(es_estudiante(p) for p in personas)
print("¿Existe al menos un estudiante?:", existe_estudiante)

# Cuantificador universal: ¿todos son estudiantes?
todos_estudiantes = all(es_estudiante(p) for p in personas)
print("¿Todos son estudiantes?:", todos_estudiantes)
