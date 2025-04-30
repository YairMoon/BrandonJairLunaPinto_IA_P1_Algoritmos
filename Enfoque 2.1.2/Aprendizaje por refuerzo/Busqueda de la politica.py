import random

class EntornoLineal:
    """
    Entorno simple donde el agente parte del estado 0 y quiere llegar al estado final (meta).
    Cada acción incorrecta penaliza, y llegar a la meta recompensa.
    """
    def __init__(self):
        self.estado_final = 4  # El objetivo es llegar al estado 4
        self.estado = 0        # Comenzamos en el estado 0

    def reset(self):
        """
        Reinicia el entorno al estado inicial.
        """
        self.estado = 0
        return self.estado

    def acciones(self, estado):
        """
        Devuelve las acciones disponibles desde un estado.
        """
        return [0, 1]  # 0 = quedarse, 1 = avanzar

    def step(self, accion):
        """
        Ejecuta una acción y devuelve el nuevo estado y la recompensa obtenida.
        """
        if accion == 1:
            self.estado = min(self.estado + 1, self.estado_final)

        recompensa = 10 if self.estado == self.estado_final else -1
        return self.estado, recompensa


def evaluar_politica(politica, entorno, episodios=100):
    """
    Evalúa cuán buena es una política promediando la recompensa total en varios episodios.
    """
    recompensa_total = 0
    for _ in range(episodios):
        estado = entorno.reset()
        total = 0
        while estado != entorno.estado_final:
            accion = politica[estado]
            estado, recompensa = entorno.step(accion)
            total += recompensa
        recompensa_total += total
    return recompensa_total / episodios


def busqueda_politica(entorno, iteraciones=1000):
    """
    Realiza búsqueda aleatoria de políticas y se queda con la mejor encontrada.
    """
    # Genera política inicial aleatoria
    politica_actual = {s: random.choice(entorno.acciones(s)) for s in range(entorno.estado_final)}
    mejor_politica = politica_actual.copy()
    mejor_valor = evaluar_politica(politica_actual, entorno)

    print("Evaluación inicial:", mejor_valor)

    for i in range(iteraciones):
        # Crear una nueva política mutando una acción
        nueva_politica = mejor_politica.copy()
        estado_random = random.randint(0, entorno.estado_final - 1)
        nueva_politica[estado_random] = random.choice(entorno.acciones(estado_random))

        valor = evaluar_politica(nueva_politica, entorno)

        # Si es mejor, la adoptamos
        if valor > mejor_valor:
            mejor_valor = valor
            mejor_politica = nueva_politica
            print(f"Iteración {i}: Nueva mejor política con valor esperado {mejor_valor:.2f}")

    return mejor_politica


# ----------------------------
# Ejemplo de uso
# ----------------------------
if __name__ == "__main__":
    entorno = EntornoLineal()
    politica = busqueda_politica(entorno)

    print("\nPolítica final aprendida:")
    for estado in sorted(politica):
        accion = politica[estado]
        accion_txt = "Avanzar" if accion == 1 else "Quedarse"
        print(f"Estado {estado}: {accion_txt}")
