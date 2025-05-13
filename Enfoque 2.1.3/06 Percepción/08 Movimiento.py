import cv2  # Importamos OpenCV para capturar video y procesar imágenes.

# Capturar video desde la cámara
cap = cv2.VideoCapture(0)  # Iniciamos la captura de video desde la cámara (índice 0 para la cámara predeterminada).

# Leer el primer frame
ret, frame_anterior = cap.read()  # Leemos el primer frame del video.

while True:
    # Leer el siguiente frame
    ret, frame_actual = cap.read()  # Capturamos el siguiente frame del video.

    # Convertir a escala de grises
    frame_anterior_gray = cv2.cvtColor(frame_anterior, cv2.COLOR_BGR2GRAY)  # Convertimos el frame anterior a escala de grises.
    frame_actual_gray = cv2.cvtColor(frame_actual, cv2.COLOR_BGR2GRAY)  # Convertimos el frame actual a escala de grises.

    # Calcular el flujo óptico (movimiento) usando el método Farneback
    flujo_optico = cv2.calcOpticalFlowFarneback(
        frame_anterior_gray, frame_actual_gray, None, 0.5, 3, 15, 3, 5, 1.2, 0
    )
    # Calculamos el flujo óptico entre los frames consecutivos usando el método de Farneback.
    # Parámetros:
    # - 0.5: Escala de la imagen.
    # - 3: Número de niveles en la pirámide.
    # - 15: Tamaño de la ventana para el cálculo.
    # - 3: Iteraciones por nivel.
    # - 5: Tamaño del filtro de derivadas.
    # - 1.2: Sigma del filtro gaussiano.
    # - 0: Indicador de operación (0 para el método estándar).

    # Mostrar el flujo óptico
    cv2.imshow("Flujo Óptico (Movimiento)", flujo_optico)  # Mostramos el flujo óptico en una ventana.

    # Actualizar el frame anterior
    frame_anterior = frame_actual  # Actualizamos el frame anterior con el frame actual.

    # Detener si presionamos la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Si se presiona la tecla 'q', salimos del bucle.
        break

# Liberar recursos
cap.release()  # Liberamos la cámara.
cv2.destroyAllWindows()  # Cerramos todas las ventanas abiertas por OpenCV.

# Este código captura video desde la cámara y calcula el flujo óptico entre frames consecutivos utilizando el método de Farneback.
# Muestra el flujo óptico en tiempo real y se detiene al presionar la tecla 'q'.