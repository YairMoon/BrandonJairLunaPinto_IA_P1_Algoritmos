# Red semántica básica representada como un grafo
red_semantica = {
    "Perro": ["Animal"],
    "Animal": ["Ser Vivo"],
    "Gato": ["Animal"]
}

# Función para recorrer la jerarquía de una palabra
def recorrer_red(nodo):
    while nodo in red_semantica:
        nodo = red_semantica[nodo][0]
        print("Sube a:", nodo)

recorrer_red("Gato")
# La salida mostrará la jerarquía de la palabra "Gato" subiendo a través de la red semántica.
# La jerarquía es: Gato -> Animal -> Ser Vivo