# Creamos una jerarquía de clases en Python que simula una taxonomía
class Animal:
    pass

class Mamifero(Animal):
    pass

class Ave(Animal):
    pass

class Perro(Mamifero):
    pass

class Gato(Mamifero):
    pass

# Instanciamos un objeto de la clase Perro
mi_perro = Perro()
print("Mi perro es un mamífero:", isinstance(mi_perro, Mamifero))  # True
