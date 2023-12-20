import cv2

#lendo a imagem
image = cv2.imread('img.png')

#convertendo a imagem para o formato de escala cinza
img_cinza = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#aplicando o limiar binário
ret, thresh = cv2.threshold(img_cinza, 60, 255, cv2.THRESH_BINARY)

#visualizando a imagem binária
cv2.imshow('Imagem Binária', thresh)

'''
#copiando parte da imagem
copia = image[100:1000, 80:1500]

#mostrando a copia
cv2.imshow('Copia', copia)

#salavndo a imagem copiada
cv2.imwrite('Copia.png', copia)'''

#recortando a imagem

y = 200
h = 500

x =500
w = 400

croped = image[y:y+h, x:x+w]

cv2.imshow('image', croped)
cv2.waitKey(0)
cv2.destroyAllWindows()






