# Razonamiento por defecto: Todos los pájaros vuelan... excepto algunos casos
class Pajaro:
    def __init__(self, nombre, puede_volar=True):
        self.nombre = nombre
        self.puede_volar = puede_volar

# Creamos algunos pájaros
loro = Pajaro("Loro")
pinguino = Pajaro("Pingüino", puede_volar=False)

# Verificamos si pueden volar
for ave in [loro, pinguino]:
    print(f"{ave.nombre} puede volar: {ave.puede_volar}")
# La salida mostrará si cada pájaro puede volar o no.
# En este caso, el loro puede volar, mientras que el pingüino no puede. Esto ilustra el razonamiento por defecto: asumimos que todos los pájaros pueden volar, pero hay excepciones.