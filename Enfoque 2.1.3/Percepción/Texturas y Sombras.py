import cv2
import numpy as np

# Cargar una imagen
img = cv2.imread("ruta_a_imagen.jpg", cv2.IMREAD_GRAYSCALE)

# Aplicar un filtro Sobel para detectar bordes (simulando texturas)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Mostrar la imagen con efectos de texturas
cv2.imshow("Textura Sobel-X", sobelx)
cv2.imshow("Textura Sobel-Y", sobely)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Este código carga una imagen en escala de grises y aplica un filtro Sobel para detectar bordes en ambas direcciones (X e Y). Luego, muestra las imágenes resultantes con los efectos de textura.
# Asegúrate de reemplazar "ruta_a_imagen.jpg" con la ruta real de tu imagen.