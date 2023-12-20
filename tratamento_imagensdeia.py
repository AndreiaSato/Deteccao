import cv2
im = cv2.imread('img.png')
new = cv2.convertScaleAbs(im, 1.0, 2.2)

imagemcinza = cv2.cvtColor(new, cv2.COLOR_BGR2GRAY)
ret2,thresh2 = cv2.threshold(imagemcinza, 127, 255, 0)
contours2, hierarchy2 = cv2.findContours(thresh2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for i in contours2:
    if i. size >= 1000:
        cv2.drawContours(im, i, -1, (0, 255, 0), 2)
cv2.imshow('teste', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
