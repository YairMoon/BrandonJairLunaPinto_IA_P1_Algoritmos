import cv2
import numpy as np

# Cargar la imagen
img = cv2.imread("ruta_a_imagen.jpg", cv2.IMREAD_GRAYSCALE)

# Aplicar el operador de Canny para detectar bordes
edges = cv2.Canny(img, 50, 150, apertureSize=3)

# Detectar líneas usando la transformada de Hough
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=50, maxLineGap=10)

# Dibujar las líneas detectadas
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Mostrar la imagen con las líneas etiquetadas
cv2.imshow("Imagen con Líneas Etiquetadas", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Este código carga una imagen en escala de grises, aplica el operador de Canny para detectar bordes y luego utiliza la transformada de Hough para detectar líneas. Finalmente, dibuja las líneas detectadas sobre la imagen original y muestra el resultado.   