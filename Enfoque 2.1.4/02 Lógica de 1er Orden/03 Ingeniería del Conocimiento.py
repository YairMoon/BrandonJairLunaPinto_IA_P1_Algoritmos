# Base simple de conocimientos y hechos

# Hechos conocidos
conocimiento = {
    "mamifero": ["perro", "gato"],
    "vuela": ["pajaro"],
}

# Reglas de inferencia para obtener nuevos hechos
def es_mamifero(animal):
    return animal in conocimiento["mamifero"]

def puede_volar(animal):
    return animal in conocimiento["vuela"]

print("¿El perro es mamífero?", es_mamifero("perro"))
print("¿El gato puede volar?", puede_volar("gato"))
# La salida mostrará si el perro es un mamífero y si el gato puede volar.
# En este caso, el perro es un mamífero y el gato no puede volar según la base de conocimiento proporcionada.