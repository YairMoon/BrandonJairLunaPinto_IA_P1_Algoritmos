import cv2

# Cargar un clasificador Haar (detector de rostros)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Cargar una imagen
img = cv2.imread("ruta_a_imagen.jpg")

# Convertir a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detectar rostros
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Dibujar los rectángulos alrededor de los rostros detectados
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Mostrar la imagen
cv2.imshow("Reconocimiento de Objetos", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Este código utiliza un clasificador Haar para detectar rostros en una imagen. Carga la imagen, la convierte a escala de grises y luego aplica el detector de rostros. Finalmente, dibuja rectángulos alrededor de los rostros detectados y muestra la imagen resultante.          
