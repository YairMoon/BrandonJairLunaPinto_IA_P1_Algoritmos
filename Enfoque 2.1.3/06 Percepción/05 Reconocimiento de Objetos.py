import cv2  # Importamos OpenCV para procesamiento de imágenes.

# Cargar un clasificador Haar (detector de rostros)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') 
# Cargamos el clasificador Haar preentrenado para detección de rostros.
# `cv2.data.haarcascades` proporciona la ruta a los clasificadores Haar incluidos en OpenCV.

# Cargar una imagen
img = cv2.imread("ruta_a_imagen.jpg")
# Leemos la imagen desde la ruta especificada. Asegúrate de reemplazar "ruta_a_imagen.jpg" con la ruta real de tu imagen.

# Convertir a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Convertimos la imagen a escala de grises, ya que el clasificador Haar funciona mejor con imágenes en escala de grises.

# Detectar rostros
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# Detectamos rostros en la imagen utilizando el clasificador Haar.
# Parámetros:
# - `1.1`: Factor de escala para reducir la imagen en cada paso.
# - `4`: Número mínimo de vecinos que un rectángulo debe tener para ser considerado un rostro.

# Dibujar los rectángulos alrededor de los rostros detectados
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    # Dibujamos un rectángulo azul (255, 0, 0) alrededor de cada rostro detectado.
    # `(x, y)` es la esquina superior izquierda, `(x + w, y + h)` es la esquina inferior derecha.
    # `2` es el grosor del rectángulo.

# Mostrar la imagen
cv2.imshow("Reconocimiento de Objetos", img)
# Mostramos la imagen con los rostros detectados en una ventana.

cv2.waitKey(0)  # Esperamos a que se presione una tecla para cerrar la ventana.
cv2.destroyAllWindows()  # Cerramos todas las ventanas abiertas por OpenCV.

# Este código utiliza un clasificador Haar para detectar rostros en una imagen.
# Carga la imagen, la convierte a escala de grises y luego aplica el detector de rostros.
# Finalmente, dibuja rectángulos alrededor de los rostros detectados y muestra la imagen resultante.