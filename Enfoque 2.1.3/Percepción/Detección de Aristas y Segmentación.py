import cv2
import numpy as np

# Cargar la imagen
img = cv2.imread("C:\Users\Jair\Desktop\BrandonJairLunaPinto_IA_P1_Algoritmos\carro.jpeg", cv2.IMREAD_GRAYSCALE)

# Aplicar un filtro Canny para detección de aristas
aristas = cv2.Canny(img, 100, 200)

# Mostrar la imagen original y la imagen con aristas
cv2.imshow("Imagen Original", img)
cv2.imshow("Aristas Detectadas", aristas)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Este código carga una imagen en escala de grises y aplica un filtro Canny para detectar aristas. Luego, muestra la imagen original y la imagen con las aristas detectadas.
# Asegúrate de reemplazar "ruta_a_imagen.jpg" con la ruta real de tu imagen.