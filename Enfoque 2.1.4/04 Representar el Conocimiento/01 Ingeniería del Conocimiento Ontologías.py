# Importamos la librería Owlready2 para trabajar con ontologías en formato OWL
from owlready2 import *

# Creamos una nueva ontología
onto = get_ontology("http://example.org/onto.owl")

with onto:
    # Definimos una clase Persona
    class Persona(Thing):
        pass

    # Definimos una propiedad 'tieneNombre' asociada a la clase Persona
    class tieneNombre(DataProperty):
        domain = [Persona]  # Se aplica a instancias de Persona
        range = [str]       # El tipo de dato es string

# Creamos una instancia de la clase Persona
persona1 = onto.Persona("juan")
persona1.tieneNombre = ["Juan Pérez"]  # Le asignamos un nombre

# Guardamos la ontología en un archivo
onto.save(file="ontologia.owl")
