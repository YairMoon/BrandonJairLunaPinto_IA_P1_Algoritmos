import random  # Importamos la librería random para manejar la aleatoriedad.

class EntornoLineal:
    """
    Entorno simple donde el agente parte del estado 0 y quiere llegar al estado final (meta).
    Cada acción incorrecta penaliza, y llegar a la meta recompensa.
    """
    def __init__(self):
        # Definimos el estado final (meta) y el estado inicial.
        self.estado_final = 4  # El objetivo es llegar al estado 4.
        self.estado = 0        # Comenzamos en el estado 0.

    def reset(self):
        """
        Reinicia el entorno al estado inicial.
        """
        self.estado = 0  # Reiniciamos el estado al inicial.
        return self.estado  # Retornamos el estado inicial.

    def acciones(self, estado):
        """
        Devuelve las acciones disponibles desde un estado.
        """
        return [0, 1]  # 0 = quedarse, 1 = avanzar.

    def step(self, accion):
        """
        Ejecuta una acción y devuelve el nuevo estado y la recompensa obtenida.
        """
        if accion == 1:  # Si la acción es avanzar.
            self.estado = min(self.estado + 1, self.estado_final)  # Avanzamos al siguiente estado sin exceder la meta.
        # Si la acción es quedarse, el estado no cambia.

        recompensa = 10 if self.estado == self.estado_final else -1  # Recompensa por llegar a la meta o penalización.
        return self.estado, recompensa  # Retornamos el nuevo estado y la recompensa.


def evaluar_politica(politica, entorno, episodios=100):
    """
    Evalúa cuán buena es una política promediando la recompensa total en varios episodios.

    Parámetros:
    - politica: diccionario que define la acción a tomar en cada estado.
    - entorno: instancia del entorno donde el agente interactúa.
    - episodios: número de episodios para evaluar la política.

    Retorna:
    - Promedio de la recompensa total obtenida en los episodios.
    """
    recompensa_total = 0  # Inicializamos la recompensa total en 0.
    for _ in range(episodios):  # Iteramos sobre el número de episodios.
        estado = entorno.reset()  # Reiniciamos el entorno al estado inicial.
        total = 0  # Inicializamos la recompensa acumulada del episodio.

        while estado != entorno.estado_final:  # Mientras no lleguemos al estado final.
            accion = politica[estado]  # Seleccionamos la acción según la política.
            estado, recompensa = entorno.step(accion)  # Ejecutamos la acción y obtenemos el nuevo estado y recompensa.
            total += recompensa  # Acumulamos la recompensa.

        recompensa_total += total  # Sumamos la recompensa del episodio a la recompensa total.

    return recompensa_total / episodios  # Retornamos el promedio de la recompensa total.


def busqueda_politica(entorno, iteraciones=1000):
    """
    Realiza búsqueda aleatoria de políticas y se queda con la mejor encontrada.

    Parámetros:
    - entorno: instancia del entorno donde el agente interactúa.
    - iteraciones: número de iteraciones para buscar políticas.

    Retorna:
    - mejor_politica: la mejor política encontrada.
    """
    # Generamos una política inicial aleatoria.
    politica_actual = {s: random.choice(entorno.acciones(s)) for s in range(entorno.estado_final)}
    mejor_politica = politica_actual.copy()  # Inicializamos la mejor política como la actual.
    mejor_valor = evaluar_politica(politica_actual, entorno)  # Evaluamos la política inicial.

    print("Evaluación inicial:", mejor_valor)  # Mostramos la evaluación inicial.

    for i in range(iteraciones):  # Iteramos sobre el número de iteraciones.
        # Crear una nueva política mutando una acción.
        nueva_politica = mejor_politica.copy()  # Copiamos la mejor política actual.
        estado_random = random.randint(0, entorno.estado_final - 1)  # Seleccionamos un estado aleatorio.
        nueva_politica[estado_random] = random.choice(entorno.acciones(estado_random))  # Mutamos la acción.

        valor = evaluar_politica(nueva_politica, entorno)  # Evaluamos la nueva política.

        # Si la nueva política es mejor, la adoptamos.
        if valor > mejor_valor:
            mejor_politica = nueva_politica  # Actualizamos la mejor política.
            mejor_valor = valor  # Actualizamos el mejor valor.

    return mejor_politica  # Retornamos la mejor política encontrada.


# ----------------------------
# Ejemplo de uso
# ----------------------------
if __name__ == "__main__":
    entorno = EntornoLineal()  # Creamos una instancia del entorno.

    politica = busqueda_politica(entorno)  # Buscamos la mejor política.

    # Mostramos la política final aprendida.
    print("\nPolítica final aprendida:")
    for estado in sorted(politica):  # Iteramos sobre los estados en orden.
        accion = politica[estado]  # Obtenemos la acción para el estado.
        accion_texto = "Avanzar" if accion == 1 else "Quedarse"  # Convertimos la acción a texto.
        print(f"Estado {estado}: {accion_texto}")  # Mostramos la acción óptima para cada estado.