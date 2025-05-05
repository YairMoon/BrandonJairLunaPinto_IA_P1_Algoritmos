import cv2

# Capturar video desde la cámara
cap = cv2.VideoCapture(0)

# Leer el primer frame
ret, frame_anterior = cap.read()

while True:
    # Leer el siguiente frame
    ret, frame_actual = cap.read()

    # Convertir a escala de grises
    frame_anterior_gray = cv2.cvtColor(frame_anterior, cv2.COLOR_BGR2GRAY)
    frame_actual_gray = cv2.cvtColor(frame_actual, cv2.COLOR_BGR2GRAY)

    # Calcular el flujo óptico (movimiento) usando el método Farneback
    flujo_optico = cv2.calcOpticalFlowFarneback(frame_anterior_gray, frame_actual_gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)

    # Mostrar el flujo óptico
    cv2.imshow("Flujo Óptico (Movimiento)", flujo_optico)

    # Actualizar el frame anterior
    frame_anterior = frame_actual

    # Detener si presionamos la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
# Este código captura video desde la cámara y calcula el flujo óptico entre frames consecutivos utilizando el método de Farneback. Muestra el flujo óptico en tiempo real y se detiene al presionar la tecla 'q'.