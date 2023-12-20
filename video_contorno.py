import cv2
video = cv2.VideoCapture(0)

while True:
    conectado, frame = video.read()
    new = cv2.convertScaleAbs(frame, 1.0, 1.5)

    imagemcinza = cv2.cvtColor(new, cv2.COLOR_BGR2GRAY)

    ret,thresh = cv2.threshold(imagemcinza, 127, 255, 0)
    contornos, hierarquuia = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for i in contornos:
        if i.size > 100:
            cv2.drawContours(frame, i, -1, (0, 0, 255), 2)
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()