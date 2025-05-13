import cv2  # Importamos OpenCV para procesamiento de imágenes.
import numpy as np  # Importamos NumPy para operaciones con matrices.

# Cargar una imagen
img = cv2.imread("ruta_a_imagen.jpg", cv2.IMREAD_GRAYSCALE)
# Leemos la imagen desde la ruta especificada y la convertimos a escala de grises.
# Asegúrate de reemplazar "ruta_a_imagen.jpg" con la ruta real de tu imagen.

# Aplicar un filtro Sobel para detectar bordes (simulando texturas)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
# Detectamos bordes en la dirección X utilizando el filtro Sobel.
# Parámetros:
# - `cv2.CV_64F`: Tipo de dato de salida (64 bits flotante).
# - `1, 0`: Derivada en X (1) y en Y (0).
# - `ksize=3`: Tamaño del kernel (3x3).

sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
# Detectamos bordes en la dirección Y utilizando el filtro Sobel.
# Parámetros:
# - `0, 1`: Derivada en X (0) y en Y (1).

# Mostrar la imagen con efectos de texturas
cv2.imshow("Textura Sobel-X", sobelx)
# Mostramos la imagen resultante del filtro Sobel en la dirección X.

cv2.imshow("Textura Sobel-Y", sobely)
# Mostramos la imagen resultante del filtro Sobel en la dirección Y.

cv2.waitKey(0)  # Esperamos a que se presione una tecla para cerrar las ventanas.
cv2.destroyAllWindows()  # Cerramos todas las ventanas abiertas por OpenCV.

# Este código carga una imagen en escala de grises y aplica un filtro Sobel para detectar bordes en ambas direcciones (X e Y).
# Luego, muestra las imágenes resultantes con los efectos de textura.