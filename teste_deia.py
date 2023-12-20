import cv2
imagem = cv2.imread('img_1.png') #carrega a imagem
imagem2 = imagem
imagem2 = cv2.convertScaleAbs(imagem2, 2.0, 2.2)

imagemcinza2 = cv2.cvtColor(imagem2, cv2.COLOR_BGR2GRAY) #transformar em escala de cinza / (imagem binarizada)

ret2, thresh2 = cv2.threshold(imagemcinza2, 127, 255, 0) # threshold - binarizar a imagem (preto e branco)
countours2, hierarchy2 = cv2.findContours(thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for i in countours2:
    if i.size >= 1:
        cv2.drawContours(imagem, i, -1, (1, 255, 0), 2)


cv2.imshow('imagem', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
