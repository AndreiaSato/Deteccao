import cv2
img = cv2.imread('img_1.png')
cv2.imshow('img', img)
img = cv2.convertScaleAbs(img, 2.0, 2.2)

cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('cinza', cinza)

_, bin = cv2.threshold(cinza, 90, 255, cv2.THRESH_BINARY)
#cv2.imshow('bin', bin)

desfoque = cv2.GaussianBlur(bin, (5, 5), 0)
#cv2.imshow('des', desfoque)

contornos, hier = cv2.findContours(desfoque, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) #retr_tree - contorno dentro de contorno

cv2.drawContours(img, contornos, -1, (0, 255, 0), 2)
cv2.imshow('cont', img)



cv2.waitKey(0)
cv2.destroyAllWindows()
