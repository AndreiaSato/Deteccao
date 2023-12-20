import cv2
lista = list()
imagem = cv2.imread('Logo/teste/foofighters.jpg')
classificador = cv2.CascadeClassifier('cascade_logo.xml')
imagemcinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
deteccoes = classificador.detectMultiScale(imagemcinza, minNeighbors=4, scaleFactor=1.2)

for (x, y, l, a) in deteccoes:
    roi = imagem[y:y + l, x:x +a]
    roi_cinza = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, roi_binaria = cv2.threshold(roi_cinza, 127, 255, 0)
    contornos, hierarchy = cv2.findContours(roi_binaria, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(roi, contornos, -1, (1, 255, 0),4)

cv2.imshow("Imagem com contornos", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()