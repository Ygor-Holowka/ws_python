import cv2 as cv 

camera = cv.VideoCapture(1)
rodando = True

while rodando:
    status, frame = camera.read()
    if not status or cv.waitKey(1) & 0xff == ord('q'):
        rodando = False
    frame = cv.flip(frame, 1)
    cv.imshow("Camera", frame)