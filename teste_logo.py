import cv2
imagem = cv2.imread('Logo/teste/foofighters2.png')

classificador = cv2.CascadeClassifier('cascade_logo.xml')

imagemcinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

deteccoes = classificador.detectMultiScale(imagemcinza)

print(deteccoes)
print(len(deteccoes))

for (x, y, l, a) in deteccoes:
    cv2.rectangle(imagem, (x,y), (x + l, y + a), (0,255,0), 2)

cv2.imshow('Detector de logos', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()