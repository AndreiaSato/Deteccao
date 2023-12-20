import cv2

carrega = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #carrega a biblioteca haarcascade

imagem = cv2.imread('WhatsApp Image 2023-07-18 at 19.21.51.jpeg') #carrega a imagem

imagemcinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY) #transforma em tom de cinza

faces = carrega.detectMultiScale(imagemcinza)#carrega em multiescalas a imagem

print(faces) #imprime a imgaem

for(x, y, l, a) in faces:
    cv2.rectangle(imagem, (x,y), (x + l, y + a), (0, 255, 0), 2)

cv2.imshow('faces', imagem)
cv2.waitKey()