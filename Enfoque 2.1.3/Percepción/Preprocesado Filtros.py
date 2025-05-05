import cv2
import numpy as np

# Cargar una imagen
img = cv2.imread("C:\Users\Jair\Desktop\BrandonJairLunaPinto_IA_P1_Algoritmos\carro.jpeg", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error al cargar la imagen. Verifica la ruta.")
else:
    print("Imagen cargada correctamente.")


# Aplicar un filtro de suavizado (Gaussian blur)
filtro_suavizado = cv2.GaussianBlur(img, (5, 5), 0)

# Mostrar la imagen original y la filtrada
cv2.imshow("Original", img)
cv2.imshow("Imagen Filtrada", filtro_suavizado)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Este código carga una imagen en escala de grises y aplica un filtro de suavizado utilizando Gaussian Blur. Luego, muestra la imagen original y la imagen filtrada.
# Asegúrate de reemplazar "ruta_a_imagen.jpg" con la ruta real de tu imagen.