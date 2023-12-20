import cv2

video = cv2.VideoCapture(0) #caso haja mais de uma câmera, alterar os valores (1), (2)
classificador = cv2.CascadeClassifier('cascade_caneca3.xml')

while True:
    conectado, frame = video.read() #usar a varável conectado pela sintaxe video.read() / frame - captura de tempos em tempos do vídeo

    imagemCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #para fazer a conversão

    deteccoes = classificador.detectMultiScale(imagemCinza, scaleFactor=1.3, minNeighbors=9, minSize=(60, 60))
    for (x, y, l, a) in deteccoes:
        cv2.rectangle(frame, (x, y), (x + l, y + a), (0, 0, 255), 2)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) == ord('q'):
        break                        # waitkey (1) significa que o sistema vai esperar vc digitar uma tecla, sendo o ('q') para parar

video.release()
cv2.destroyAllWindows()
